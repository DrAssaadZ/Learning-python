# let's talk about functions
def num_sign(i:int):
    if i<0:
        print('neg')
        return i
    elif  i==0:
        print('null')
        return i
    else:
        print('pos')
        return i

x= num_sign(0)
print(x)
