import pathlib
p = pathlib.Path("./").glob("*")
files=list(p)
print(f"{p=} --- {files=}")

for i,f in enumerate(files):
    f = str(f)
    print(f"file {i} is: {f} with f variable of type {type(f)}")

