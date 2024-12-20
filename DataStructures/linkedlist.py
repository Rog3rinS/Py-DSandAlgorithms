class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None #We will set this to point to the next node in the list
    
    def __init__(self, data): #After the object is created we pass the data to the object
        self.data = data
    
    def __repr__(self):
        return "%s" % self.data #Return the data in the node in the form of a string
 

class LinkedList:
    def __init__(self):
        self.head = None #Setting the head of the list as None to start

    def is_empty(self):
        return self.head == None #Verifying if the list is empty by checking if the head exists

    def size(self):
        """
        Returns the number of nodes in the list
        Takes O(n) time
        """
        current = self.head #Start or current at the head of the list
        count = 0
        
        while current: #while current exists
            count += 1
            current = current.next_node
        
        return count #found the count of nodes in the list

    def add(self, data):
        """
        Adds a new Node containing data at the head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node #Setting the head to the new node

    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index): #Inserting a node at a specific index
        if index == 0: #if is to insert in position 0 we just call the add method
            self.add(data)

        if index > 0: #if not we need to find the position to insert the node
            new = Node(data) #we create our new object
            position = index
            current = self.head #we set a pointer to the head of the list

            while position > 1: #we iterate through the list until we reach the position we want to insert the node at
                current = current.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def removeindex(self, index):
        current = self.head
        if index == 0:
            self.head = current.next_node
        if index > 0:
            position = index
            
            while position > 1:
                current = current.next_node
                position -= 1

            otherindex = current.next_node
            current.next_node = otherindex.next_node

    def remove(self, target):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == target and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == target:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)



