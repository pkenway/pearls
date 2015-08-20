import array
import random
import time

# Problem: sort an list of unique integers with a set maximum
# Solution: use a bit array and flag the corresponding bit for each number.
# this takes up extra space, but we can sort in O(n) time


# need a way to make an array of arbitrary size to store bit flags
#can't really make a boolean array in python, so use 32 bit integers
def makeBitArray(bitSize):
    num_ints = bitSize  >> 5

    # will evaluate to true if the number of bits is not
    # evenly divisible by 32 
    if bitSize & 31:
        # add another int for the overflow bits
        num_ints += 1 

    # make an array of unsigned ints
    bit_array = array.array('I')

    # initialize the array with 0s
    bit_array.extend((0,) * num_ints)
    return bit_array

# get the bit at the given position
def testBit(bit_array, bit_num):
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    try:
        return bit_array[record] & mask
    except:
        print('error')
        print(len(bit_array))
        print(bit_num)
        print(record)
        print(offset)
        raise

def setBit(bit_array, bit_num, is_selected):
    record = bit_num >> 5
    offset = bit_num & 31
    if is_selected:
        #to toggle on 
        mask = 1 << offset
        bit_array[record] |=  mask
    else:
        mask =  ~(1 << offset)
        bit_array[record] &=  mask


def enter_numbers(numbers, maxNum):
    # create a bit array with each number flagged
    bit_array = makeBitArray(maxNum)
    for num in numbers:
        setBit(bit_array, num, True)

    return bit_array

def get_all_numbers(bit_array, maxNum):
    return [i for i in range(0, maxNum) if testBit(bit_array, i)]

def print_all_numbers(bit_array, maxNum):
    for i in range(0, maxNum):
        if testBit(bit_array, i):
            print(i)

def generate_unique_number_array(k, n):
    """ Generate k unique random integers with a max value of n."""
    # start with the first K integers selected
    random_numbers = ([True,] * k)

    # add slots for the rest
    random_numbers.extend([False,] * (n - k))

    # 
    for i in range(0, k):
        #exchange the current value with a value further in the array
        new_index = random.randrange(i+1, n, 1)
        temp_val = random_numbers[new_index]
        random_numbers[new_index] = random_numbers[i]
        random_numbers[i] = temp_val

    # now we have random numbers but they are ordered
    # first condense into an actual list of numbers
    number_list = [i for i in range(0, n) if random_numbers[i]]

    # now shuffle the numbers
    for i in range(0, k - 1):
        dest = random.randrange(i+1, k,1)
        temp_val = number_list[i]
        number_list[i] = number_list[dest]
        number_list[dest] = temp_val

    return number_list

if __name__ == '__main__':

    # timing it out, the algo didn't seem to shine 
    # over system sort until the numbers got this big
    k = 10000000
    n = 100000000

    print('generating...')
    rands = generate_unique_number_array(k, n)
    print('done')
    #compare performance to sort
    sort_start =  (time.clock())
    sorted_numbers = sorted(rands)
    print('built-in sort: %s' % str(time.clock() - sort_start))

    sort_start = time.clock()

    sorted_numbers = enter_numbers(rands, n)
    print('my sort: %s' % str(time.clock() - sort_start))
