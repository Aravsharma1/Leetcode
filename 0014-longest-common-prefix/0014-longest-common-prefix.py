class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_string = ""
        dictionary = {}
        counter = 0
        
        if len(strs) == 1:
            return strs[0]

        for x in range(len(strs[0])):
            dictionary[counter] = strs[0][x]
            counter += 1
            in_dict = True  # Start as True and break if any mismatch

            for y in range(1, len(strs)):
                if x >= len(strs[y]) or strs[y][x] != dictionary[x]:
                    in_dict = False
                    break  # No need to check further if one string fails

            if in_dict:
                result_string += strs[0][x]
            else:
                break  # No more common prefix beyond this point

        return result_string

                    
        