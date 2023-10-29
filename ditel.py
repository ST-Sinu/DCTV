import djitellopy as tello
import cv2
from groundingdino.util.inference import load_model, load_image, predict, annotate
import numpy as np
from PIL import Image
import groundingdino.datasets.transforms as T
import matplotlib.pyplot as plt
import winsound as sd

model = load_model("C:/Users/user/anaconda3/envs/test/GroundingDINO/groundingdino/config/GroundingDINO_SwinT_OGC.py", "C:/Users/user/anaconda3/envs/test/GroundingDINO/weights/groundingdino_swint_ogc.pth")
#모델경로 2개

def inference(img, prompt, box_threshold=0.35, text_threshold=0.25):
    transform = T.Compose([
        T.RandomResize([800], max_size=1333),
        T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

    image_transformed, _ = transform(Image.fromarray(img), None)

    boxes, logits, phrases = predict(
        model=model,
        image=image_transformed,
        caption=prompt,
        ##prompt가 찾고싶은 객체
        box_threshold=box_threshold,
        text_threshold=text_threshold
    )

    annotated_frame = annotate(image_source=img, boxes=boxes, logits=logits, phrases=phrases)

    for index in range(len(phrases)):
        if 'a knife' in phrases[index] and int(logits[index] >= 0.5) :
            sd.Beep(1000, 500)  # 1000Hz 소리를 0.5초 동안 재생


    return annotated_frame

def dino(drone_img):
    img = drone_img
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (1280, 720))

    result_img1 = inference(img, TEXT_PROMPT)
    result_img = np.array(result_img1)
    result_img = result_img[:,:,::-1]

    return result_img

TEXT_PROMPT = "a knife , an unmbrella, a cup, a smart phone, his or her hand, a straw, a pipe, a pen,a bag, a person"

def dino_quit():
    quit()

# drone = tello.Tello()
# drone.connect()
# print(drone.get_battery())

# drone.streamon()

# while True:
#     img = drone.get_frame_read().frame
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (1280, 720))

#     result_img1 = inference(img, TEXT_PROMPT)
#     result_img = np.array(result_img1)
#     result_img = result_img[:,:,::-1]

#     cv2.imshow('result_img',result_img)

#     key = cv2.waitKey(1)
#     if key == 27:
#         quit()
