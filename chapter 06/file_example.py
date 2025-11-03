import pathlib

file_path = pathlib.Path("./data/abc.txt")
if not file_path.parent.exists():
    file_path.parent.mkdir(parents=True, exist_ok=True)
with open(file_path, "a") as file:
    data = 1
    file.write(f"{data}\n")

with open(file_path, "r") as file:
    sum = 0
    for line in file:
        number = int(line.rstrip("\n"))
        sum += number

print(f"Sum is: {sum}")