import json

paths = [
    r"/Users/yusuke/programs/pythoncorse1/notebooks/intro_to_programming/functions.ipynb",
    r"/Users/yusuke/programs/pythoncorse1/notebooks/intro_to_programming/exercise-functions.ipynb"
]

for path in paths:
    print("====================")
    print(path)
    print("====================")
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
        for i, cell in enumerate(nb["cells"]):
            if cell["cell_type"] == "markdown":
                src = "".join(cell["source"])
                print(f"--- Cell {i} ---")
                print(repr(src))
