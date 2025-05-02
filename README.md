# Traffic Density Controlled Traffic Signal System

This project is a smart traffic signal system that adjusts the green light timing based on the number of vehicles detected using real-time video input. The goal is to reduce unnecessary waiting time at intersections, improve traffic flow, and optimize signal timing based on actual road conditions.

# About the Project

The system uses a live video feed from a phone camera and applies YOLOv8 object detection to count vehicles. Based on the vehicle count, the signal timing is adjusted dynamically using a simple logic:

- If no vehicles are present, the clearance time is set to 2 seconds.
- For every vehicle detected, 1.5 seconds are added to the green light duration.
- A maximum limit is applied (e.g., 6 vehicles = 10 seconds).

This logic makes the signal system practical and responsive to real-time traffic situations.

# Key Features

- Detects and counts vehicles using YOLOv8 in real-time
- Uses your phone's camera (IP-based feed) as the video input
- Displays vehicle count and estimated green light time on a user-friendly interface
- Simple, adjustable logic to change timings based on traffic density
- Modular and easy to understand code structure

# Technologies Used

- Python 3.11
- OpenCV for video handling
- Ultralytics YOLOv8 for object detection
- Tkinter for GUI
- NumPy for array manipulation

# Getting Started

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/traffic-density-signal.git
cd traffic-density-signal
