pos=-1

def search(list,n):
    i=0

    while i< len(list):
        if list[i] == n:
            globals() ['pos'] =  i
            return True
        i=i+1

    return False

list = [4,5,7,8,6,4,3]
n=4
if search(list,n):
    print('found at ',pos+1)
else:
    print('not found')
