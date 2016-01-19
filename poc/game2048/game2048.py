from poc_test import poc_simpletest

# Functions to perform merge in 2048 game

def merge(list_to_merge):
    """ 1. Make a copy of the list
        2. Move any zeroes in the list to the end
        3. If adjacent numbers are the same (2 and 2), then merge them (2+2)
           or if they are different evaluate the next two numbers in the list.
        4. Fill the list to zeroes after merge to make it the same length as
           the original list.
    """
    merged_list_copy = list_to_merge[::]
    merged_list = move_zeroes_to_end(merged_list_copy)
    working_list = []

    for idx, num in enumerate(merged_list):
        if idx==len(merged_list)-1 and num:
            working_list.append(merged_list[idx])
        elif num == 0:
            pass
        elif merged_list[idx] == merged_list[idx+1]:
            working_list.append(merged_list[idx]*2)
            merged_list[idx+1] = 0
        else:
            working_list.append(merged_list[idx])

    return fill_with_zeroes(working_list, len(list_to_merge))

def move_zeroes_to_end(line):
    """
    If there are zeroes in the list, move them to the end
    """
    new_line = [ 0 for val in line ]

    strip_zeroes = [ val for val in line if val > 0]

    for idx, val in enumerate(strip_zeroes):
        new_line[idx] = strip_zeroes[idx]

    return new_line

def fill_with_zeroes(list_to_fill, list_size):
    """
    Fill the list with zeroes to the list_size
    """

    list_of_zeroes = [0]*list_size

    for idx, item in enumerate(list_to_fill):
        list_of_zeroes[idx] = list_to_fill[idx]

    return list_of_zeroes


def run_suite(test_function):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs
    suite.run_test( test_function([2, 0, 2, 2]), [4, 2, 0, 0], "Test #1:")
    suite.run_test( test_function([8, 16, 16, 8]), [8, 32, 8, 0], "Test #2:")
    suite.run_test( test_function([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0], "Test #3:")

    suite.report_results()


if __name__ == '__main__':
    run_suite(merge)
