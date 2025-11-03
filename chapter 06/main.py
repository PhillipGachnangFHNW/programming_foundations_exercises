
    

def main():
    with open("./names.txt", "r") as file:
        for line in file:
            line = line.rstrip("\n")
            first_name, birth_year = line.split(" ")
            print(f"{first_name} was born in {birth_year}")

if __name__ == "__main__":
    main()