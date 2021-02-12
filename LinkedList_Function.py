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

