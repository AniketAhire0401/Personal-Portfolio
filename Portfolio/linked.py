from select import select


class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
       
class LinkedList:
    def linked_list(self):
        self.head = None
        self.numofnodes = 0
        
    def insert_at_start(self, data) :
        
        self.numofnodes = numofnodes + 1
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            
        else :
            new_node.next = self.head
            self.head = new_node               
    def traverse(self):
        actualnode= self.head
        while actualnode != None:
            print(actualnode.data)
            actualnode = actualnode.next

a = LinkedList()
a.insert_at_start(10)
a.insert_at_start(20)  
a.traverse()      