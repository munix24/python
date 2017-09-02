def permute(elements):
    """recursively generate list of all possible permutations"""
    if len(elements) <=1:
        yield elements
    else:
        for perm in permute(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                
def permute2(lst):
    """recursively return list of all possible permutations"""
    if len(lst) == 0:
        return []
 
    if len(lst) == 1:
        return [lst]
 
    l = [] 
 
    for i in range(len(lst)):
       m = lst[i]
       tempLst = lst[:i] + lst[i+1:]
       
       for p in permute2(tempLst):
           l.append([m] + p)
    return l
