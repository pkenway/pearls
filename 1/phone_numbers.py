import array
import random
import time
# Problem: sort an list of unique integers with a set maximum
# Solution: use a bit array and flag the corresponding bit for each number.
# this takes up extra space, but we can sort in O(n) time

class CodeTimer:
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        self.clock_start = time.clock()

    def __exit__(self, type, value, traceback):
        print ('%s - %s' % (self.tag, str(time.clock() - self.clock_start)))


def makeBitArray(bitSize):
    """Generate an array of bits initialized to 0.

    Bits will be stored as 32-bit unsigned ints"""
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

def testBit(bit_array, bit_num):
    """Retrieve the value at the given position."""
    record = bit_num >> 5
    offset = bit_num & 31
    mask = 1 << offset
    return bit_array[record] & mask
   

def setBit(bit_array, bit_num, is_selected):
    """Set the value at the given position."""
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
    """Initialize a bit array and mark each number in the numbers list."""
    bit_array = makeBitArray(maxNum)
    for num in numbers:
        setBit(bit_array, num, True)

    return bit_array

def get_all_numbers(bit_array, maxNum):
    """Get all selected numbers for a bit array."""
    return [i for i in range(0, maxNum) if testBit(bit_array, i)]

def print_all_numbers(bit_array, maxNum):
    for i in range(0, maxNum):
        if testBit(bit_array, i):
            print(i)

def generate_unique_number_array(k, n):
    """ Generate k unique random integers with a max value of n."""
    # start with the first K integers selected
    random_numbers = makeBitArray(n)
    for i in range(0, k):
        setBit(random_numbers, i, True)
        
    for i in range(0, k):
        #exchange the current value with a value further in the array
        new_index = random.randrange(i+1, n, 1)

        # need a temp val here
        temp_bit = testBit(random_numbers, new_index)
        setBit(random_numbers, new_index, testBit(random_numbers, i))
        setBit(random_numbers, i, temp_bit)

    # now we have random numbers but they are ordered
    # first condense into an actual list of numbers
    number_list = [i for i in range(0, n) if testBit(random_numbers,i)]

    # now shuffle the numbers
    for i in range(0, k - 1):
        dest = random.randrange(i+1, k,1)
        number_list[i], number_list[dest] = number_list[dest], number_list[i]

    return number_list

if __name__ == '__main__':

    # timing it out, the algo didn't seem to shine 
    # over system sort until the numbers got this big
    k = 1000000
    n = 10000000

    with CodeTimer('generating random numbers'):
        rands = generate_unique_number_array(k, n)

    #compare performance to sort
    with CodeTimer('builtin sort'):
        sorted_numbers = sorted(rands)

    with CodeTimer('bitmap sort'):
        sorted_numbers = enter_numbers(rands, n)

