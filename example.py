def menu(items):
    is_valid = False
    while not is_valid:
        for i, item in enumerate(items):
            print(f"{i+1}. {item}")
        choice = input(f"Enter what you want to do (1-{len(items)}):")
        try:
            choice = int(choice)
            if 1 <= choice <= len(items):
                is_valid = True
            else:
                print(f"Invalid input, please give a number between 1-{len(items)}")
                
        except:
            print(f"Invalid input, please give a number between 1-{len(items)}")
    return choice

def is_valid_prio(prio):
    if prio.lower() in ["high", "medium", "low"]:
        return True
    else:
        return False

def add_task():
    is_valid = False
    while not is_valid:
        name = input("What is the tasks name.")


print(is_valid_prio("nothing"))
