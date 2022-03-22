def num_verify(rangemin = 1, rangemax = 3, msg = ""):

    '''Number Verification'''

    num = input(msg)

    if num.isnumeric():
        if int(num) <= rangemax:
            if int(num) >= rangemin:
                return int(num)
            else:
                print("ERROR INVALID NUMBER\n")
                return num_verify(rangemin, rangemax , msg)
        else:
            print("ERROR INVALID NUMBER\n")
            return num_verify(rangemin, rangemax, msg)
    else:
        print ("ERROR INVALID INPU\nT")
        return num_verify(rangemin, rangemax, msg)


def verify_str(msg):
    '''String verification'''
    text = input(msg)
    if text.isalpha():
        return text
    else:
        print("ERROR INVALID INPUT\n")
        return verify_str(msg)


def verify_str_num(rangemax, msg):
    '''Verifier for alphanumeric string'''
    text = input(msg)
    if text.isalnum():

        if rangemax != 0:
            if len(text) == rangemax:
                return text
            
            else:

                print ("ERROR INVALID INPUT\n\n")
                return verify_str_num (rangemax, msg)
        else:

            return text
        
    else:

        print("ERROR INVALID INPUT\n")
        return verify_str_num(msg)



def yes_no (msg):
    '''Y/N input verifier'''
    op = input(msg)

    if op.capitalize() == "Y":
        return True
    elif op.capitalize() == "N":
        return False
    else:
        print("ERROR INVALID INPUT\n")
        return yes_no(msg)
