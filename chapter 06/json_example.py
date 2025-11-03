import json
import pathlib

def input_bool(msg: str) -> bool:
    while True:
        anwser = input(msg)
        if anwser.lower() in ["y", "yes"]:
            return True
        elif anwser.lower() in ["n", "no"]:
            return False
        else:
            print("Error: Enter 'y' or 'n'")

def input_int(msg: str) -> int:
    while True:
        try:
            number = int(input(msg))
        except ValueError as err:
            print(f"Error: {err}")
            print("Enter an integer number.")
        else:
            return number


def create_new_record(name, year) -> dict:
    return {
        "name": name,
        "year": year
    }


def display_record(record):
    print(record["name"], record["year"])


def main():
    file_path = pathlib.Path("./data/records.json")
    if not file_path.exists():
        with open(file_path, "w") as file:
            data = []
            json.dump(data, file)
    with open(file_path, "r") as file:
        data: list = json.load(file)
        for record in data:
            display_record(record)

    new_record = input("Do you wish to create a new record? (y/n)")
    while new_record == 'y':
        name = input("What's the name? ")
        year = input_int("What's the year? ")
        new = create_new_record(name, year)
        data.append(new)
        new_record = input("Do you wish to create a new record? ")

    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    main()
