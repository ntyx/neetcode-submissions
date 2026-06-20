class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappa = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - 97] += 1

            signature = tuple(count)
            mappa[signature].append(word)

        return list(mappa.values())
