# Get “1” to print when passed a 1
# Get “2” to print when passed a 2
# Get “Soda” to print when passed a 3
# Get “Pop” to print when passed a 5

# Modify code for steps 3/4 so that your code can do this:
    # Get “Soda” when passed a 6 (a multiple of 3)
    # Get “Pop” when passed a 10 (a multiple of 5)
    # Get “SodaPop” when passed a 15 (a multiple of 3 and 5)

def kata(value):
    if (value == 1):
        print("1")
    elif (value == 2):
        print("2")
    elif (value % 5 == 0) and (value % 3 == 0):
        print("SodaPop")
    elif (value % 3 == 0):
        print("Soda")
    elif (value % 5 == 0):
        print("Pop")
    else:
        raise Exception("Input has no return.")