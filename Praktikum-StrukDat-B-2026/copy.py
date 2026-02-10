parents, babies = (1, 1)
while babies < 100:
    print (f'This generation has {babies} babies')
    parents, babies = (babies, parents + babies)
                        # 1   0+1
                        # 1   1+1
                        # 2   2+1
                        # 3   3+2
                        # 5   5+3
                        # 8   8+5

def greet(name):
    print ('Hello', name)

greet('Jack')
greet('Jill')
greet('Bob')