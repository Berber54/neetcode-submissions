class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ''

        if strs == []:
            return 'none'

        for word in range(len(strs)):
            string += strs[word]
            if word < len(strs) - 1:
                string += '*#'
            
        return string

    def decode(self, s: str) -> List[str]:
        if s == 'none':
            return []
        
        return s.split('*#')