import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def analyze_image_golden_ratio(image_path):
    # 画像を読み込む
    img = Image.open(image_path)
    img_array = np.array(img)

    # 画像の幅と高さを取得
    height, width = img_array.shape[:2]

    # 黄金比（φ）を計算
    phi = (1 + np.sqrt(5)) / 2

    # 黄金比に基づいて画像を分割
    golden_width = int(width / phi)
    golden_height = int(height / phi)

    # 結果を表示するためのfigureを作成
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

    # 元の画像を表示
    ax1.imshow(img_array)
    ax1.set_title("Original Image")
    ax1.axis('off')

    # 黄金比の線を引く
    ax2.imshow(img_array)
    ax2.axvline(x=golden_width, color='r', linestyle='--')
    ax2.axvline(x=width - golden_width, color='r', linestyle='--')
    ax2.axhline(y=golden_height, color='r', linestyle='--')
    ax2.axhline(y=height - golden_height, color='r', linestyle='--')
    ax2.set_title("Image with Golden Ratio Lines")
    ax2.axis('off')

    plt.tight_layout()
    plt.show()

    # 画像の主要部分が黄金比の線に沿っているかを簡単に分析
    print("画像分析結果:")
    print(f"画像サイズ: {width}x{height}")
    print(f"黄金比による分割位置: 縦={golden_height}, 横={golden_width}")
    print("注意: 主要な被写体や構図の要素がこれらの線に近いほど、")
    print("黄金比に基づいた構図である可能性が高くなります。")

if __name__ == "__main__":
    # サンプル画像のパスを指定（ユーザーの環境に合わせて変更してください）
    image_path = "path/to/your/image.jpg"
    analyze_image_golden_ratio(image_path)
