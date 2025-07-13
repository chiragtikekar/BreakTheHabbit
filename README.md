# 🛑 BREAK THE HABIT – Nail Biting Detection System

A real-time webcam-based behavior-monitoring tool that helps users break nail-biting habits by detecting hand-to-mouth gestures and providing immediate audio feedback.

---

## 🧠 Project Overview

**BREAK THE HABIT** is a wellness-focused application that uses computer vision to track hand and facial movements via webcam. It identifies when the user's fingers approach their mouth and plays a sound alert to discourage nail-biting behavior. This non-intrusive system can support behavior correction through consistent feedback.

---

## 🛠️ Tech Stack

- **Python**  
- **OpenCV** – for live webcam feed and frame processing  
- **MediaPipe** – for detecting hand and facial landmarks  
- **Winsound** – to play alert sounds on Windows systems  
- *(Cross-platform audio modules can be added for Linux/macOS)*

---

## 🚀 Features

- 👁️ Real-time detection of hand-to-mouth proximity using webcam  
- ✋ Supports all five fingers for accurate and flexible monitoring  
- 🔊 Plays a sound alert whenever fingers approach the lips  
- ⚙️ Sensitivity can be adjusted via threshold values  
- 🧘 Ideal for promoting mindful behavior and reducing unconscious habits

---

## 📷 How It Works

1. **Landmark Detection**: Uses MediaPipe to track hand and face landmarks in each video frame.  
2. **Proximity Calculation**: Computes the Euclidean distance between each fingertip and the upper/lower lip.  
3. **Alert System**: If a fingertip is within the proximity threshold, an audio alert is triggered via Winsound.
