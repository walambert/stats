#Mean calculator with variety of input methods.

#Source - Keyboard input
#variables: list that will take arbitrary number of inputted float values
def keyboard_input():
    count = int(input("How many numbers are you inputting?"))
    nums = []
    while n <= count:
        nums.append(float(input("Please enter number: ")))
        n += 1

    mean = sum(nums) / count
    return mean
