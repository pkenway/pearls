
import math

def binary_search(element, array):
    print('test count should be %d' % math.log(len(array),2))
    test_count = 0
    lower = 0
    upper = len(array)-1

    while lower <= upper:
        middle =  round((lower + upper) / 2)
        test_count += 1
        if array[middle] == element:
            print('tests: %d' % test_count)
            return middle

        if array[middle] < element:
            lower = middle + 1
        else:
            upper = middle - 1
        
    print('tests: %d' % test_count)
    return None

def binary_search_recursive(element, array, lower=0, upper=None):
    if upper == None:
        upper = len(array) -1

    if lower > upper:
        return None
    middle = round((lower + upper) / 2)
    if array[middle] == element:
        return middle
    if array[middle] < element:
        return binary_search_recursive(element, array, middle + 1, upper)
    else:
        return binary_search_recursive(element, array, lower, middle - 1)



if __name__ == '__main__':
    array = list(range(0,1000))
    print(binary_search(432, array))