"""
Linked List
- is basically a data structure for storing collection of data or items

class Box{
    int data;
    Box next
}

head.data
- the data of the head

head
- represents the first box

Box next
- reflects to the next box that is connected to a particular box

[6|->]  ->  [3|->]  ->  [ |]
self.head  head.next head.next.next
head	   previous    current

head.next = current.next
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def sort(self):
        if self.head is None:
            return

        changed = True
        while changed:
            current = self.head
            changed = False
            while current.next:
                if current.data < current.next.data:
                    current.data, current.next.data = current.next.data, current.data
                    changed = True
                current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

# Input Values
input_values = [6, 3, 4, 2, 1]

my_linked_list = LinkedList()
for value in input_values:
    my_linked_list.insert(value)

print("Original linked list:")
my_linked_list.display()
print("Sorted Linked list: ")
# Sort the Linked List in descending order
my_linked_list.sort()
# Display the Linked List
my_linked_list.display()

