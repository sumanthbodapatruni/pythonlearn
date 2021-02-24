def div(a,b):
    print(a/b)

def smart_div(func):          # adds below operations to above function - edit div function
    
    def inn(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inn

div=smart_div(div)
div(2,4)
