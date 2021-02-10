def remove_lists(self, value_to_remove):
        current_node = self.get_head_node() 
        next_node = current_node.get_link()

            
        
        if current_node.get_value() != None:
            if current_node.get_value() == value_to_remove:
                updated_string_list = self.stringify_list().replace(str(current_node.get_value()), "")
                print(updated_string_list.strip("\n"))
        #print(type(self.stringify_list()))
        else:
            current_node = next_node
