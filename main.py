while True:
    try:
        x = int(input("What is X? "))
        
    except ValueError:
        print("X is not STR ")
    except NameError:
        print("Y is not defined")
    else:
        print(y)
        print(f"X is {x}")        