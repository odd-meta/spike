

class spikeNode(object):
    """
    each time we create a new node we give it:
        * A children list, which can be another node(s), or None
        * A threshold value that is used to figure out when to signal all child nodes
        * The current level of the node, when level > threshold, the node signals it's children and resets level to baseline
        * the function used to increase the level by when signaled, level += 1, etc.
    """
    def __init__(self, children, threshold, baseline, level, level_increment):
        self.children = children
        self.threshold = threshold
        self.baseline = baseline
        self.level = level
        self.level_increment = level_increment

    def signal(self):

        self.level = self.level_increment(self.level)

        if self.level > self.threshold:
            print "trigger for \n%s" % self
            self.level = self.baseline
            
            if isinstance(self.children,list):
                
                for child in self.children:
                    if isinstance(child, spikeNode):
                        child.signal()
        return self.level


    def add_child(self,child):
        if isinstance(self.children,list):
            self.children.append(child)
        else:
            self.children = []
            self.children.append(child)
                
        
    def __str__(self):
        output = ""

        my_id = id(self)

        child_ids = []

        if isinstance(self.children,list):
            for child in self.children:
                child_ids.append(id(child))

        output += "My ID is %s\n" % my_id
        output += "My current level is %s\n" % self.level
        output += "I have %s children\n" % len(child_ids)
        

        if len(child_ids) > 0:
            output += "%s" % child_ids

        return output


        
        
        
