# A recursive function is a function that calls itself.
# This program has a recursive function named message

def main():
    message()    # function variable message

def message():   # Calling itself but without any parameters.
    print('This is a recursive function.')
    message()

# Call the main function.
if __name__ == '__main__':
    main()

# This program calls itself again and again and again....
# Recursive functions are like loops it needs a control mechanism.