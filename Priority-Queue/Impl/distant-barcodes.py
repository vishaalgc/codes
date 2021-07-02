"""
Distant Barcodes
https://leetcode.com/problems/distant-barcodes/

"""


class Element:

    def __init__(self,val,freq):
        self.val = val
        self.freq = freq


class Maxheap:

    def __init__(self):
        self.heap = []

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        return False

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
            while self.hasParent(index) and self.getParent(index).freq < self.heap[index].freq:
                self.swap(index,self.getParentIndex(index))
                index = self.getParentIndex(index)
    
    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChild(index).freq > self.getLeftChild(index).freq:
                smallChildIndex = self.getRightChildIndex(index)
            if self.heap[index].freq < self.heap[smallChildIndex].freq:
                break
            else:
                self.swap(index,smallChildIndex)
            index = smallChildIndex 

    def poll(self):
        if self.heap:
            item = self.heap[0]
            self.heap[0] = self.heap[len(self.heap)-1]
            del self.heap[len(self.heap)-1]
            self.heapifyDown()
            return item

    

    def add(self,val):
        self.heap.append(val)
        self.heapifyUp()

    def printer(self):
        for item in self.heap:
            print(item.val,item.freq)

class Solution:

    def rearrangeBarcodes(self, barcodes):

        maxheap = Maxheap()
        mp = {}
        for i in barcodes:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        
        for key in mp.keys():
            e = Element(key,mp[key])
            maxheap.add(e)
        
        # maxheap.printer()

        out = []
        
        while not maxheap.isEmpty():
            elem1 = maxheap.poll()
            elem2 = maxheap.poll()
            out.append(elem1.val)
            out.append(elem2.val)
            if elem1.freq > 1:
                elem1.freq-=1
                maxheap.add(elem1)
            if elem2.freq > 1:
                elem2.freq-=1
                maxheap.add(elem2)
        
        return out



s = Solution()
codes = [1,1,1,1,2,2,3,3]

print(s.rearrangeBarcodes(codes))
        

