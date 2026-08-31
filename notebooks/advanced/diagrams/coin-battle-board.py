"""コイン争奪戦の盤面イメージ図を coin-battle-board.png に描き出す。

実際の board.html と同じ配色の盤面に、ルールの注釈を添えたイラスト。
実行: python notebooks/advanced/diagrams/coin-battle-board.py
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 24, 24
CELL = 20
PAD_R = 210          # 右側の注釈スペース
IMG_W = W * CELL + PAD_R
IMG_H = H * CELL

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
font = load_font(15)
small = load_font(11)

# 盤面
draw.rectangle([0, 0, W * CELL, H * CELL], fill="#161b22")
for i in range(W + 1):
    draw.line([(i * CELL, 0), (i * CELL, H * CELL)], fill="#2a2f3a")
    draw.line([(0, i * CELL), (W * CELL, i * CELL)], fill="#2a2f3a")

def coin(x, y):
    draw.ellipse([x * CELL + 4, y * CELL + 4, x * CELL + CELL - 4, y * CELL + CELL - 4],
                 fill="#f1c40f", outline="#b7950b", width=2)

def player(x, y, color, icon, name, label_below=False):
    draw.rounded_rectangle([x * CELL + 1, y * CELL + 1, x * CELL + CELL - 1, y * CELL + CELL - 1],
                           radius=5, fill=color)
    draw.text((x * CELL + CELL / 2, y * CELL + CELL / 2), icon,
              font=small, fill="#ffffff", anchor="mm")
    label_y = y * CELL + CELL + 8 if label_below else y * CELL - 7
    draw.text((x * CELL + CELL / 2, label_y), name,
              font=small, fill="#e6edf3", anchor="mm")

for cx, cy in [(8, 6), (3, 18), (14, 15), (20, 10), (11, 2), (6, 12)]:
    coin(cx, cy)

player(5, 6, "#e74c3c", "太", "太郎")
player(14, 16, "#3498db", "花", "花子", label_below=True)
player(19, 4, "#2ecc71", "b", "bot3")

def arrow(x1, y1, x2, y2, color):
    draw.line([(x1, y1), (x2, y2)], fill=color, width=3)
    draw.polygon([(x2, y2), (x2 - 8, y2 - 5), (x2 - 8, y2 + 5)], fill=color)

# 太郎がコインへ向かう矢印
arrow(6 * CELL + 4, 6 * CELL + CELL / 2, 8 * CELL - 2, 6 * CELL + CELL / 2, "#e6edf3")
# 花子はコインの1マス手前から乗る
arrow(14 * CELL + CELL / 2, 16 * CELL - 2, 14 * CELL + CELL / 2, 15 * CELL + CELL + 2, "#e6edf3")
draw.text((15 * CELL + 6, 15 * CELL - 2), "+1", font=font, fill="#f1c40f")

# 右側の注釈
notes = [
    ("#f1c40f", "コインに乗ると +1点"),
    ("#e6edf3", "上下左右に 1マスずつ"),
    ("#e6edf3", "24×24 マスの盤面"),
    ("#e6edf3", "制限時間内の得点で勝負"),
]
ny = 40
for color, text in notes:
    draw.text((W * CELL + 16, ny), text, font=font, fill=color)
    ny += 34

img.save(__file__.replace(".py", ".png"))
print("coin-battle-board.png を書き出しました")
