class Pcache():
    data = []
    max
    def __init__(self,max=100):
        self.max = max

    def add(self,p):
        print("最大长度是{}".format(self.max))
        print("添加了一个")
        self.data.insert(0,p)
        for item in self.data:
            print(item.__dict__)
        if len(self.data) > self.max:
            self.data.pop()
            print("删除了一个")
            for item in self.data:
                print(item.__dict__)
    
    def get(self,name):
        if len(self.data) <1:
            return None
        for p in self.data:
            if p.router == name:
                return p
        return None

    def remove(self,name):
        if len(self.data) <1:
            return None
        for p in self.data:
            if p.router == name:
                self.data.remove(p)
                return p