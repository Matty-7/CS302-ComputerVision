from ultralytics import YOLO

model = YOLO('yolov8x')

result = model.predict('Tennis/input_videos/image.png', save=True)

print(result)

print("boxes:")

for box in result[0].boxes:
    print(box)