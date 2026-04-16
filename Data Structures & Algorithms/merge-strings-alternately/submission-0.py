class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=[]
        i=0
        for i in range(min(len(word1),len(word2))):
            final.append(word1[i])
            final.append(word2[i])
        
        if len(word1)>len(word2):
            for i in range(len(word2),len(word1)):
                final.append(word1[i])
        else:
            for i in range(len(word1),len(word2)):
                final.append(word2[i])
                
        output=(''.join(final))
        return output
