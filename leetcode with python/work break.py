# -*- coding:utf-8 -*-
def wordBreak(s, wordDict):
    if not s: return True
    if not wordDict: return False

    maxLength = self.getMaxLength(wordDict)
    cache = [False for i in range(len(s) + 1)]
    cache[0] = True

    for i in range(1, len(s) + 1):
        j = 1
        while j <= maxLength and j <= i:
            if not cache[i - j]:
                j += 1
                continue
            if s[i - j:i] in wordDict:
                cache[i] = True
                break
            j += 1
    return cache[len(s)]

def getMaxLength(dict):
    maxLength = 0
    for word in dict:
        maxLength = max(len(word), maxLength)
    return maxLength


# def wordBreak(s, wordDict):
#     """
#     :type s: str
#     :type wordDict: Set[str]
#     :rtype: bool
#     """
#     queue = [0]
#     ls = len(s)
#     lenList = [l for l in set(map(len, wordDict))]
#     visited = [0 for _ in range(0, ls + 1)]
#     while queue:
#         start = queue.pop(0)
#         for l in lenList:
#             if s[start:start + l] in wordDict:
#                 if start + l == ls:
#                     return True
#                 if visited[start + l] == 0:
#                     queue.append(start + l)
#                     visited[start + l] = 1
#     return False

s = Solution()
print s.wordBreak("leetcode",["leet", "code"])