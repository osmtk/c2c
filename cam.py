import pygame
import cv2
import numpy as np

def calculate_aspect_ratio_fit(src_width, src_height, max_width, max_height):
    """
    Calculate the width and height to fit an aspect ratio within a bounding box.
    """
    ratio = min(max_width / src_width, max_height / src_height)
    return int(src_width * ratio), int(src_height * ratio)

# Pygameの初期化
pygame.init()

# Webカメラを初期化
cap = cv2.VideoCapture(0)

# Webカメラのフレームサイズを取得
src_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
src_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 初期ウィンドウサイズ
window_width, window_height = 640, 480

# Pygameのディスプレイを設定
screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Webcam Stream")

# メインループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            window_width, window_height = event.w, event.h
            screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

    # フレームをキャプチャ
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # OpenCVのBGRフォーマットをPygameのRGBフォーマットに変換
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # フレームをウィンドウサイズに合わせてリサイズし、アスペクト比を維持
    new_width, new_height = calculate_aspect_ratio_fit(src_width, src_height, window_width, window_height)
    frame = cv2.resize(frame, (new_width, new_height))

    # フレームをPygameのサーフェスに変換
    frame = np.rot90(frame)  # 必要に応じて回転
    frame_surface = pygame.surfarray.make_surface(frame)

    # ウィンドウ全体を黒で塗りつぶす
    screen.fill((0, 0, 0))

    # フレームを中央に配置
    x_offset = (window_width - new_width) // 2
    y_offset = (window_height - new_height) // 2
    screen.blit(frame_surface, (x_offset, y_offset))

    # Pygameディスプレイを更新
    pygame.display.flip()

# リソースの解放
cap.release()
pygame.quit()
