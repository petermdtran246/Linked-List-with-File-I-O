class Node:
    """
    Represents a single node in the linked list.

    Attributes:
        data (int): The data value stored in the node.
        next (Node): A reference to the next node in the linked list, or None if it's the last node.
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    Represents a linked list data structure.

    Attributes:
        head (Node): The first node in the linked list, or None if the list is empty.
    """
    def __init__(self):
        self.head = None

    def insert(self, data):
        """
        Inserts a new node with the given data into the linked list while maintaining sorted order.

        Args:
            data (int): The data value to insert.
        """
        new_node = Node(data)
        if not self.head or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, data):
        """
        Removes the first node containing the given data from the linked list.

        Args:
            data (int): The data value to remove.
        """
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, data):
        """
        Searches for a node containing the given data in the linked list.

        Args:
            data (int): The data value to search for.

        Returns:
            bool: True if the data is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def print_list(self):
        # Prints the contents of the linked list.
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next
        print('None')