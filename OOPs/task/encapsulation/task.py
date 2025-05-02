class Student:
    def __init__(self, name, mark):
        self.name = name
        self.__mark = mark
        
    @property
    def mark(self):
        return self.__mark
    
    
    @mark.setter
    def set_mark(self, value):
        if 0 <= value <= 100:
            self.__mark = value
        else:
            print("invalid marks")
            
            

s = Student("alice", 95)

print(s.mark)

# s.mark = 98

s.set_mark = 120



print("last mark: ", s.mark)