class Stack:
    def __init__(self):
        self.storage = []
    
    def push(self, num):
        self.storage.append(num)
    
    def pop(self):
        el = self.storage[0]
        self.storage.remove(self.storage[0])
        return el
    
    def size(self):
        return len(self.storage)
    
    def peek(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # push
        self.s1 = Stack()
        # pop
        self.s2 = Stack()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s2.size() == 0:
            # move elements from s1 to s2
            for _ in range(self.s1.size()):
                #populates s2 with s1 in reverse order
                self.s2.push(self.s1.pop())
            
            el = self.s2.pop()
            for _ in range(self.s2.size()):
                # repopulate the push stack and re-reverse the order
                self.s1.push(self.s2.pop())
            # return the top of pop stack
            return el
        
        
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        # check if pop is empty
        if self.s2.size() == 0:
            # peek the push stack
            return self.s1.peek()
        # otherwise peek the pop stack
        else:
            return self.s2.peek()
            

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        
        if self.s1.size() > 0 or self.s2.size() > 0:
            return False
        else:
            return True
        


# Driver Code
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.pop())
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.peek())
print(obj.empty())