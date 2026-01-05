import math
import cv2
import time
from collections import defaultdict
from ultralytics import YOLO

class CycleDetectionAndMotionDetection:
    def __init__(self):
        self.model = YOLO('yolo11m.pt')
        self.MOVEMENT_THRESHOLD = 10
        
        # Track positions over multiple frames
        self.position_history = defaultdict(list)
        self.movement_status = defaultdict(lambda: None)
        self.FRAMES_TO_CHECK = 20
        
    def detect(self, img):
        # Detect motorcycles (3) and bicycles (1)
        results = self.model.track(img, classes=[3], persist=True)
        return results
    
    def update_position(self, track_id, bbox):
        """Store position history for each track"""
        x1, y1, x2, y2 = bbox
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)
        
        # Add current position to history
        self.position_history[track_id].append((cx, cy))
        
        # Keep only last N frames
        if len(self.position_history[track_id]) > self.FRAMES_TO_CHECK:
            self.position_history[track_id].pop(0)
    
    def check_movement(self, track_id):
        """Check if object is moving based on last N frames"""
        positions = self.position_history[track_id]
        
        # Need at least FRAMES_TO_CHECK positions to calculate
        if len(positions) < self.FRAMES_TO_CHECK:
            return self.movement_status[track_id]
        
        # Calculate total displacement over last N frames
        first_pos = positions[0]
        last_pos = positions[-1]
        
        total_displacement = math.sqrt(
            (last_pos[0] - first_pos[0])**2 + 
            (last_pos[1] - first_pos[1])**2
        )
        
        # Update status
        is_moving = total_displacement > self.MOVEMENT_THRESHOLD
        self.movement_status[track_id] = "Moving" if is_moving else "Stationary"
        
        return self.movement_status[track_id]

