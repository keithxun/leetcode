class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd_map = {}
        even_map = {}

        for index, c in enumerate(s1):
            if index % 2 == 0:
                even_map[c] = even_map.get(c, 0) + 1
            else:
                odd_map[c] = odd_map.get(c, 0) + 1

        for index, c in enumerate(s2):
            if index % 2 == 0:
                even_map[c] = even_map.get(c, 0) - 1
            else:
                odd_map[c] = odd_map.get(c, 0) - 1

        return all(count == 0 for count in even_map.values()) and \
               all(count == 0 for count in odd_map.values())