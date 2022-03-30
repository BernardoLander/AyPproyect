
def verify_str_indb(list, msg):

    '''String verification'''
    
    pretty = "\n ==>"
    text = input(msg + pretty)
    
    if text.replace(" ","").isalpha():
    
        for i in range(len(list)):
            if text == list[i]:
                return text

    else:
    
        print("ERROR INVALID INPUT\n")
    
        return verify_str_indb(list, msg)




def num_verify_range(rangemin = 1, rangemax = 3, msg = ""):

    '''Number Verification'''

    pretty = "\n ==>"
    num = input(msg + pretty)

    if num.isnumeric():
        if int(num) <= rangemax:
            if int(num) >= rangemin:
                return int(num)
            else:
                print("ERROR INVALID NUMBER\n")
                return num_verify_range(rangemin, rangemax , msg)
        else:
            print("ERROR INVALID NUMBER\n")
            return num_verify_range(rangemin, rangemax, msg)
    else:
        print ("ERROR INVALID INPU\nT")
        return num_verify_range(rangemin, rangemax, msg)



def num_verify (msg):

    pretty = "\n ==>"
    num = input(msg + pretty)

    if num.isnumeric():
        
        return int(num)

    else:
        print ("ERROR INVALID INPU\nT")
        return num_verify(msg)



def verify_str(msg):

    '''String verification'''
    
    pretty = "\n ==>"
    text = input(msg + pretty)
    
    if text.replace(" ","").isalpha():
    
        return text
    
    else:
    
        print("ERROR INVALID INPUT\n")
    
        return verify_str(msg)



def verify_str_num(rangemax, msg):
    '''Verifier for alphanumeric string'''

    pretty = "\n ==>"
    text = input(msg + pretty)

    if text.isalnum():

        if rangemax != 0:
            if len(text) == rangemax:
                return text.capitalize()
            
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
    pretty = "\n Y/N ==>"
    op = input(msg + pretty)

    if op.capitalize() == "Y":
        return True
    elif op.capitalize() == "N":
        return False
    else:
        print("ERROR INVALID INPUT\n")
        return yes_no(msg)



def get_list_cute(list):
    '''arrange lists in a cute way'''
    out = ""

    for i in range(len(list)):

        if i == len(list) - 1:
            out = out + list[i]

        else:    
            out = out + list[i] + " / "
    
    return out


def selection_sort (vector):
    n = len(vector)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vector[min_idx]>vector[j]:
                min_idx = j
        vector[i], vector[min_idx] = vector[min_idx], vector[i]
    print(vector)