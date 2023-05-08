"""
Data Structures and Algorithms

A brief overview of LinkedList using Python. Below are the methods implemented
1. pop
2. pop_first
3. get
4. set_value
5. append
6. prepend
7. insert
8. remove
9. reverse

By: Amitabh Suman (amitabhsuman.ss89@gmail.com)
"""

from typing import Union

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
    3. Method to pop from end
    4. Method to pop from first
    5. Method to prepend
    """

    def __init__(self, value: int) -> None:
        """
        Creates a new node and inits head, tail and length of the new Linked List
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        Prints the list whenever called
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print("\n\n")

    def get(self, index: int) -> Union[None, Node]:
        """
        Get the node at index from the linked list
        3 conditions are checked here is
        1. If thr index passes is valid
        2. If the index asked is 0 (not entirely necessary though)
        3. If its a index within range
        """
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.head

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index: int, value: int) -> bool:
        """
        Set value of certain index to the passed on value
        """
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def append(self, value: int) -> bool:
        """
        Create a new node and appends to endof the list
        Checks if the list was empty. If so, assigns head and tail with new node
        Progresses the tail to point to the newly created node
        Return True (optional return)
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # pylint: disable=inconsistent-return-statements
    def pop(self) -> Union[None, Node]:
        """
        Pops the element from end of the list.
        Conditions checked are:
        1. Check if linkedlist is empty, return None
        2. If not 1 : take 2 variables
            1. pre and temp
            2. pre is temp to start with
            3. While temp.next is not none, in loop : assign pre = temp and temp = temp.next
            4. Once loop exits (O(n)) : pre points to last temp, before the None
              (temp points to this node)
            5. Assign tail to pre and tail.next to none
            6. Reduce the length by 1
        """
        # check if we have empty case
        if self.head is None:
            self.tail = None
            print("Noting to pop")
            return None

        # remove the last element
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.head == self.tail:
            print(f"Popped value : {self.head.value}")
            self.head = None
            self.tail = None
            return

        print(f"Removed value : {temp}  : value : {temp.value}")
        return temp

    def prepend(self, value: int) -> None:
        """
        1. Create a new node.
        2. Checks if the list is none.
        3. If 2 : then assign head and tail to new node and tail.next to none
        4. if not 2 : store head to a pre variable. Assign head to new node
        5. head.next to pre
        6. Increase lenght by 1
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None

        if self.head:
            pre = self.head
            self.head = new_node
            self.head.next = pre

        self.length += 1

    # pylint: disable=inconsistent-return-statements
    def pop_first(self) -> Union[None, Node]:
        """
        1. Checks if the list is none, return None
        2. If len of list is 1 : make head and tail as none and lenght as 0
        3. If length is more than 1 : Save head in a temp variable.
        4. Make head = head.next
        5. Make temp.next = None
        6. Decrease lenght by 1
        """
        if self.head is None:
            return None

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return None

        if self.length > 1:
            temp = self.head
            self.head = self.head.next
            self.length -= 1
            temp.next = None
            print(f"Popped {temp} : {temp.value}")
            return temp

    def insert(self, index: int, value: int) -> Union[bool, None, Node]:
        """
        Function to insert a value at given index.
        Few conditions that can be checked for implementation
        1. Check if insert is right at the begining or end
        2. If no, the traverse till the index and insert
        """
        if index > self.length or index < 0:
            print("Index out of range")
            return False

        if index == 0:
            # Check if the index is 0. If so, invoke the prepend method
            # which will check for the status of the list
            # Performs checks related to Empty list and so on.
            return self.prepend(value)

        if index == self.length:
            # User intends to insert at end of the list.
            # Used the append function
            return self.append(value)

        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index: int) -> Union[None, Node]:
        """
        Remove by index. Things we have considered here are:
        1. Check for index validity
        2. If we have index at 0 or at end, we have methods to remove them already
        3. If index is in range, we remove it by retriving the index-1 node and applying as below.
        """
        if index < 0 or index > self.length:
            return None

        if index == 0:
            self.pop_first()

        if index == self.length - 1:
            self.pop()

        prev = self.get(index - 1)
        # Since get is O(n), using prev to retrieve the temp value
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self) -> None:
        """
        Most common DSA question. The order of the code matters here a lot.
        So small explanation as below
        1. First reverse the Head and Tail node
        2. Take 2 variables: before and after
        3. before is none and after is temp.next
        4. Iterate through the linked list and in below order, reverse the list
        5. First after = temp.next
        6. Then temp.next = before
        7. Then before = temp
        8. Then temp = after 
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = None
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# Try below

j = LinkedList(0)
j.print_list()

j.append(1)
j.print_list()

j.append(2)
j.print_list()

j.append(3)
j.print_list()

j.append(4)
j.print_list()

print("Checking Pop")
j.pop()
j.print_list()

print("Checking Prepend")
j.prepend(10)
j.print_list()

print("Checking Pop")
j.pop_first()
j.print_list()

print("Checking Insert")
j.insert(2, 10)
j.print_list()

print("Checking Get")
j.get(2)
j.print_list()

print("Checking Set")
j.set_value(2, 4)
j.print_list()

print("Checking Remove")
j.remove(2)
j.print_list()
