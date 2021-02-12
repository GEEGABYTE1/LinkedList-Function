def remove_nodes(self, value):                                                 #Removes certain nodes that have the specified value all at once
        current_node = self.get_head_node()

        while current_node:
            next_node = current_node.get_link()
            if current_node.get_value() == value:
                current_node = None
            else:
                print(current_node.get_value())
            
            current_node = next_node
                
                
def insert_node_end(self, new_value):                                           #Adds a new node at the end of the Linked List instead the start
        new_node = Node(new_value)
        current_node = self.get_head_node()

        while current_node:
            next_node = current_node.get_link()

            if current_node.get_link() == None:
                current_node.set_link(new_node)
                new_node.set_link(None)
                break
            else:
                current_node = next_node 
                
                
def insert_node_after_value(self, new_value, value):                           #Adds a new node after a certain node
        current_node = self.get_head_node()
        new_node = Node(new_value)

        while current_node:
            next_node = current_node.get_link()
            next_next_node = next_node.get_link()
            if next_node.get_value() == value:
                next_node.set_link(new_node)
                new_node.set_link(next_next_node)
                break
                
            else:
                current_node = next_node
  

 def insert_before_value(self, new_value, value):                               #Adds a new node before a certain node                
    current_node = self.get_head_node() 
    new_node = Node(new_value)


    while current_node:
        next_node = current_node.get_link()
        if next_node == value:
            new_node.set_link(self.head_node)
            self.head_node = new_node 
            print(self.head_node.get_value())
            #next_node = next_node.get_link()
        elif current_node.get_value() == value:
            new_node.set_link(current_node)
            print(new_node.get_value())
            print(current_node.get_value())
            current_node = next_node

        else:
            print(current_node.get_value())
            current_node = next_node
   
def remove_node_at_certain_index(self, index):                                  #Removes a node at certain index. Nodes start from 1.
        count = 1
        current_node = self.get_head_node()

        if index == 1:
            self.head_node = current_node.get_link()
        else:
            while current_node:
                count += 1
                next_node = current_node.get_link()

                if count == index:
                    current_node.set_link(next_node.get_link())
                    current_node = None
                else:
                    
                    current_node = next_node
                    
                
        
            
            
                

ll = LinkedList('a')
ll.insert_node('b')
ll.insert_node('c')
ll.insert_node('d')
ll.insert_before_value('e', 'b')
#print(ll.remove_nodes('b'))
#print(ll.stringify_list())

