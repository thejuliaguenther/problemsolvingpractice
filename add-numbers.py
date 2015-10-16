

def add_nums(num_list, total):
    """
    This function adds a list of numbers
    """
    if not num_list:
        return total
    else:
        total += num_list[0]
        return add_nums(num_list[1:], total)