class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list_of_lists = []
        # my_map = {}
        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     if (sorted_word in my_map):
        #         my_map[sorted_word].append(word)
        #     my_map[sorted_word] = list(word)
        # for key in my_map:
        #     list_of_lists.append(my_map[key])
        # return list_of_lists
        my_dict = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            my_dict[sorted_word].append(word)
        return my_dict.values()
        
        