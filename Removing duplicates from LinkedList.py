class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1

    # Above code is part of the problem, below code is implemented by me
    def remove_duplicates(self):
        temp_hash = {}
        curr_node = self.head
        prev_node = self.head
        if curr_node == None:
            return None
        else:
            temp_hash[curr_node.value] = True
        curr_node = curr_node.next
        while curr_node:
            if curr_node.value not in temp_hash.keys():
                temp_hash[curr_node.value] = True
                curr_node = curr_node.next
                prev_node = prev_node.next
            else:
                prev_node.next = curr_node.next
                curr_node = curr_node.next
                self.length -= 1



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_all()


