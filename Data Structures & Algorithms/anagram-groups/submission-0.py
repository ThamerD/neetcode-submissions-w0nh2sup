class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i, x in enumerate(strs):
            letters = [0] * 26

            for char in x:
                letters[ord(char)-97] += 1

            letters = tuple(letters)
            
            if letters in result:
                result[letters].append(x)
            else:
                result[letters] = [x]
        
        return list(result.values())