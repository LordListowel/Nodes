#Implementing a system of 3 nodes in which the first node is linked to the second, 
#and the second is linked to the third. The third node is the terminal node and hence
#will have no link node"""
class Node:
    def __init__(self,value:int,link_node=None):
        """Initializes the structure of the Node class instances"""
        self.value=value
        self.link_node=link_node
    def get_value(self):
        """gets the value of a specific node"""
        return self.value
    def get_link_node(self):
        """gets the link node of a particular node if it has one"""
        return self.link_node
    def set_link_node(self,link_node):
        """links a node to another node"""
        self.link_node=link_node

#creating the three Node class instances
Emmanuella=Node(15)
Richarda=Node(12)
Listowel=Node(20)
#Setting link nodes such that Listowel is linked to Emmanuella and Emmanuella is linked to Richarda
#Richarda will be the terminal node because she is the youngest lol
Listowel.set_link_node(Emmanuella)#this sets emmanuella as the link node of Listowel
Emmanuella.set_link_node(Richarda)#this sets Richarda as the link node of Emmanuella
#We can now get Emmanuella's age from Listowel because she is linked to him
#We can also get Richarda's age from Emmanuella

#Getting Emmanuella's age from Listowel
print(Listowel.link_node.get_value())
print(Emmanuella.link_node.get_value())


    
