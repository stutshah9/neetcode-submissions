class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []  # pairs of temp,index since there might be duplicate temps

        for i, temp, in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                poppedT, poppedI = stack.pop()
                answer[poppedI] = i - poppedI
            stack.append((temp, i))
        return answer
        