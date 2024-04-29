from ultralytics import YOLO

# model = YOLO('Tennis/models/yolov8x.pt')
model = YOLO('Tennis/models/yolo5_last.pt')

# result = model.predict('Tennis/input_videos/image.png', save=True)
# result = model.predict('Tennis/input_videos/input_video.mp4', save=True)

result = model.predict('Tennis/input_videos/input_video.mp4', conf=0.2, save=True)

print(result)

print("boxes:")

for box in result[0].boxes:
    print(box)