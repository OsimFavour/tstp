class Node:                                              # a subclass of the linked_list.
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self) -> None:
        self.head = Node()                               # used as a place holder to allow us to point to the first element in the list.

    def append(self, data):                              # adding on a new data point to the end of the current list.
        new_node = Node(data)                            # creating a new_node of the class Node and passing the data into it which will set the data point inside the node.
        cur = self.head
        while cur.next != None:                          # creating the variable to store the node that we are currently looking at iterating over 
            cur = cur.next                               # each one of the nodes in the list starting with the head and once we get to a point where
        cur.next = new_node                              # the next node of the current node is none, we know that that will be the last point in the list, 
                                                        
    def length(self):                                    
        cur = self.head 
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):                                       # Function used to display the current content of our list.
        elems = []
        cur_node = self.head 
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):                                     # an extractor function to pull out a data point at a certain index from our linked list
        if index >= self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0                                           # create a variable to contain the current index
        cur_node = self.head                                  # a variable to contain the current number we are looking at
        while True:                                           # then begin the iteration
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1
        
    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

my_list = Linkedlist()

my_list.append(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

my_list.display()

# print("element at 2nd index: %d" % my_list.get(2))
                                                                      
                                                  
                                                      
            
    
       
       