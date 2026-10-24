class Underscore:
    def map(self, iterable, callback):
        x=[]
        for item in iterable:
            x.append(callback(item))
        return x
    def find(self, iterable, callback):
        for item in iterable:
            if callback(item):
                return item 
            
          
    def filter(self, iterable, callback):
        x=[]
        for item in iterable:
            if callback(item):
                x.append(item)
        return x        
    def reject(self, iterable, callback):
        x=[]
        for item in iterable:
            if callback(item)==0:
                x.append(item)
        return x   


if __name__=="__main__":
    _ = Underscore() 
    x=_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
    print(x)

    y=_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
    print(y)

    evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)# should return [2,4,6] 
    print(evens)

    reject_even=_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]
    print(reject_even)

