'''
https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab
'''
class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here
        temp =''
        global_string = ''
        for l in range(len(S)-1,-1,-1):
            if S[l] == '.':
                global_string = global_string + temp[::-1] +'.'
                temp = ''
                continue
            temp = temp + S[l]
        global_string = global_string + temp[::-1]
        return global_string