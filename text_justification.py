class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        # Time O(nm), Space O(nm)
        output = [[]]
        line_length = [0]
        current_length = 0
       
        # Get words for each line first
        for word in words:
            current_length += len(word)
            if current_length <= maxWidth:
                output[-1].append(word)
                line_length[-1] += len(word)
                # Add a space here
                current_length += 1
            else:
                output.append([word])
                line_length.append(len(word))
                current_length = len(word) + 1


        result = []
        # Add extra spaces to ech line
        for j, line in enumerate(output):
            line_str = ""
            # Not last line
            if j != len(output) -1:
                # Total slots in current line
                slots = len(line) - 1
                # Edge case where there is only one word for current line
                if slots == 0:
                    line_str += line[0]
                    line_str += " " * (maxWidth - len(line_str))
                    result.append(line_str)
                    continue

                # Total spaces in current line
                spaces = maxWidth - line_length[j]
                # Evenly assign spaces to each slots first
                space_per_slot = spaces // slots
                # Get how many left after evenly assigning
                remaining = spaces % slots
                for i, word in enumerate(line):
                    line_str += word
                    # It it's the last word, push it to the result
                    if i == len(line)-1:
                        result.append(line_str)
                    # Otherwise add spaces
                    else:
                        # Add even spaces
                        line_str += " " * space_per_slot
                        # Add one more space if the index smaller then remaining spaces after evenly assigning
                        if i < remaining:
                            line_str += " "
            # Special handling for last line
            else:
                for i, word in enumerate(line):
                    line_str += word
                    if i == len(line)-1:
                        line_str += " " * (maxWidth - len(line_str))
                    else:
                        line_str += " "
                result.append(line_str)
        
        return result



