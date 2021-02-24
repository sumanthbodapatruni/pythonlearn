def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)




person('satya',age=22,village='narsipatnam')



