def input_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Error: This was not a number, give an integer number!")


def input_float(msg: str):
    while True:
        try:
            return float(input(msg))
        except ValueError as e:
            print(f"Error: {e}")
            print("Enter a floating number!")
        except:
            pass


number = input_float("Give me a number: ")
print(f"The user entered the number: {number}")
