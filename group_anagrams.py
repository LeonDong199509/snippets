class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sort solution, Time O(nmlogm), Space O(nm)
        # strs_sorted = []
        # for s in strs:
        #     s = [c for c in s]
        #     s.sort()
        #     strs_sorted.append("".join(s))
        
        # index_dict = {}
        # for i, s in enumerate(strs_sorted):
        #     if s in index_dict:
        #         index_dict[s].append(i)
        #     else:
        #         index_dict[s] = [i]
        
        # result = []
        # for index_list in index_dict.values():
        #     result.append([strs[i] for i in index_list])
        
        # return result

        # ASCII with 26 letters list solution (For English only)
        # Time complexity O(mn), Space O(mn)
        hash_mapping = {}

        for s in strs:
            letters = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                letters[index] += 1
            letters_tuple = tuple(letters)
            if letters_tuple in hash_mapping:
                hash_mapping[letters_tuple].append(s)
            else:
                hash_mapping[letters_tuple] = [s]
 
        return list(hash_mapping.values())
        
