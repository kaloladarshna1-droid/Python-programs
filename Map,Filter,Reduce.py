from functools import reduce
l = [1,23,5,6,8]

def cube(x) :
    return x*x*x

a = list(map(cube,l))
print(a)

# Filter
def Filter(A) :

    return A > 3 
    
newl = list(filter(Filter,l))
print(newl)

#Reduce

print(reduce(lambda x,y : x+y,l ))