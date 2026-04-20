class Solution:

    def encode(self, strs: List[str]) -> str:

        size = str(len(strs))
        str_lengths = ""
        words = ""

        for string in strs:
            str_lengths += "#"
            str_lengths += str(len(string))
            words += string
            
        print(size + str_lengths + '#' + words)
        return size + str_lengths + '#' + words

    def decode(self, s: str) -> List[str]:
        if len(s) < 3:
            return []
        size_code = ""
        lengths = []

        i = 0
        while i < len(s) and s[i] != '#':
            size_code += s[i]
            i += 1
        
        size = int(size_code)

        for i in range(len(s)):
            if s[i] == '#':
                code = ""
                i += 1
                while i < len(s) and s[i] != '#':
                    code += s[i]
                    i += 1
                
                lengths.append(int(code))
                if len(lengths) == size:
                    break
        
        # print(size)
        # print(lengths)
        # print(i)
        # print(s)

        result = []

        z = 0
        i += 1
        while len(result) < size:
            word = ""
            for k in range(lengths[z]):
                word += s[i]
                i += 1
            result.append(word)
            z += 1
            
        return result