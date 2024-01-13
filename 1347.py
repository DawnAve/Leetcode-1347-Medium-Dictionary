class Solution:
    def minSteps(self, s: str, t: str) -> int:
        a = defaultdict(int)
        b = defaultdict(int)
        for i in range(len(s)):
                a[s[i]] += 1
                b[t[i]] += 1

        answer = 0
        temp = 0
        for i in a.keys():
            num = a[i] - b[i]
            answer += num if num >0 else 0
            
        return answer
