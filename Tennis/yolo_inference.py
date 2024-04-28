from ultralytics import YOLO

model = YOLO('yolov8x')

model.predict('Tennis/input_videos/image.png', save=True)