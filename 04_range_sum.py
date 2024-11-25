# This program demonstrates the range_sum function.

def main():
    # Create a list of numbers.
 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #  index   0  1  2  3  4  5  6  7  8
                   
    # Get the sum of the items at indexes 2
    # through 5.
    my_sum = range_sum(numbers, 2, 5)

    # Display the sum.
    print(f'The sum of items 2 through 5 is {my_sum}.')
    
# The range_sum function returns the sum of a specified
# range of items in num_list. The start parameter
# specifies the index of the starting item. The end
# parameter specifies the index of the ending item.
def range_sum(num_list, start, end):
    if start > end: # BASE CASE If start is > end, there are no elements left
                    #  to sum in the range, so the function returns 0
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# Call the main function.
if __name__ == '__main__':
    main()