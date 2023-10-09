#single linked list 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("LinkedList is Empty")
        else:
            temp = self.head
            while temp:
                print(temp.data ,"===>" ,end=" ")
                temp = temp.next
lis = SingleLinkedList()
n1 = Node(10)
lis.head= n1
n2= Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
lis.display()

##output:  10 ===> 20 ===> 30 ===> 
