"""
DATA STRUCTURES AND ALGORITHMS : TORTOISE AND HARE PROBLEM -or- TWO POINTER

This code defines a function find_kth_from_end(ll, k) that finds the k-th node from the end of a linked list.
The function takes two arguments, ll representing the linked list and k representing the position of the node
to be found from the end.

The function initializes two pointers, slow and fast, both initially pointing to the head of the linked list.

It then moves the fast pointer k nodes ahead in the list. If fast becomes None before moving k steps,
it means the list is shorter than k nodes, and the function returns None.

Once the fast pointer is k nodes ahead, the function enters a loop that continues until the fast pointer reaches the
end of the list.

Inside the loop, both the slow and fast pointers move one node forward at each iteration.

When the fast pointer reaches the end of the list, the slow pointer will be at the k-th node from the end of the list.

The function returns the slow pointer, which points to the k-th node from the end.

This algorithm is known as the "tortoise and hare" or "two-pointer" technique and allows us to find the k-th node
from the end of a singly linked list in a single pass with O(n) time complexity.

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

    def append(self, value):
        """
        Create a new node and appends to endof the list
        Checks if the list was empty. If so, assigns head and tail with new node
        Progresses the tail to point to the newly created node
        Return True (optional return)
        """
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
def find_kth_from_end(ll, k):
    # Initialize both slow and fast pointers to head
    slow = fast = ll.head
    # Move the fast pointer k nodes ahead
    for _ in range(k):
        if fast is None:
            return None  # List is shorter than k
        fast = fast.next

    # Move slow and fast pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next

    # Return the slow pointer (k-th node from the end)
    return slow