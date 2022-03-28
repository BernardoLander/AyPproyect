v=int(input("Enter number to test for vampire:"))
#Test for pair number of digits
def nd(a):
    nd = 0
    while a != 0:
        d = a % 10
        if d != 0:
            nd += 1
        a = a // 10
    return nd
def DigitosPar(a):
    if nd(a)%2==0:
        return 1
    else:
        return 0
#Last digit is 0
def UltimoDigCero(b):
    ud = 0
    ud = b % 10
    if ud==0:
        return 1
    else:
        return 0

if DigitosPar(v)==1:
    x=[]
    for i in range(int(10**(nd(v)/2-1)),int(10**(int(nd(v))/2))):
        x.append(i)
    y=x
    z=0
    posiblex=0
    posibley=0
    for ia in range(0,len(y)):
        for ib in range(0,len(x)):
            z=y[ia]*x[ib]
            if z==v and not((UltimoDigCero(x[ib])==1 and UltimoDigCero(y[ia])==1)):
                posiblex=x[ib]
                posibley=y[ia]
                print(v,"has as fangs",posiblex,posibley)
    if posiblex==0:
        print(v, "not a vampire")
else:
    print(v, "not a vampire")