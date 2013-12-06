class s:
    k = 0
    i = []
    def simple(self):
        self.i.append(len(self.i))
    
def inc():
    t = s()
    t.b = len(t.i)
    t.i.append(len(t.i))
    return len(t.i)


a = s()
a.k = 1
a.simple()
b = s()
b.k = 2
b.simple()

print(len(b.i), b.k)
print(len(a.i), a.k)