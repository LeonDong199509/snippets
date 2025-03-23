class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Hashmap
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        
        mapping_1 = {}
        mapping_2 = {}
        for i, word in enumerate(s_list):
            if pattern[i] not in mapping_1:
                mapping_1[pattern[i]] = word
            else:
                if mapping_1[pattern[i]] != word:
                    return False
            if word not in mapping_2:
                mapping_2[word] = pattern[i]
            else:
                if mapping_2[word] != pattern[i]:
                    return False

        return True
