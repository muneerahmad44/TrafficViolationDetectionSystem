from ultralytics import YOLO
import cv2
model=YOLO('/home/muneer/Data/computer vision learning/projects/traffic system/system/helmetviolationandnumberplatedetection/backend/src/helmetviolation/25_epoch_last_model.pt')
class Helemtdetection:
    def __init__(self):
        pass

    def detect(self,img):
        results=model(img)
        
        return results
    


# obj=Helemtdetection()

# cap=cv2.VideoCapture('/home/muneer/Data/computer vision learning/projects/traffic system/system/backend/HelmetViolation/13105484_1920_1080_30fps.mp4')
# frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))

# # Main output video
# output_filename = 'output.mp4'
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter(output_filename, fourcc, fps, (frame_width, frame_height))
# while True:
#     success,frame=cap.read()
#     if not success:
#         print("entered")
#         break
#     print("working")
#     results=obj.detect(frame)
#     result=results.plot()
#     # cv2.imshow("detected",result)
#     out.write(result)
