class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        stack = []

        for p, s in pairs:
            t = (target-p)/s #time
            if not stack or stack[-1] < t:
                stack.append(t)
            
        return len(stack)
