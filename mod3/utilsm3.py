
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
    
        return verify_str(msg)