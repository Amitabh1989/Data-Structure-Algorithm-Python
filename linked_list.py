"""
Data Structures and Algorithms

A brief overview of LinkedList using Python.

Amitabh Suman
"""

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
    def __init__(self, value):
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
    
    def append(self, value):
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

    def pop(self):
        """
        Pops the element from end of the list.
        Conditions checked are:
        1. Check if linkedlist is empty, return None
        2. If not 1 : take 2 variables
            1. pre and temp
            2. pre is temp to start with
            3. While temp.next is not none, in loop : assign pre = temp and temp = temp.next
            4. Once loop exits (O(n)) : pre points to last temp, before the None (temp points to this node)
            5. Assign tail to pre and tail.next to none
            6. Reduce the length by 1
        """
        # check if we have empty case
        if self.head is None:
            self.tail = None
            print("Noting to pop")
            return None

        # remove the last element
        else:
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
                print("Popped value : {}".format(self.head.value))
                self.head = None
                self.tail = None
                return
            
            print("Removed : {}  : value : {}".format(temp, temp.value))
            return temp

    def prepend(self, value):
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

    def pop_first(self):
        """
        1. Checks if the list is none, return None
        2. If len of list is 1 : make head and tail as none and lenght as 0
        3. If length is more than 1 : Save head in a temp variable.
        4. Make head = head.next
        5. Make temp.next = None
        6. Decrease lenght by 1
        """
        if self.head == None:
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
            print("Popped {} : {}".format(temp, temp.value))
            return temp

# Try belows

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

j.pop()
j.print_list()

# j.pop()
# j.print_list()
# j.pop()
# j.print_list()
# j.pop()
# j.print_list()
# j.pop()
# j.print_list()

j.prepend(10)
j.print_list()

j.pop_first()
j.print_list()