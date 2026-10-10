class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        com = []
        for p, s in zip(position, speed):
            com.append((p, s))
        
        com.sort()
        
        for p, s in com[::-1]:
            t = (target - p) / s
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)

        return len(stack)