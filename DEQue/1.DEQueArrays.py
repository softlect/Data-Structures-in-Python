class DEQueArray:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def addfirst(self, e):
        self._data.insert(0,e)

    def addlast(self, e):
        self._data.append(e)

    def removefirst(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop(0)

    def removelast(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data.pop()

    def first(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[0]

    def last(self):
        if self.isempty():
            print('DEQue is empty')
            return
        return self._data[-1]


D = DEQueArray()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
print('DEQue:',D._data)
print('DEQue Length:', len(D))
ele = D.removefirst()
print('DEQue:',D._data)
print('DEQue Length:', len(D))
print('Removed Element from Front:',ele)
ele = D.removelast()
print('DEQue:',D._data)
print('DEQue Length:', len(D))
print('Removed Element from Last:',ele)
