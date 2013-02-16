
"""
This class will create a network of spikeNodes based on the algorithm defined
in spike_generator.  The maximum width and maximum depth of the network are defined during the
creation of the collection.  These help keep the collection in bounds of what
is possible on a given system, but allow the generation algorithm freedom to
expand up to those constraints.
"""
import random

from spikeNode import *


class spikeGenerator(object):

    def __init__(self, max_nodes, gen_func = None):
        self.max_nodes = max_nodes
        self.gen_func = gen_func

    def default_gen_func(self, max_nodes):
        node_list = []


        width = 6

        depth = 50

        def inc(level):
            roll = random.random()
            if roll < 0.2:
                return level + roll
            else:
                return level + 0.1 + (roll / 10)

        node_structure = []
        
        for d in range( 0, depth ):
            temp_list = []
            
            for n in range(0,width):
                temp_node = spikeNode( None, 1, 0, 0, inc )
                
                temp_list.append( temp_node )
                node_list.append( temp_node )

            node_structure.append( temp_list )

            if d == 0:
                pass
            else:
                for node in node_structure[ d - 1 ]:

                    for child in node_structure[ d ]:
                        is_child = random.random()

                        if is_child > 0.5:
                            node.add_child(child)
                



            
        return node_list

    def generate(self):
        if self.gen_func is None:
            self.gen_func = self.default_gen_func

        node_list = self.gen_func(self.max_nodes)
        
        return node_list
        
