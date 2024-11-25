# This program has a recursive function.

def main():
    # By passing the argument 5 to the message
    # function we are telling it to display the
    # message five times.
    message(10)

def message(times):
    if times > 0:          # This is the control statement.
        print('This is a recursive function.')
        message(times - 1) # This reduces the message down by one each loop.

# Call the main function.
if __name__ == '__main__':
    main()