"""部品1の説明用に、マンハッタン距離のイラストを coin-battle-distance.png に描き出す。

実行: python notebooks/advanced/diagrams/coin-battle-distance.py
"""
from PIL import Image, ImageDraw, ImageFont

N = 12
CELL = 32
PAD_B = 44
IMG_W = N * CELL
IMG_H = N * CELL + PAD_B

def load_font(size):
    candidates = [
        "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
        "/System/Library/Fonts/Hiragino Sans GB.ttc",
        "/Library/Fonts/Arial Unicode.ttf",
        "C:/Windows/Fonts/meiryo.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()

img = Image.new("RGB", (IMG_W, IMG_H), "#0d1117")
draw = ImageDraw.Draw(img)
font = load_font(16)

draw.rectangle([0, 0, N * CELL, N * CELL], fill="#161b22")
for i in range(N + 1):
    draw.line([(i * CELL, 0), (i * CELL, N * CELL)], fill="#2a2f3a")
    draw.line([(0, i * CELL), (N * CELL, i * CELL)], fill="#2a2f3a")

def center(x, y):
    return (x * CELL + CELL / 2, y * CELL + CELL / 2)

px, py = 3, 8      # 自分
cx, cy = 8, 3      # コイン

# 自分: 赤い角丸四角
draw.rounded_rectangle([px * CELL + 2, py * CELL + 2, px * CELL + CELL - 2, py * CELL + CELL - 2],
                       radius=6, fill="#e74c3c")
draw.text(center(px, py), "自", font=load_font(15), fill="#ffffff", anchor="mm")
# コイン: 金の丸
draw.ellipse([cx * CELL + 6, cy * CELL + 6, cx * CELL + CELL - 6, cy * CELL + CELL - 6],
             fill="#f1c40f", outline="#b7950b", width=2)

# 経路: 横に5マス、縦に5マス
mid = (center(cx, py)[0], center(px, py)[1])
draw.line([center(px, py), mid], fill="#e6edf3", width=3)
draw.line([mid, center(cx, cy)], fill="#e6edf3", width=3)
tip = center(cx, cy)
draw.polygon([(tip[0], tip[1] + 14), (tip[0] - 6, tip[1] + 24), (tip[0] + 6, tip[1] + 24)], fill="#e6edf3")

draw.text((center(5.5, py)[0], py * CELL + CELL + 8), "x差 = 5", font=font, fill="#e6edf3", anchor="mm")
draw.text((cx * CELL + CELL + 8, center(cx, 5.5)[1]), "y差 = 5", font=font, fill="#e6edf3", anchor="lm")
draw.text((IMG_W / 2, N * CELL + PAD_B / 2), "距離 = abs(x差) + abs(y差) = 5 + 5 = 10", font=font,
          fill="#f1c40f", anchor="mm")

img.save(__file__.replace(".py", ".png"))
print("coin-battle-distance.png を書き出しました")
