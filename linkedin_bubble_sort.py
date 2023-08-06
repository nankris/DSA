class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        for i in range(self.length):
            pointer1  = self.head
            pointer2 = self.head.next
            for j in range(self.length-i):
                if j+1 < self.length and pointer1.value > pointer2.value:
                    tmp = pointer1.value
                    pointer1.value = pointer2.value
                    pointer2.value = tmp
                if pointer2 != None:
                    pointer1 = pointer1.next
                    pointer2 = pointer2.next
                else:
                    break
                  
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

my_linked_list.print_list()

my_linked_list.bubble_sort()

print("Sorted Linked List:")
my_linked_list.print_list()


