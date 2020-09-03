#Mean calculator with variety of input methods.

#Source - Keyboard input
#variables: list that will take arbitrary number of inputted float values
def keyboard_input(nums = [], total):
    total = int(input("How many numbers are you inputting?"))

    while n <= total:
        nums.append(float(input("Please enter number: ")))
        n += 1
        
