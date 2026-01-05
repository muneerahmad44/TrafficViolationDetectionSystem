# 🚦 Traffic Violation Detection System

An advanced AI-powered system for automated traffic enforcement, specializing in motorcycle helmet compliance monitoring and license plate recognition using state-of-the-art computer vision techniques.

---

## 🎯 Key Features

### Intelligent Motorcycle Monitoring
- **Video-based detection system** capable of identifying and tracking moving motorcycles in real-time
- **Advanced classification engine** supporting 35+ predefined helmet configuration classes for comprehensive rider-passenger scenarios
- **Smart post-classification association logic** that accurately links detected helmet configurations with corresponding motorcycles using:
  - Spatial relationship analysis
  - Motion-based tracking cues
  - Multi-object correlation algorithms

### Conditional Enforcement Pipeline
- **Selective license plate detection** triggered only for non-compliant or rule-violating configurations
- **Automated violation flagging** to support traffic enforcement workflows
- **Configurable detection logic** for testing and production environments

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

The processed output video will be saved in the same directory.

---

## 📹 Sample Videos & Demonstrations

### Test Video
**testvideo.mp4** - Original test footage used for violation detection validation
- [Download Test Video](https://drive.google.com/file/d/1wfPZZyaz4aD0iZJ9cIelDkR-GaoH5mTr/view?usp=sharing)

### Output Videos

#### 📹 processed_out1.mp4 (Testing Mode)
Demonstrates license plate detection capabilities using **inverted logic** for testing purposes. Since all riders in the test video wear helmets, the system was configured to detect plates when helmets ARE present, showcasing the plate detection functionality.

**Purpose:** Validation of license plate recognition module
- [View Output 1](https://drive.google.com/file/d/1GD5Hs8HecBoY3lVsMyyCi-tSPuDNeqv0/view?usp=sharing)

#### 📹 output_processed2.mp4 (Production Mode)
Shows the **correct production logic** where license plates are detected only when riders are NOT wearing helmets (actual violation detection). As all riders in the test video are compliant, no license plates are detected.

**Purpose:** Real-world enforcement scenario
- [View Output 2](https://drive.google.com/file/d/1BEez7XZ5qpoX0x3Of5e-2M_4jEoDThhf/view?usp=sharing)

---

## 📊 System Architecture

### Flow Diagram
For a comprehensive understanding of the system architecture, processing pipeline, and workflow logic, refer to the detailed flow diagram:

- [View Complete System Flow](https://github.com/muneerahmad44/TrafficViolationDetectionSystem/blob/main/flowchart/completeflow.png)

### Processing Pipeline

1. **Video Input** → Frame extraction and preprocessing
2. **Motorcycle Detection** → Identification of moving bikes in the scene
3. **Helmet Classification** → Analysis of rider-passenger configurations (35+ classes)
4. **Association Logic** → Linking helmet status with specific motorcycles
5. **Conditional Plate Detection** → Triggering license plate recognition for violations
6. **Output Generation** → Annotated video with violation markers

---

## 🤖 Model Details

- **Architecture:** YOLOv11s (Small variant, fine-tuned)
- **Primary Task:** Helmet detection and classification
- **Secondary Task:** License plate recognition
- **Dataset:** Labeled motorcycle dataset from Myanmar (2016)
- **Training Strategy:** Transfer learning with fine-tuning on domain-specific data
- **Classification Categories:** 35+ distinct helmet configuration classes covering:
  - Single rider scenarios
  - Rider-passenger combinations
  - Helmet compliance states
  - Edge cases and special configurations

---

## 🔮 Future Roadmap

### Phase 1: Database Integration
- Extract and store license plate numbers in structured database
- Maintain violation records with timestamps and evidence
- Build query interface for enforcement officers

### Phase 2: E-Challan System
- Automatic e-challan generation for registered vehicles
- Integration with vehicle registration databases
- Notification system for vehicle owners


## ⚠️ Current Limitations

- **Testing Scope:** System validated primarily on provided test video due to computational constraints
- **Single Source:** Currently processes one video stream at a time
- **No Persistence:** Database integration pending for violation record storage
- **Resource Requirements:** Requires adequate GPU resources for optimal real-time performance
- **Dataset Specificity:** Model trained on Myanmar dataset may require fine-tuning for other regions
- **Environmental Factors:** Performance may vary under extreme weather or lighting conditions

---

## 🛠️ Technical Requirements

### Minimum Requirements
- Python 3.8+
- 8GB RAM
- CUDA-compatible GPU (recommended) can also be runed on the cpu but fps is very low
- OpenCV 4.x
- YOLOv11 dependencies



---

## 📄 License

MIT License

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests, report issues, or suggest new features.

---

## 📧 Contact

For questions, suggestions, or collaboration contact at muneerahmed.dev@gmail.com

---

**Built with ❤️ using YOLOv11s**

*Advancing road safety through intelligent computer vision*
