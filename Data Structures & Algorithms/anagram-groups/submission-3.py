class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            hash[key].append(word)
        return list(hash.values())
