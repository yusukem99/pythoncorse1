"""ノートブック内の Mermaid 図を画像に変換して埋め込む。

マークダウンセルにある、alt テキストが .mmd ファイルのパスになっている画像行

    ![notebooks/advanced/diagrams/webrtc-signaling.mmd](...)

を見つけ、その .mmd ファイルを画像に変換して data URI で差し替える。
パスはリポジトリのルートからの相対パス。新しく図を置くときは
括弧の中を空にした行 ![diagrams/xxx.mmd]() を書いてから、このツールを実行する。

使い方:
    python tools/render_mermaid.py notebooks/advanced/network-programming.ipynb
"""
import base64
import json
import re
import sys

import requests

IMAGE = re.compile(r"!\[([^\]]+\.mmd)\]\([^)]*\)")


def render_png(source):
    """mermaid.ink で Mermaid ソースを PNG にする"""
    encoded = base64.urlsafe_b64encode(source.encode()).decode()
    url = "https://mermaid.ink/img/" + encoded + "?type=png&bgColor=ffffff"
    res = requests.get(url, timeout=60)
    res.raise_for_status()
    return res.content


def replace_image(match):
    mmd_path = match.group(1)
    with open(mmd_path, encoding="utf-8") as f:
        source = f.read()
    png = render_png(source)
    png_b64 = base64.b64encode(png).decode()
    print("  ", mmd_path, "->", len(png), "bytes")
    return "![{}](data:image/png;base64,{})".format(mmd_path, png_b64)


def main(paths):
    for path in paths:
        with open(path, encoding="utf-8") as f:
            nb = json.load(f)
        print(path)
        count = 0
        for cell in nb["cells"]:
            if cell["cell_type"] != "markdown":
                continue
            text = "".join(cell["source"])
            new_text, n = IMAGE.subn(replace_image, text)
            if n:
                cell["source"] = new_text.splitlines(keepends=True)
                count += n
        with open(path, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print("  ", count, "枚の図を更新")


if __name__ == "__main__":
    main(sys.argv[1:])
