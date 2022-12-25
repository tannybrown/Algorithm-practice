class Solution(object):
    def buddyStrings(self, s, goal):
        if s[0] == goal[1] and s[1] == goal[0]:
            return True
        else :return False
