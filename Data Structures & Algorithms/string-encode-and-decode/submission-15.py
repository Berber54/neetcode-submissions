class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return 'None'
        for s in range(len(strs)):
            for c in strs[s]:
                res += c
            if s != len(strs) - 1:
                res += '*_'

        return res

    def decode(self, s: str) -> List[str]:
        if s == 'None':
            return []
        return s.split('*_')