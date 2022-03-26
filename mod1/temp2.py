def print_list_cute(list):
    '''Prints lists in a cute way'''

    if len(list) > 1:
        for i in range(len(list)):
            print(list[i],end='')
        return
    else:
        print(list[0],end='')
        return

def main():
    list = ["hello",'world,','fuck','you']
    print_list_cute(list)

main()