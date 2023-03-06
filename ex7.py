#################################################################
# FILE : ex7.py
# WRITER : Yuval Shaffir , yuval.shaffir , 208448068
# EXERCISE : ex7
# DESCRIPTION: Recursive functions and the hanoi tower game.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none.
# NOTES:
#################################################################


def print_to_n(n, number=1):
    """The function receives a number and prints the numbers
    from 1 until that number."""
    if number <= n and n >= 1:
        print(number)
        return print_to_n(n, number + 1)
    return


def digit_sum(n):
    """The function receives a number and prints the sum
    of it's digits."""
    if n > 0:
        return n % 10 + digit_sum(n//10)
    return 0


def is_prime(n):
    """The function receives a number and returns true if it is a prime
    number, false if it isn't a prime number"""
    if n > 1:
        if not has_divisor_smaller_than(n, n):
            return True
        return False


def has_divisor_smaller_than(n, i):
    """checks if the number n has a divider that is smaller than
    i and isn't 1."""
    divider = i - 1
    if divider > 1 and n >= i:
        if n % divider == 0:
            return True
        elif has_divisor_smaller_than(n, i-1):
            return True
    return False


def play_hanoi(hanoi, n, src, dst, temp):
    """The function solves the Hanoi towers game"""
    if n < 0:
        n = 0
    if n == 1:  # base case
        hanoi.move(src, dst)  # move a disk to the destination
    else:
        play_hanoi(hanoi, n-1, src, temp, dst)  # move a smaller stack of disks to the temp
        play_hanoi(hanoi, 1, src, dst, temp)  # move the remaining disk to the destination
        play_hanoi(hanoi, n-1, temp, dst, src)  # more the same smaller stack from the temp to the destination


def print_sequences(char_list, n, string=""):
    """The function prints all the possible characters combinations of length n"""
    if n <= 0:
        print("")
        return
    if n == 1:  # base case
        for char in char_list:
            comb = string + char
            print(comb)
    else:
        for main_char in char_list:
            string += main_char
            print_sequences(char_list, n-1, string)
            string = string[:-1]


def string_from_one_char_only(string, checked_char):
    """The function checks if the string is built from one character,
    if it is than it will return True, else False."""
    count = 0
    for char in string:
        if char == checked_char:
            count += 1
        else:
            return False
    if len(string) == count and count >= 1:
        return True
    else:
        return False


def print_no_repetition_sequences(char_list, n, string=""):
    """The function prints all different character's combinations."""
    if n <= 0:
        print("")
        return
    if n == 1:  # base case
        for char in char_list:
            if not string_from_one_char_only(string, char):
                comb = string + char
                print(comb)
    else:
        for main_char in char_list:
            string += main_char
            print_no_repetition_sequences(char_list, n-1, string)
            string = string[:-1]  # after the function finishes, the string will reduce it's size by 1.
            # so new characters can be added to the string without crossing the length n.


def parentheses(n):
    """The function gets a number 'n' and returns the combinations of the parenthesis that open
     and close 'n' times each."""
    if n > 0:
        comb = ""
        parenthesis_lst = []
        parenthesis_helper(n, 0, 0, comb, parenthesis_lst)
    else:
        return [""]
    return parenthesis_lst


def parenthesis_helper(n, left_par, right_par, comb, parenthesis_lst):
    """Recursive function that gets number of opening and closing parenthesis, calculates their possible
    combinations and add them to a list"""
    if len(comb) == 2*n:
        parenthesis_lst.append(comb)
        return
    if left_par < n:
        parenthesis_helper(n, left_par+1, right_par, comb + "(", parenthesis_lst)
    if left_par > right_par:
        parenthesis_helper(n, left_par, right_par+1, comb + ")", parenthesis_lst)


def flood_fill(image, start):
    """The function gets an image of a 2D list containing '.' or '*', and a tuple starting point,
     then it sends the image and starting point to the recursive utility function."""
    row = start[0]
    col = start[1]
    flood_fill_helper(image, row, col)


def flood_fill_helper(image, row, col):
    """The recursive function gets an image of a 2D list containing '.' and '*', then it fills the '.' cells with
         '*' in the condition that they are reachable by other '.' cells."""
    if image[row][col] == ".":
        image[row][col] = "*"
    if image[row - 1][col] == ".":
        if not flood_fill_helper(image, row-1, col):  # will return to the previous cell
            flood_fill_helper(image, row, col)
    elif image[row + 1][col] == ".":
        if not flood_fill_helper(image, row+1, col):  # will return to the previous cell
            flood_fill_helper(image, row, col)
    elif image[row][col + 1] == ".":
        if not flood_fill_helper(image, row, col+1):  # will return to the previous cell
            flood_fill_helper(image, row, col)
    elif image[row][col - 1] == ".":
        if not flood_fill_helper(image, row, col-1):  # will return to the previous cell
            flood_fill_helper(image, row, col)
    else:
        return False


