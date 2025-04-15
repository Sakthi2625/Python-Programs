class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        i = self.head

        while i.next:

            i = i.next

        i.next = new_node

    def display(self):
        i = self.head
        while i:
            print(i.data)
            i = i.next

    def remove(self,item):
        
        if item == self.head.data:       
            self.head = self.head.next
         
        else:
            i= self.head.next
            prev= self.head
            while True:
                if i.data == item:
                    # i=i.next
                    prev.next=i.next
                    # prev=i
                    break
                prev=i
                i=i.next
    def insert(self,position,data):
        new_node=Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        i=self.head
        for j in range(position-2):
            i=i.next
        new_node.next = i.next
        i.next = new_node

  
l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.display()
print("#######################################")
l.remove(3)
l.display()
print("#######################################")
l.insert(2,5)
l.display()

