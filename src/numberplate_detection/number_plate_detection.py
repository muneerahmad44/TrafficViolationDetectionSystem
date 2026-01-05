from ultralytics import YOLO
import cv2

model = YOLO("/home/muneer/Data/computer vision learning/projects/traffic system/system/helmetviolationandnumberplatedetection/backend/src/numberplate_detection/best.pt")
names=model.model.names
class NPD:  # number plate detection
    def __init__(self):
        pass

    def detect_np(self, img):
        """
        Detect number plates and return bounding boxes
        Returns: list of boxes in format [x1, y1, x2, y2, confidence, class]
        """
        results = model(img, conf=0.5)
        
        return results,names
        
    
    def detect_and_visualize(self, img):
        """
        Detect and return annotated image (for visualization purposes)
        """
        results = model(img, conf=0.5)
        annotated_img = results[0].plot()
        return annotated_img
