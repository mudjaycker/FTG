import pathlib2
import re
from config import *


path_to = lower_case
path_from = "../FOA_simple_template/"
view_file = path_from + "views/book.py"
schema_file = path_from + "schemas/book.py"
models_path = path_from + "models/book.py"
# ___new files_______________________________|
view_file2 = path_to+"/views/"+lower_case+".py"
schema_file2  = path_to+"/schemas/"+lower_case+".py"
# _______________________________________________|

p = pathlib2.Path(path_to)
p.mkdir(parents=True, exist_ok=True)

view_path = pathlib2.Path(path_to+"/views")
view_path.mkdir(parents=True, exist_ok=True)

schema_path = pathlib2.Path(path_to+"/schemas")
schema_path.mkdir(parents=True, exist_ok=True)



# view creation
with open(view_file, "r") as vi:
    v = vi.read()

v_lower = (re.sub("book", lower_case, v))

with open(view_file2, "w") as vi2:
    vi2.write(v_lower)


with open(view_file2, "r") as vi2:
    v2 = vi2.read()


v2_pascal = (re.sub("Book", PascalCase, v2))

with open(view_file2, "w") as vi3:
    vi3.write(v2_pascal)
# ____________________________________________________

# schema creation
with open(schema_file, "r") as sch:
    sc = sch.read()

sc_pascal = (re.sub("Book", PascalCase, sc))

with open(schema_file2, "w") as sch2:
    sch2.write(sc_pascal)
# _____________________________________________________