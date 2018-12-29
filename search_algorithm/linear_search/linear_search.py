#define the method that accepts an array and the element to be searched
def linear_search(n, x):

    #loop over the array
    for element in n:
        if element == x:
            return n.index(element)
