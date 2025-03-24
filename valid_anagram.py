class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Pythonic way to slove the problem, time O(nlogn)
        # s_list = [c for c in s]
        # t_list = [c for c in t]
        # s_list.sort()
        # t_list.sort()
        # return s_list == t_list

        # Use Hashmap, time O(n)
        if len(s) != len(t):
            return False
        s_dict = {}
        for c in s:
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        
        for c in t:
            if c not in s_dict or s_dict[c] <= 0:
                return False
            else:
                s_dict[c] -= 1
        
        return True


        
