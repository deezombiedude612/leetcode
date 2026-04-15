class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        temp = ''.join(word1[i]+word2[i] for i in range(min_length))

        return temp + word1[min_length:] + word2[min_length:]


for w1, w2 in (
    ("abc", "pqr"),
    ("ab", "pqrs"),
    ("abcd", "pq"),
):
    print(Solution().mergeAlternately(w1, w2))
