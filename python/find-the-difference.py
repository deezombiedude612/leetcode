class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # while s:
        #     if s[0] in t:
        #         for i in range(len(t)):
        #             if t[i] == s[0]:
        #                 t = t[:i] + t[i+1:]
        #                 break
        #     s = s[1:]
        # return t

        ls, lt = sorted(s), sorted(t)
        for i in range(len(ls)):
            if ls[i] != lt[i]:
                return lt[i]

        return lt[-1]


for s, t in (
    ("abcd", "abcde"),
    ("", "y"),
    ("a", "aa"),
):
    print(Solution().findTheDifference(s, t))
