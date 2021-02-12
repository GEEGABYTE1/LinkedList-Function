def remove_nodes(self, value):
        current_node = self.get_head_node()

        while current_node:
            next_node = current_node.get_link()
            if current_node.get_value() == value:
                current_node = None
            else:
                print(current_node.get_value())
            
            current_node = next_node
                
                
def insert_node_back(self, new_value):
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

