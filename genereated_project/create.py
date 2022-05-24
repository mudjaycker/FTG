import pathlib2
import re
from config import *


path_to = lower_case
path_from = "../FOA_simple_template/"
views_path = path_from + "views/book.py"
schemas_path = path_from + "schemas/book.py"
models_path = path_from + "models/book.py"

p = pathlib2.Path(path_to)
p.mkdir(parents=True, exist_ok=True)

# view creation
with open(views_path, "r") as vi:
    v = vi.read()

print(v)