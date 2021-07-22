"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        pos = 1
        current = self.head
        if position < 1:
            return None
        while current and pos <= position:
            if pos == position:
                return current
            current = current.next
            pos += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        pos = 1
        current = self.head
        if position > 1:
            while current and pos < position:
                if pos == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                pos += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
    

    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
