
class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items[:limit] 
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
    

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range(len(self.items)-1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1