
# Mapping
# index 
# left -> index*2 + 1
# right -> index*2 + 2
# parent -> (index-1) / 2


class Maxheap:

    def __init__(self):
        self.heap = []

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None

    def getLeftChild(self,index):
        return self.heap[(index*2)+1]

    def getLeftChildIndex(self,index):
        return (index*2)+1
    
    def getRightChildIndex(self,index):
        return (index*2)+2
        

    def getRightChild(self,index):
        return self.heap[(index*2)+2]
    
    def getParent(self,index):
        return self.heap[(index-1)//2]

    def getParentIndex(self,index):
        return (index-1)//2

    def hasParent(self,index):
        val = (index-1)//2
        if val < 0:
            return False
        return True

    def hasLeftChild(self,index):
        val = (index*2)+1
        if val < 0 or val > len(self.heap)-1:
            return False
        return True

    def hasRightChild(self,index):
        val = (index*2)+2 
        if val < 0 or val > len(self.heap)-1:
            return False
        return True

    def swap(self,index1,index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


    def heapifyUp(self):
        index = len(self.heap)-1
        if index >= 0:
            while self.hasParent(index) and self.getParent(index) < self.heap[index]:
                self.swap(index,self.getParentIndex(index))
                index = self.getParentIndex(index)
    
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChild(index) > self.getLeftChild(index):
                smallChildIndex = self.getRightChildIndex (index)
            if self.heap[index] < self.heap[smallChildIndex]:
                break
            else:
                self.swap(index,smallChildIndex)
            index = smallChildIndex 

    def poll(self):
        if self.heap:
            val = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            self.heapifyDown()
            return val

    def add(self,val):
        self.heap.append(val)
        self.heapifyUp()

    def printer(self):
        print(self.heap)


s = Maxheap()

s.add(1)
s.add(2)
s.add(10)
print(s.peek())
s.add(5)
print(s.poll())
s.printer()
    

        
        
    

