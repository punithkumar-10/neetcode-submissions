class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        a = ord("a")
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - a] += 1
            groups[tuple(count)].append(word)
        return list(groups.values())
