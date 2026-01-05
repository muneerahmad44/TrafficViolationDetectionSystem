# Initialize
import cv2
import time
import os
from src.helmetviolation.bikeandmotiondetection import CycleDetectionAndMotionDetection
from src.helmetviolation.HelmetDetection import Helemtdetection
from src.numberplate_detection.number_plate_detection import NPD

from src.helmetviolation.extract_moving_bbox import extract_bbox_moving
from src.helmetviolation.helmet_bboxes_andassociation_violation_logic import helmet_association
from collections import defaultdict

np_detect = NPD()


# Class mapping
class_to_label = {
    0: "DHelmetP1Helmet",
    1: "DHelmet",
    2: "DNoHelmet",
    3: "DNoHelmetP1NoHelmetP2NoHelmet",
    4: "DNoHelmetP0NoHelmet",
    5: "DNoHelmetP1NoHelmet",
    6: "DHelmetP1NoHelmet",
    7: "DNoHelmetP1NoHelmetP2NoHelmet",
    8: "DHelmetP0NoHelmetP1HelmetP2Helmet",
    9: "DNoHelmetP1Helmet",
    10: "DNoHelmetP0NoHelmetP1NoHelmet",
    11: "DHelmetP1NoHelmetP2NoHelmet",
    12: "DHelmetP1NoHelmetP2Helmet",
    13: "DHelmetP0HelmetP1NoHelmetP2Helmet",
    14: "DHelmetP0NoHelmetP1NoHelmet",
    15: "DHelmetP1HelmetP2Helmet",
    16: "DHelmetP0NoHelmetP1NoHelmetP2Helmet",
    17: "DHelmetP0NoHelmetP1Helmet",
    18: "DHelmetP1HelmetP2NoHelmet",
    19: "DHelmetP0NoHelmetP1NoHelmetP2NoHelmet",
    20: "DHelmetP0NoHelmet",
    21: "DNoHelmetP0NoHelmetP1NoHelmetP2NoHelmet",
    22: "DNoHelmetP0HelmetP1NoHelmet",
    23: "DNoHelmetP1NoHelmetP2Helmet",
    24: "DHelmetP1NoHelmetP2NoHelmetP3Helmet",
    25: "DHelmetP0Helmet",
    26: "DHelmetP0HelmetP1NoHelmetP2NoHelmet",
    27: "DHelmetP0HelmetP1Helmet",
    28: "DHelmetP1NoHelmetP2NoHelmetP3NoHelmet",
    29: "DHelmetP0NoHelmetP1NoHelmetP2NoHelmetP3Helmet",
    30: "DNoHelmetP0NoHelmetP1NoHelmetP2Helmet",
    31: "DNoHelmetP0NoHelmetP1Helmet",
    32: "DNoHelmetP0NoHelmetP1NoHelmetP2NoHelmetP3NoHelmet",
    33: "DNoHelmetP1HelmetP2Helmet",
    34: "DHelmetP0HelmetP1HelmetP2Helmet",
    35: "DHelmetP0NoHelmetP1NoHelmetP2NoHelmetP3NoHelmet"
}




model = CycleDetectionAndMotionDetection()
helmet_det = Helemtdetection()
cap = cv2.VideoCapture('testVideo.mp4')

# Video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Main output video
output_filename = 'output_processed.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))

# Store license plate information for each bike
bike_license_plates = {}  # {track_id: {'plate_text': str, 'confidence': float}}

# FPS calculation
frame_count = 0
start_time = time.time()
fps_list = []

# IoU threshold for matching helmet detection to bike
 # Maximum pixel distance to consider proximity

while True:
    loop_start = time.time()
    
    success, frame = cap.read()
    if not success:
        break
    
    frame_count += 1
    
    # Detect bikes/motorcycles
    results = model.detect(frame)#bike detection and motion 
    annotated_frame = frame.copy()
    
    # Store bike information
    
    
    
    
    moving_bikes,annotated_frame,stationary_count,moving_count=extract_bbox_moving(results,model,annotated_frame)

    
    # Run helmet detection on FULL frame
    helmet_results = helmet_det.detect(frame)#detect helmet in each frames 
    
    # Match helmet detections to moving bikes
    moving_bikes , annotated_frame=helmet_association(helmet_results,class_to_label,annotated_frame,moving_bikes)
    
    # Process bikes with helmet - detect license plates
    # Process bikes with helmet - detect license plates
    for bike_id, bike_info in moving_bikes.items():
        if bike_info['has_violation']:  # "has helmet detected"
            # Crop the bike region
            x1, y1, x2, y2 = map(int, bike_info['bbox'])

            # Add some padding to the crop
            padding = 20
            x1 = max(0, x1 - padding)
            y1 = max(0, y1 - padding)
            x2 = min(frame_width, x2 + padding)
            y2 = min(frame_height, y2 + padding)

            bike_crop = frame[y1:y2, x1:x2]

            # Skip if crop is too small
            if bike_crop.shape[0] < 20 or bike_crop.shape[1] < 20:
                continue

            # Detect license plate on cropped bike
            plate_results, names = np_detect.detect_np(bike_crop)

            # Draw license plates on the crop first
            for box in plate_results[0].boxes:
                bbox = box.xyxy[0].cpu().numpy()
                cls = box.cls[0].cpu().numpy()
                cls_label = names  # or class label if needed

                # Coordinates relative to crop
                px1, py1, px2, py2 = map(int, bbox)

                # Draw bbox on the cropped image (optional)
                cv2.rectangle(bike_crop, (px1, py1), (px2, py2), (255, 255, 0), 2)
                cv2.putText(bike_crop, f"{cls_label}", (px1, py1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

                # Map crop coordinates back to original frame
                frame_x1 = x1 + px1
                frame_y1 = y1 + py1
                frame_x2 = x1 + px2
                frame_y2 = y1 + py2

                # Draw license plate bbox on the original annotated frame
                cv2.rectangle(annotated_frame, (frame_x1, frame_y1), (frame_x2, frame_y2), (255, 255, 0), 2)
                cv2.putText(annotated_frame, f"{cls_label}", (frame_x1, frame_y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

                    
              
    
    # Calculate FPS
    loop_time = time.time() - loop_start
    current_fps = 1 / loop_time if loop_time > 0 else 0
    fps_list.append(current_fps)
    if len(fps_list) > 30:
        fps_list.pop(0)
    avg_fps = sum(fps_list) / len(fps_list)
    
    # Display FPS and counts
    cv2.putText(annotated_frame, f"FPS: {avg_fps:.1f}", 
               (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    cv2.putText(annotated_frame, f"Moving: {moving_count} | Stationary: {stationary_count}", 
               (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    
    # # Write frame
    out.write(annotated_frame)
    
    # Display
    # cv2.imshow("Detection", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# print(f"\nProcessing complete!")
# print(f"Main output saved to: {output_filename}")
# print(f"\nDetected License Plates:")
# for bike_id, plate_info in bike_license_plates.items():
#     print(f"  Bike ID {bike_id}: {plate_info['plate_text']} (Confidence: {plate_info['confidence']:.2f})")

cap.release()
out.release()
cv2.destroyAllWindows()