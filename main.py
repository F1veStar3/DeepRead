import cv2
import numpy as np
import torch
import torchvision.transforms as transforms
from torch.autograd import Variable

IMAGE_SIZE = 480
CANVAS_SIZE = 28
BRUSH_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
RADIUS_STEP = 1

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (CANVAS_SIZE, CANVAS_SIZE))
    tensor = transforms.ToTensor()(resized).view(-1, CANVAS_SIZE * CANVAS_SIZE)
    return tensor

def predict_letter(img):
    tensor = preprocess_image(img)
    with torch.no_grad():
        output = net(tensor)
    scores = output[0].detach().numpy()
    max_index = np.argmax(scores)
    return alf[max_index], scores

def draw(event, x, y, flags, param):
    global drawing, radius, last_x, last_y
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if last_x is not None and last_y is not None:
            cv2.line(img, (last_x, last_y), (x, y), BRUSH_COLOR, radius * 2)
        last_x, last_y = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_x, last_y = None, None
    elif event == cv2.EVENT_RBUTTONDOWN:
        img.fill(0)
    elif event == cv2.EVENT_MOUSEWHEEL:
        radius = max(1, radius + (RADIUS_STEP if flags > 0 else -RADIUS_STEP))

net = torch.jit.load(r'DeepReadModel.pt')
net.eval()

img = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), np.uint8)
drawing = False
radius = 10
last_x, last_y = None, None
alf = [chr(i) for i in range(65, 91)]

cv2.namedWindow('Canvas')
cv2.setMouseCallback('Canvas', draw)

while True:
    cv2.imshow('Canvas', img)
    letter, scores = predict_letter(img)
    print(f"Predicted letter: {letter} | Brush size: {radius}")
    if cv2.waitKey(100) == ord('q'):
        break

cv2.destroyAllWindows()
