class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    #you forgot when the list is empty. I fix your code :)
    def __str__(self):
        result = ""
        if self.__size == 0:
            result = "[]"
        else:
            result = "["

            current = self.__head
            for i in range(self.__size):
                result += str(current.element)
                current = current.next
                if current != None:
                    result += ", " # Separate two elements with a comma
                else:
                    result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element o 
    def contains(self, e):
        #iterate through the objects and check each object's element value to see if it matches the parameter.
        #break out of loop if next is None or element is found
        current = self.__head
        if current == None:
            return False
        while current.element != e:
            if current.next == None:
                break;
            current = current.next

        #return true if element was found, else false
        if current.element == e:
            return True
        else:
            return False

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        #switch scenario based on size of list.
        match self.__size:
            case 0:
                #no element to remove
                return False
            case 1:
                #only need to check the head element
                if self.__head.element == e:
                    self.__head = self.__tail = None
                    self.__size -= 1
                    return True
                else:
                    return False
            case _:
                # check if head has element. if not, previous = head, current = previous.next and loop through until current = element.
                #print("case _")
                if self.__head.element == e:
                    #nextAddress = self.__head.next
                    #print("the object address of the head is: " + str(self.__head))
                    #print("the next object address after head is: " + str(self.__head.next))
                    #print("I will make the head object address the head.next object address now...")
                    self.__head = self.__head.next
                    #print("head object address is now: " + str(self.__head))
                    #print("is the new address the same as the head.next address? " + str(self.__head == nextAddress))
                    #print("what is the element of the new head? " + str(self.__head.element))
                    self.__size -=1
                    return True
                else:
                    #print("remove not head")
                    previous = self.__head
                    current = previous.next
                    while current.element != e:
                        # stop looping if there are no more elements
                        if current.next == None:
                            break;
                        # update previous and current to next element
                        previous = current
                        current = current.next

                    # check if element was found. if element is at tail, make previous the new tail, change previous next to None.
                    # if element is not at tail, previous.next will be current.next,
                    if current.element == e:
                        if current == self.__tail:
                            previous.next = None
                            self.__tail = previous
                        else:
                            previous.next = current.next
                        self.__size -= 1
                        return True
                    else:
                        return False

    # Return the element from this list at the specified index 
    def get(self, index):
        #store object of the given index in variable
        current = self.__head
        #loop through to the given index
        for element in range(index):
            if current == None:
                break;
            current = current.next
        #check if object is None. if it is, return none, else, return object's element
        if current == None:
            return None
        else:
            return current.element

    # Return the index of the first matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        #crate variables to hold index and current object
        indexAccumulator = 0
        current = self.__head

        #loop through until current element equals given element
        while current.element != e:
            current = current.next
            indexAccumulator += 1
            if current == None:
                break;

        #check if element was found. if not, return -1, else return the index
        if current == None:
            return -1
        else:
            return indexAccumulator

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        #3 variables, 1 for index of last matching element, 1 for accumulating index, and 1 for the current object
        lastIndex = None
        indexAccumulator = 0
        current = self.__head
        #Loop through list until the end of the list. if current object has element e, store index in lastIndex var
        while current != None:
            if current.element == e:
                lastIndex = indexAccumulator
            current = current.next
            indexAccumulator += 1

        #check if lastIndex value was updated. if not, return -1. else, return the value
        if lastIndex == None:
            return -1
        else:
            return lastIndex


    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        #store current object in variable. loop through list until you reach the given index, change element value to e
        current = self.__head
        #do not loop if index = 0
        if index == 0:
            current.element = e
        #throw exception errors if index is outside of acceptable range
        elif index < 0:
            raise Exception("Index value out of range")
        elif index >= self.__size:
            raise  Exception("Index value out of range")
        #loop if index != 0
        else:
            for element in range(index):
                current = current.next
        #change element value to e
        current.element = e
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    
