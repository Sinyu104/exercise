'''
class Shape:
    #edge=0
    def set_edge(self,edg):
        self.edge=edg
    def display(self):
        for i in range(self.edge+1):
            print('*'*i)
            print()
x=Shape()
x.set_edge(5)
x.display()
'''
'''
class Life:
    map=[]
    row=0
    min=0
    certer=0
    def set_map(self, n):
        self.row=n
        self.center=int(n/2-0.5)
        for i in range(1,n+1):
            self.map.append(['*']*n)
    def display(self):
        for i in range(0,self.row):
            for j in range(0,self.row):
                print(self.map[i][j],end='')
            print()
    def set_pattern(self,n):
        if(n==1):
            self.map[self.center-1][self.center]=0
            self.map[self.center-1][self.center-1]=0
            self.map[self.center-1][self.center+1]=0
            self.map[self.center][self.center-1]=0
            self.map[self.center+1][self.center]=0
        else:
            return None


my_map = Life()
my_map.set_map(7)
my_map.display()
print('---------------')
my_map.set_pattern(1)
my_map.display()
'''
class Map:
    map=[]
    row=0
    min=0
    certer=0
    def __init__(self,n,p):
        self.row=n
        self.center=int(n/2-0.5)
        for i in range(1,n+1):
            self.map.append(['*']*n)
        if(p==1):
            self.map[self.center-1][self.center]=0
            self.map[self.center-1][self.center-1]=0
            self.map[self.center-1][self.center+1]=0
            self.map[self.center][self.center-1]=0
            self.map[self.center+1][self.center]=0
        else:
            return None
    def display(self):
        for i in range(0,self.row):
            for j in range(0,self.row):
                print(self.map[i][j],end='')
            print()
my_map = Map(5, 1)
my_map.display()
    