class Test:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def to_dict(self):
        my_dict = {}
        for i in self.key: 
            my_dict[i] = self.value
        print(my_dict)
    def dict_dublicates(self):
        a = Test.to_dict()
        print(a)
        temp = []
        res = dict()
        for key, val in my_dict.items():
            if val not in temp:
                temp.append(val)
                res[key] = val
                print(res)
                

c = Test("python", "123423")
# c.to_dict()
c.dict_dublicates()
# f = highest(1)