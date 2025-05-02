import cv2
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ultralytics import YOLO

# Phone webcam configuration (Update these values)
PHONE_IP = "Enter your Webcam IP "
PORT = "8080"  # Default port for IP Webcam/DroidCam
STREAM_URL = f"http://{PHONE_IP}:{PORT}/video"  # For IP Webcam
# STREAM_URL = f"http://{PHONE_IP}:{PORT}/mjpegfeed"  # For DroidCam

# Initialize YOLOv8 model
model = YOLO("yolov8n.pt")
vehicle_classes = [2, 3, 5, 7]

# Time estimation parameters
avg_time_per_vehicle = 2  # Adjust based on testing
buffer_time = 10

# Initialize phone webcam stream
cap = cv2.VideoCapture(STREAM_URL)
if not cap.isOpened():
    raise ConnectionError(f"Failed to connect to phone at {STREAM_URL}")

# Create GUI
root = tk.Tk()
root.title("Phone Camera Traffic System")

# Configure styles
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="white")
style.configure("Title.TLabel", font=("Arial", 16, "bold"))

# GUI components
title_label = ttk.Label(root, text="Phone-Based Traffic System", style="Title.TLabel")
title_label.pack(pady=10)

video_label = ttk.Label(root)
video_label.pack(padx=10, pady=10)

stats_label = ttk.Label(root, text="Vehicles: 0 | Time: 0s", style="TLabel")
stats_label.pack(pady=10)

def update_gui():
    ret, frame = cap.read()
    if ret:
        results = model.track(frame, persist=True, classes=vehicle_classes, verbose=False)
        vehicle_count = len(results[0].boxes) if results[0].boxes else 0
        
        estimated_time = (vehicle_count * avg_time_per_vehicle) + buffer_time
        stats_label.config(text=f"Vehicles: {vehicle_count} | Time: {estimated_time}s")
        
        annotated_frame = results[0].plot()
        img = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        
        video_label.imgtk = imgtk
        video_label.configure(image=imgtk)
    
    root.after(10, update_gui)

update_gui()

def on_closing():
    cap.release()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
