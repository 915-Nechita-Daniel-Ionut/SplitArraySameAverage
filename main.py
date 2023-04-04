def get_sum(array):
    """
    Function used for obtaining the sum of an array
    :param array: Array of elements
    :return: The sum of elements
    """

    sum = 0
    for index in range(len(array)):
        sum += array[index]

    return sum


def is_possible(sum, partial_length, length):
    """
    :param sum: Sum of the elements in the array
    :param partial_length: Half of the length of the array
    :param length: The length of the array
    :return: True if it is possible or False otherwise

    Starting from the fact that 2 subarrays need to have the same average means that: sum(a)/len(a) = sum(b)/len(b) = sum/length
    This results in sum(a)= (len(a)*sum) / length and we check here if it is possible to split the array
    """
    possible = False

    for index in range(1, partial_length + 1):
        if sum * index % length == 0:
            possible = True

    return possible


def split_array_with_same_average(array):
    length = len(array)     #length of the array
    partial_len = int(length/2)
    sum = get_sum(array)    #sum of the array
    if not is_possible(sum, partial_len, length):
        return False

    matrix = [set() for _ in range(partial_len+1)]  #actually this is an array of sets

    matrix[0].add(0)    #we initialize the first element with 0


    #Using dynamic programming we make combinations of elements into sums and add them to the sets
    for elem in array:
        for index in range(partial_len, 0, -1):
            for set_element in matrix[index-1]:
                matrix[index].add(set_element + elem)


    #Here we check if the is a sum in every set that satisfies the condition
    for index in range(1, partial_len + 1):
        if sum * index % length == 0:
            partial_sum = int(sum * index / length)
            if partial_sum in matrix[index]:
                return True

    return False






if __name__ == '__main__':
    array=[2, 4, 5, 7, 10, 14]
    if split_array_with_same_average(a) is True:
        print('IS TRUEEE')
    else:
        print('not true...')
