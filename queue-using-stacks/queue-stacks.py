class Stack:
    def __init__(self):
        self.storage = []
    
    def push(self, num):
        self.storage.append(num)
    
    def pop(self):
        el = self.storage[0]
        self.storage.remove(el)
        return el
    
    def size(self):
        return len(self.storage)
    
    def peek(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

class Queue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int):
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2.size() <= 0:
            # move elements from s1 to s2
            for _ in range(self.s1.size()):
                #populates s2 with s1 in reverse order
                self.s2.push(self.s1.pop())
            
        else:
            return self.s2.pop()
        
        
    def peek(self):
        """
        Get the front element.
        """
        return self.s2.peek()
            

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        
        if self.s1.size() > 0 or self.s2.size() > 0:
            return False
        else:
            return True
        



# Your MyQueue object will be instantiated and called as such:
obj = Queue()
obj.push(1)
obj.push(2)
print(obj.pop())
print(obj.peek())
print(obj.empty())
