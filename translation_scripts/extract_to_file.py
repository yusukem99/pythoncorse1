import json

paths = [
    r"/Users/yusuke/programs/pythoncorse1/notebooks/intro_to_programming/functions.ipynb",
    r"/Users/yusuke/programs/pythoncorse1/notebooks/intro_to_programming/exercise-functions.ipynb"
]

with open("/Users/yusuke/programs/pythoncorse1/extracted_markdown.txt", "w", encoding="utf-8") as out:
    for path in paths:
        out.write("====================\n")
        out.write(path + "\n")
        out.write("====================\n")
        with open(path, "r", encoding="utf-8") as f:
            nb = json.load(f)
            for i, cell in enumerate(nb["cells"]):
                if cell["cell_type"] == "markdown":
                    src = "".join(cell["source"])
                    out.write(f"--- Cell {i} ---\n")
                    out.write(repr(src) + "\n")
