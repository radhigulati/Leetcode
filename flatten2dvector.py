class ArrayList(object): 
    
    def __init__(self, vec):
        self.vec = vec
        self.row = 0
        self.col = 0
        i = 0
    
    def hasNext(self):
        #edge case
        if self.row == len(self.vec):
            return False
        if self.col != len(self.vec[self.row]):
            return True
        else:
            self.row += 1
            
        while self.row != len(self.vec):
            if len(self.vec[self.row]) != 0:
                   self.col = 0
                   return True 
            self.row += 1
        return False
            
                
    def next(self): 
        ret = self.vec[self.row][self.col]  
        self.col += 1  
        return ret  
    
    def remove():
        pass 


arr = ArrayList([[1,2,3],[4,5,6]])
print(arr.next())
print(arr.next())
print(arr.next())
print(arr.hasNext())
print(arr.next())
print(arr.next())
print(arr.next())