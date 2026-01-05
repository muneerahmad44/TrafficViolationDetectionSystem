
import cv2
def extract_bbox_moving(results,model,annotated_frame):
        # Process bike detections
    moving_bikes = {}
    stationary_count=0
    moving_count=0
    for box in results[0].boxes:#for the single image get boxes one by one  
        if box.cls[0]==3:
            if box.id is not None:#if box.id tracking id is not none
                track_id = int(box.id[0])#track id of the box
                bbox = box.xyxy[0].cpu().numpy()#bboxes of each box
                
                # Update position history
                model.update_position(track_id, bbox)#update posotion by inserting the bboxes to the track id of each bbox 
                
                # Check movement status
                status = model.check_movement(track_id)#check moment of each decetecd bbox after each 10 frames 
                
                # Count movement status
                if status == "Moving":
                    moving_count += 1
                    moving_bikes[track_id] = {
                        'bbox': bbox,
                        'has_violation': False,
                        'helmet_class': None,
                        'helmet_bbox': None
                    }
                elif status == "Stationary":
                    stationary_count += 1
                
                # Display info
                x1, y1, x2, y2 = map(int, bbox)
                
                # Color based on status
                color = (0, 255, 0) if status == "Moving" else (0, 0, 255)
                
                # Draw bike bbox
                label = f"ID:{track_id} {status}"
                cv2.putText(annotated_frame, label, 
                        (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.5, color, 2)
                cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)

        elif box.cls in [2,5,7]:
            track_id_car=int(box.id[0])
            #draw red and blue line 


    return moving_bikes,annotated_frame,stationary_count,moving_count