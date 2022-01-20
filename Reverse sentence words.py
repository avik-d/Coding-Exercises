class Solution:
    def reverseWords(self, s: str) -> str:
        #First reverse the string
        #strip beginning spaces
        #strip ending spaces
        #Then reverse each word
        #At end of loop, reverse the last segment(word)
        
        #Reverse the string
        j = len(s)-1
        reversed_string = ""
        while(j>=0):
            reversed_string += s[j]
            j = j -1
        
        #Strip front spaces
        front_stripped_string = ""
        i = 0
        while (i<len(reversed_string)):
            if reversed_string[i] is " ":
                i = i + 1
            else:
                break;
        while(i<len(reversed_string)):
            front_stripped_string += reversed_string[i]
            i = i + 1
        
        #strip end spaces
        end_stripped_string = ""
        i=len(front_stripped_string)-1
        while i>=0:
            if front_stripped_string[i] is " ":
                i = i - 1
                continue
            else:
                break
        j = 0
        while j <= i:
            end_stripped_string += front_stripped_string[j]
            j = j + 1
        
        #Reverse each word
        i = 0
        j = 0
        next_start = 0
        final_string = ""
        
        while ((i<len(end_stripped_string)) and (j < len(end_stripped_string))):
            # Run until first space is encounterd
            # Then reverse from i to j
            if end_stripped_string[j] is " ":
                next_start = j + 1
                j = j - 1
                while (j >= i):
                    final_string += end_stripped_string[j]
                    j = j - 1
                    
                final_string += " "
                i = next_start
                j = next_start
                
                # Also skip if there are multiple spaces in between
                while (end_stripped_string[j]) is " ":
                    j = j + 1
                i = j
            else:
                j = j + 1
                
        # Reverse the last segment
        j = j - 1
        while(j >= i):
            final_string += end_stripped_string[j]
            j = j - 1
        return final_string
        
            
        
