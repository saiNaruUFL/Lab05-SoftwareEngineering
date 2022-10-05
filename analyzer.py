import stringdata
import time

# Linear Search for element in container
def linear_search(container, element):
    for index, string in enumerate(container):
        if string == element:
            return index
    return -1

# Binary search for element in container
def binary_search(container, element):
    lower = 0
    upper = len(container)-1

    # split the data in half each iteration
    # decreasing the amount of data that needs to be iterated over
    while lower <= upper:
        mid = (upper + lower) // 2
        if container[mid] < element:
            lower = mid + 1
        elif container[mid] > element:
            upper = mid - 1
        else:
            return mid
    return -1

# times any function
# returns the result of the function being timed
# and the elapsed time of the functipn's execution
def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    elapsed = end-start
    return result, elapsed

def main():
    # Get the string data
    string_data = stringdata.get_data()

    # Strings to search for
    to_find = ["not_here", "mzzzz", "aaaaa"]
    
    # For each string in to_find
    # time the linear and binary search and print out the values
    # and times returned
    for search in to_find:
        linear_index, linear_time = time_function(linear_search, string_data, search)
        binary_index, binary_time = time_function(binary_search, string_data, search)
        print("Finding %s ..." % search)
        print("Linear Index: %d" % linear_index)
        print("Linear Time: %f seconds" % linear_time)
        print("Binary Index: %d" % binary_index)
        print("Binary Time: %f seconds\n" % binary_time)

if __name__ == "__main__":
    main()
