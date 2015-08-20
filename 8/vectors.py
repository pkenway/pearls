import random


def create_test_array(size):
    """ Generate an array of random numbers between -10 and 10."""
    return [random.randrange(-10, 10, 1) for x in range(0, size)]

def find_largest_subvector_naive(array):
    """ Find the subvector with the highest sum via naive cubic algorithm"""
    max_value = 0
    
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            subvector_sum = sum(array[i:j])
            if subvector_sum > max_value:
                subvector = array[i:j]
                max_value = subvector_sum

    return (subvector, max_value)

def find_largest_subvector_quadratic(array):
    """ Find the subvector with the highest sum via naive cubic algorithm"""
    max_value = 0
    
    for i in range(0, len(array)):
        
        subvector_sum = array[i]
        for j in range(i+1, len(array)):
            if subvector_sum > max_value:
                subvector = array[i:j]
                max_value = subvector_sum
            subvector_sum += array[j]

    return (subvector, max_value)

def find_largest_subvector_divide(array):
    if len(array) == 0:
        return 0
    if len(array) == 1:
        return max(0, array[0])

    middle = int(len(array) / 2)

    lsum = 0
    lmax = 0
    for ele in array[:middle]:
        lsum += ele
        lmax = max(lmax, lsum)
    rsum = 0
    rmax = 0
    for ele in array[middle:]:
        rsum += ele
        rmax = max(rmax, rsum)

    return max(lmax + rmax, find_largest_subvector_divide(array[:middle]), find_largest_subvector_divide(array[middle:]))

if __name__ == '__main__':
    test_array = create_test_array(10)
    print(test_array)
    print(find_largest_subvector_naive(test_array))
    print(find_largest_subvector_quadratic(test_array))
    print(find_largest_subvector_divide(test_array)) 


