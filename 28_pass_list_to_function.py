def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2==0:
            even+=1
        else:
            odd+=1

    return even ,odd

lst=[2,4,5,6,78,8,67,56,5,4,3,3,4]

even,odd=count(lst)
print("even : {} and odd :{} "   .format(even,odd))
