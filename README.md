# 🚦 Traffic Violation Detection System
An AI-powered system for detecting traffic violations using YOLOv11s, focusing on helmet detection and license plate recognition.
---
## 🚀 Quick Start
### Installation
```bash
git clone https://github.com/muneerahmad44/TrafficViolationDetectionSystem.git
cd TrafficViolationDetectionSystem
```
### Usage
1. **Update video path** in `main.py` with your test video or camera stream
2. **Run the system:**
```bash
PYTHONPATH=. python3 main.py
```
The output video will be saved in the same folder.
---
## 📹 Sample Videos

### Test Video
**testvideo.mp4** - Original test video used for violation detection
- [https://drive.google.com/file/d/1wfPZZyaz4aD0iZJ9cIelDkR-GaoH5mTr/view?usp=sharing]

### Output Videos

#### processed_out1.mp4
This video demonstrates license plate detection using inverted logic (for testing purposes). Since all riders in the test video are wearing helmets, the system was configured to detect license plates when helmets ARE detected, allowing us to showcase the plate detection capability.
- [https://drive.google.com/file/d/1GD5Hs8HecBoY3lVsMyyCi-tSPuDNeqv0/view?usp=sharing]

#### output_processed2.mp4
This video shows the **correct production logic** where license plates are only detected when riders are NOT wearing helmets (violation detection). As all riders in the test video wear helmets, no license plates are detected in this output.
- [https://drive.google.com/file/d/1BEez7XZ5qpoX0x3Of5e-2M_4jEoDThhf/view?usp=sharing]

---
## 📊 System Flow Diagram
For a detailed understanding of the system architecture and workflow, check out the flow diagram:
- [View Flow Diagram](https://github.com/muneerahmad44/TrafficViolationDetectionSystem/blob/main/flowchart/completeflow.png)
---
## 🤖 Model Details
- **Model:** YOLOv11s (fine-tuned)
- **Dataset:** Labeled dataset from Myanmar (2016)
- **Training:** Fine-tuned for helmet detection and number plate recognition
---
## 🔮 Future Work
- Extract number plates and save in database
- Generate e-challan for registered vehicles
- Improve helmet detection and number plate recognition performance
- Integrate multiple CCTV cameras with GPU support
- Add real-time CCTV camera stream processing
---
## ⚠️ Current Limitations
- Tested only on the provided video due to limited resources
- Single video source processing
- No database integration yet
- Requires adequate computational resources for optimal performance
---
## 📝 License
MIT License
---
**Built with ❤️ using YOLOv11s**
