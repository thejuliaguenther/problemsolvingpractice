

def add_nums(num_list, total):
    """
    This function adds a list of numbers
    """
    # base case
    if not num_list:
        return total
    
    # update state
    total += num_list[0]
    
    #recursive call
    return add_nums(num_list[1:], total)