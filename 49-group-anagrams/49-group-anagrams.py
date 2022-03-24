class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_dict = dict()
        
        for srt in strs:
            srt_sorted = "".join(sorted(srt))
            if srt_sorted not in map_dict:
                map_dict[srt_sorted] = list()
            map_dict[srt_sorted].append(srt)
        
        res_list = list()
        
        return map_dict.values()