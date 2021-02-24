from functools import reduce


def is_even(n):
    return n%2==0


nums=[3,8,9,0,5,3,5,67,89]
evens=list(filter(is_even,nums))
print(evens)




even=list(filter(lambda n:n%2==0,nums))
print(even)

doubles=list(map(lambda n:n+2,even))
print(doubles)

sum= reduce(lambda a,b:a+b,doubles)
print(sum)

