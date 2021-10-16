def minmp(filename, compound_formula):
    """(str, str) -> (str, int)
    When passed a filename with a listing of elements and properties and a compound_formula. Returns a tuple where the first element is the lowest melting point element in the compound and the second element is it's corresponding melting point.
    >>>minmp("elements.txt", "K1Fe4")
    'K', 336
    >>>minmp("elements.txt", "Fe6Cr1")
    'Fe', 1811
    """   
    letter = compound_formula
    lst = list(compound_formula)
    lets = []
    end = []
    for char in lst:
        if char in "abcdefghijklmnopqrstuvwxyz":
            new = lst[lst.index(char)-1] + char
            lets.append(new)
    for char in lst:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s = ' '.join(lets)
            if char not in s:
                lets.append(char)
    for word in lets:
        with open(filename) as file:
            for i in range(0,4):
                next(file)
            for line in file:
                if word in line:
                    s = line.find('\t')
                    e = line.rfind('\t')
                    p = line[s+1:e]   
                    end.append(p)
    end = ' '.join(end)
    numbers = [int(number) for number in end.split()]
    numbers.sort()
    
    with open(filename) as file:
        for i in range(0,4):
            next(file)
        for x in file:
            if str(numbers[0]) in x:
                s = x.find("\t")
                l = x[:s]
        
    return l, numbers[0]
    
def molform(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary with a string of the element symbol as the key and the number of atoms of that element as the value.
    >>>molform("C2H6O1")
    {'C':2, 'H':6, 'O':1}
    >>>molform("C1H4")
    {'C':1, 'H':4}
    """
    lst = list(compound_formula)
    letter = []
    lets = []
    num = []
    count=1
    for char in lst: 
        if char in "0123456789":
            num.append(int(char))
        if char in "abcdefghijklmnopqrstuvwxyz":
            new = lst[lst.index(char)-1] + char
            lets.append(new)
            letter.append(new)
    for char in lst:
        if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            s = ' '.join(lets)
            if char not in s:
                letter.append(char)
    d = dict(zip(letter, num))
    return d

print(molform("Fe5Ca7O6"))