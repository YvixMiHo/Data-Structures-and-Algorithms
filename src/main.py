# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#               TL i PL HL
#    # oo #     4  0 3  1
#   ## oo ##    6  1 2  2
#  ### oo ###   8  2 1  3
# #### oo ####  10 3 0  4

#TL: (len of input string we choose to be the center) = 2 + 2 * max(i)
#i: index = i
#PL: padding length = (-1) * i + max(i)
#HL: hash length = i + 1

class NegativeNumberError(Exception):
    pass

class OverboundNumberError(Exception):
    pass

def get_user_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))

            match user_input:
                case user_input if user_input > 8:
                    raise OverboundNumberError("Error value greater than 8: please enter value in range of 1 - 8")
                case user_input if user_input <= 0:
                    raise NegativeNumberError("Error negative or 0 value: please enter value in range of 1 - 8")
                case _:
                    return user_input

        except OverboundNumberError as e:
            print(e)
        except NegativeNumberError as e:
            print(e)
        except ValueError:
            print(f'Please enter a valid integer')

def pyramid_centered(val,max_n):
    max_i = max_n
    total_len = 2*max_i + 2

    for i in range(0,max_i):
        pad_left = (-1)*i + max_i
        hash_length = (i+1)
        row = (' ') * (pad_left) + ('#')*hash_length + val + ('#')*hash_length
        print(row)

if __name__ == '__main__':

    n = get_user_input('Enter pyramid depth')
    val = '00'
    pyramid_centered(val,n)

    # for i in range(0,max_i):
    #     pad_left = (-1)*i + max_i
    #     hash_length = (i+1)
    #     row = (' ') * (pad_left) + ('#')*hash_length + 'oo' + ('#')*hash_length
    #     print(row)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
