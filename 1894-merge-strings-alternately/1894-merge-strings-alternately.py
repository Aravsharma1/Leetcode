class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_str = [''] * (len(word1) + len(word2))
        p_1 = 0
        p_2 = 0
        p_turn = True
        counter_index = 0 
        while((p_1 != len(word1)) and (p_2 != len(word2))):
            if p_turn:
                final_str[counter_index] = word1[p_1]
                p_turn = False
                p_1 += 1
                counter_index += 1
            else:
                #final_str[counter_index].append(word2[p_2]) cant do this has to be like below:
                final_str[counter_index] = word2[p_2]
                p_turn = True
                p_2 += 1
                counter_index += 1
        #final_string = ''.join(final_str) # important technique
        if(len(word1) <= len(word2)): 
            # its less than equal because in the case len(w1) == len(w2), the lhs of and 
            # would cause the while loop to exit when p_1 exceeds the length of w1, so the 
            # w2 pointer would be left and this if block handles that case anyways. 
            while (p_2 != len(word2)):
                final_str[counter_index] = word2[p_2]
                counter_index += 1
                p_2 += 1
        else: 
            while (p_1 != len(word1)):
                final_str[counter_index] = word1[p_1]
                counter_index += 1
                p_1 += 1
        final_string = ''.join(final_str)
        return final_string
