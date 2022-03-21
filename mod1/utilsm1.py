def num_verify(rangemin = 1, rangemax = 3, msg = ""):

    num = input(msg)

    if num.isnumeric():
        if int(num) <= rangemax:
            if int(num) >= rangemin:
                return int(num)
            else:
                print("ERROR INVALID NUMBER")
                return num_verify(rangemin, rangemax , msg)
        else:
            print("ERROR INVALID NUMBER")
            return num_verify(rangemin, rangemax, msg)
    else:
        print ("ERROR INVALID INPUT")
        return num_verify(rangemin, rangemax, msg)


def verify_str(msg):
    text = input(msg)
    if text.isalpha():
        return text
    else:
        print("ERROR INVALID INPUT")
        return verify_str(msg)


def verify_str_num(msg):
    text = input(msg)
    if text.isalnum():
        return text
    else:
        print("ERROR INVALID INPUT\n")
        return verify_str_num(msg)

def yes_no (msg):
    op = input(msg)

    if op.capitalize() == "Y":
        return True
    elif op.capitalize() == "N":
        return False
    else:
        print("ERROR INVALID INPUT\n")
        return yes_no(msg)
