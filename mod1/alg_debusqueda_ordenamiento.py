def selection_sort (vector):
    n = len(vector)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if vector[min_idx]>vector[j]:
                min_idx = j
        vector[i], vector[min_idx] = vector[min_idx], vector[i]
    print(vector)

def linear_search(vector, key, keyName=''):
    temp = None
    for element in vector:
        if element.get(keyName) is not None:
            if element[keyName] == key:
                temp = element
                return temp
    
def linear_search_mio(list,num):

    for i in range(len(list)):
        if list[i] == num:
            print(f'{num} is in index {i} in list {list}')
            return
    print(f'{num} is not in list {list}')



def main():
    vector = [4,3,5,1,2]
    #selection_sort(vector)
    linear_search_mio (vector, 2)

main()
