class Solution:
    def lengthOfLongestSubstring(self, s):
        list1 = []
        max_len = 0

        for i in s:
            if i in list1:
                list1 = list1[list1.index(i) + 1:]

            list1.append(i)

            if len(list1) > max_len:
                max_len = len(list1)

        return max_len

        