# 💤 Drowsiness Detection Using OpenCV

## 📘 Overview
This project presents a **Driver Drowsiness Detection System** that helps prevent road accidents caused by fatigue or inattention.  
Using **Computer Vision (OpenCV)** and **Facial Landmark Detection (Dlib)**, the system continuously monitors a driver’s eyes in real time.  
If the driver’s eyes remain closed for a few seconds, the system triggers an **audible alarm** to alert the driver and prevent potential accidents.

---

## 🧠 Key Features
- 👁️ **Real-Time Eye Tracking:** Detects and monitors eye movements using webcam feed.  
- 🧮 **Eye Aspect Ratio (EAR):** Calculates EAR to identify whether eyes are open or closed.  
- 🚨 **Automatic Alert System:** Sounds an alarm when drowsiness is detected.  
- 💻 **Lightweight and Fast:** Runs efficiently on most laptops with standard webcams.  
- 🕶️ **Spectacle-Compatible:** Works even when the driver wears glasses.  

---

## ⚙️ Tech Stack
**Languages:** Python  
**Libraries:** OpenCV, Dlib, NumPy, Imutils, Pygame, Scipy  
**Tools:** Jupyter Notebook / VS Code / PyCharm  
**Operating System:** Windows 8/10/11  

---

## 🧩 System Workflow
1. Capture live video using the webcam.  
2. Detect the driver’s face using Dlib’s frontal face detector.  
3. Extract **68 facial landmarks** to identify eyes.  
4. Calculate **Eye Aspect Ratio (EAR)** — a numerical value representing how open the eyes are.  
5. If EAR < 0.25 for a certain number of consecutive frames, trigger a **drowsiness alert**.  

---

## 📊 Results
| Test Case | Condition | System Behavior | Expected Result |
|------------|------------|------------------|-----------------|
| 101 | Eyes Open | Active | Active |
| 102 | Blinking | Drowsy | Drowsy |
| 103 | Eyes Closed | Sleeping | Sleeping |

✅ The system performs effectively in normal lighting conditions and detects eye closure accurately in real time.

---

## 🔮 Future Enhancements
- 🚗 Integration with vehicle systems for automatic alerts.  
- 📱 Mobile app version for real-time monitoring.  
- 🚦 Traffic sign and signal detection.  
- 🧠 AI-based adaptive drowsiness thresholds.  

---

## 👥 Authors
**Developed by:**  
B. Bhanu Sai Prakash, B. Avinash, B. Naga Karthik, and Ch. Tarun  

**Under the guidance of:**  
Mr. K. V. Subba Raju, Assistant Professor  
Department of Computer Science and Engineering  
MVGR College of Engineering, Vizianagaram, India  

---

## 🏁 Conclusion
This project successfully demonstrates how **Computer Vision and AI** can enhance road safety by monitoring driver alertness.  
By detecting early signs of fatigue, it contributes to the prevention of road accidents and promotes safe driving behavior.
