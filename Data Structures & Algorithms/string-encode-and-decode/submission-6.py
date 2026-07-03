class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''
        if strs == []:
            return 'None'

        for s in range(len(strs)):
            for char in strs[s]:
                string += chr(ord(char) + 3)
            if s != len(strs) - 1:
                string += '*_'
        return string

    def decode(self, s: str) -> List[str]:
        spaces = s.split('*_')
        result = []
        if s == 'None':
            return result

        for code in spaces:
            word = ''
            for char in code:
                word += chr(ord(char) - 3)
            result.append(word)
        return result