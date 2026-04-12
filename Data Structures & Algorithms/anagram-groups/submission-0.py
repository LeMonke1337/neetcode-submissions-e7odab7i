class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for string in strs:
            key = "".join(sorted(string))
            result.setdefault(key, []).append(string)
        return list(result.values())
        
        

        

