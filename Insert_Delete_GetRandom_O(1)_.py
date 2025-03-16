import random

class RandomizedSet(object):

    def __init__(self):
        self.list = []
        self.index_dict = {}
        self.current_list_length = 0
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.index_dict:
            return False
        
        self.list.append(val)
        self.current_list_length += 1
        self.index_dict[val] = self.current_list_length - 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.index_dict:
            index = self.index_dict[val]
            last_ele = self.list[-1]
            
            # Only swap, when it's not the last element
            if val != last_ele:
                self.list[index] = last_ele
                self.index_dict[last_ele] = index

            # Delete the last element.
            self.list.pop()
            del self.index_dict[val]
            self.current_list_length -= 1
            return True
        
        return False

        

    def getRandom(self):
        """
        :rtype: int
        """

        return random.choice(self.list)


        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
