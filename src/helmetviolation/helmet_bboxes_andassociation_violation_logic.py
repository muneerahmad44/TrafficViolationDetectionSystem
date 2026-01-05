import cv2
def check_driver_helmet(class_label):
    """
    Returns True if DRIVER is wearing a helmet,
    False if DRIVER is not wearing a helmet.
    """
    if class_label.startswith("DNoHelmet"):
        return True
    elif class_label.startswith("DHelmet"):
        return False
    else:
        raise ValueError(f"Invalid class label: {class_label}")

def calculate_iou(box1, box2):
    """Calculate Intersection over Union between two boxes"""
    x1_min, y1_min, x1_max, y1_max = box1
    x2_min, y2_min, x2_max, y2_max = box2
    
    # Calculate intersection area
    inter_x_min = max(x1_min, x2_min)
    inter_y_min = max(y1_min, y2_min)
    inter_x_max = min(x1_max, x2_max)
    inter_y_max = min(y1_max, y2_max)
    
    if inter_x_max < inter_x_min or inter_y_max < inter_y_min:
        return 0.0
    
    inter_area = (inter_x_max - inter_x_min) * (inter_y_max - inter_y_min)
    
    # Calculate union area
    box1_area = (x1_max - x1_min) * (y1_max - y1_min)
    box2_area = (x2_max - x2_min) * (y2_max - y2_min)
    union_area = box1_area + box2_area - inter_area
    
    return inter_area / union_area if union_area > 0 else 0.0

def calculate_distance(box1, box2):
    """Calculate center-to-center distance between two boxes"""
    x1_center = (box1[0] + box1[2]) / 2
    y1_center = (box1[1] + box1[3]) / 2
    x2_center = (box2[0] + box2[2]) / 2
    y2_center = (box2[1] + box2[3]) / 2
    
    distance = ((x1_center - x2_center)**2 + (y1_center - y2_center)**2)**0.5
    return distance

def helmet_association(helmet_results,class_to_label,annotated_frame,moving_bikes):
    IOU_THRESHOLD = 0.3
    DISTANCE_THRESHOLD = 150 
    for helmet_box in helmet_results[0].boxes:#each detcted helmet box in all boxes for the imageb so loop over all the bioxes in the image detcetd 
        helmet_bbox = helmet_box.xyxy[0].cpu().numpy()#get the helmet bbox 
        helmet_class = int(helmet_box.cls[0])#helmet class 
        cls_label = class_to_label[helmet_class]#helkmet label in english
        
        x1, y1, x2, y2 = map(int, helmet_bbox)
        
        # Draw helmet detection
        cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), (255, 0, 0), 2)#draw the  detected bbox to the frame 
        cv2.putText(annotated_frame, cls_label, (x1, y1-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
        
    #     # Check if this helmet detection indicates driver HAS helmet
        has_helmet = check_driver_helmet(cls_label)
        
        if has_helmet:
            # Find the nearest moving bike
            best_match_id = None
            best_iou = 0
            best_distance = float('inf')
            
            for bike_id, bike_info in moving_bikes.items():
                bike_bbox = bike_info['bbox']
                
                # Calculate IoU
                iou = calculate_iou(helmet_bbox, bike_bbox)
                
                # Calculate distance
                distance = calculate_distance(helmet_bbox, bike_bbox)
                
                # Use IoU as primary metric, distance as secondary
                if iou > IOU_THRESHOLD and iou > best_iou:
                    best_match_id = bike_id
                    best_iou = iou
                    best_distance = distance
                elif iou > 0 and distance < DISTANCE_THRESHOLD and distance < best_distance:
                    best_match_id = bike_id
                    best_distance = distance
                    best_iou = iou
            
            # If we found a matching bike, mark it for license plate detection
            if best_match_id is not None:
                moving_bikes[best_match_id]['has_violation'] = True  # Keeping same variable name for consistency
                moving_bikes[best_match_id]['helmet_class'] = cls_label
                moving_bikes[best_match_id]['helmet_bbox'] = helmet_bbox

    return moving_bikes,annotated_frame