from deque import Deque
def is_palindrome(string):
    """
    This function checks to see if a string is a palindrome
    """

    chars = Deque()

    #The implementation of deque here assumes that the front of the underliying list is the end of the deque
    for char in string: 
        chars.addRear(char)

    while chars.size() >=3:
        front_char = chars.removeRear()
        back_char = chars.removeFront()
        if front_char != back_char:
            print False
            return

    print True

is_palindrome("Julia")
is_palindrome("racecar")



