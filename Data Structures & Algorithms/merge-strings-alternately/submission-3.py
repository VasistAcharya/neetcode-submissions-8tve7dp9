class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=[]
        
        for i in range(min(len(word1),len(word2))):
            final.append(word1[i])
            final.append(word2[i])
        
        final.append(word1[len(word2):])
        final.append(word2[len(word1):])

        output=(''.join(final))
        return output
