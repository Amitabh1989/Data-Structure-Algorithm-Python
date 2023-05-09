"""
DSA with Python with Amitabh

Implementation of Floyd's algorithm with Python.

Using 2 pointers : slow and fast.

Logic goes as here:
Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer
algorithm that uses only two pointers, moving through the sequence at
different speeds. This algorithm is used to find a loop in a linked list.
It uses two pointers one moving twice as fast as the other one. The faster
one is called the fast pointer and the other one is called the slow pointer.

How Does Floyd’s Cycle Finding Algorithm Works?

While traversing the linked list one of these things will occur-
1. The Fast pointer may reach the end (NULL) this shows that there is no
   loop in the linked list.
2. The Fast pointer again catches the slow pointer at some time therefore a
   loop exists in the linked list

Pseudocode:
1. Initialize two-pointers and start traversing the linked list.
2. Move the slow pointer by one position.
3. Move the fast pointer by two positions.
4. If both pointers meet at some point then a loop exists and if the fast
   pointer meets the end position then no loop exists.

by Amitabh Suman
"""

# pylint: disable=too-few-public-methods
class Node:
    """
    Class for creating a new node
    Seperate class for SRP : Single Responsibility Principle
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """
    Class that contains all the functionality related to a Linked List
    1. Create Head and Tail of linked list
    2. Method to append new node
    """

    def __init__(self, value):
        """
        Creates a new node and inits head, tail and length of the new Linked List
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        """
        Create a new node and appends to endof the list
        Checks if the list was empty. If so, assigns head and tail with new node
        Progresses the tail to point to the newly created node
        Return True (optional return)
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # WRITE HAS_LOOP METHOD HERE #
    # pylint: disable=inconsistent-return-statements
    def has_loop(self):
        """
        Checks if the linked list has loops within
        :return: bool
        """
        slow = self.head
        fast = self.head

        if self.head:
            # while fast.next is not None:
            # for i in range(self.length):
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    print(f"Slow is : {slow.value}, Fast is {fast.value}")
                    print("Loop exists")
                    return True
            return False
    ##############################


my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
# pylint disable=pointless-string-statement
print(my_linked_list_1.has_loop())  # Returns True

my_linked_list_2 = LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print(my_linked_list_2.has_loop())  # Returns False

"""
    EXPECTED OUTPUT:
    ----------------
    True
    False
    
"""
