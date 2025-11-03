def input_name():
    name = input("Whats the first name? ")
    while name == "":
        print("Error: Enter a name!")
        name = input("Whats the first name? ")
    return name

def input_year():
    year = input("Whats the birth year? ")
    while year == "":
        print("Error: Enter a year")
        year = input("Whats the birth year? ")
    return int(year)

def print_record(name, year):
    print(f"Name: {name}, Year: {year}")

def main():
    file_path = "./data/names.txt"
    print("Welcome to the birth records!")
    new_records = input("Do you like to create a new record? ")
    while new_records == "":
        print("Error: Enter y or n")
        new_records = input("Do you like to create a new record? ")

    while new_records == "y":
        name = input_name()
        year = input_year()
        with open(file_path, "a") as file:
            file.write(f"{name} {year}\n")
        new_records = input("Do you wish to add an other? ")
    with open(file_path, "r") as file:
        for line in file:
            name, year = line.rstrip("\n").split(" ")
            print_record(name, year)

if __name__ == "__main__":
    main()
        
    