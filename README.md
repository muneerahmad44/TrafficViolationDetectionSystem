# 🚦 Traffic Violation Detection System

An AI-powered system for detecting traffic violations using YOLOv11s, focusing on helmet detection and license plate recognition.

---

## 🚀 Quick Start

### Installation

```bash
https://github.com/muneerahmad44/TrafficViolationDetectionSystem.git
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

## 📊 System Flow Diagram

For a detailed understanding of the system architecture and workflow, check out the flow diagram [https://github.com/muneerahmad44/TrafficViolationDetectionSystem/blob/main/flowchart/completeflow.png]

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
