
#Given a string s consisting of words and spaces, return the length of the last word in the string.

#A word is a maximal substring consisting of non-space characters only.



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count_pre = 0
        count = 0
        for char in s:
            if char ==" ":
                if count !=0: count_pre = count
                count = 0
            else:
                count +=1
        if count !=0:
            return count
        else:
            return count_pre
    
  
#Input: s = "Hello World"
#Output: 5

s =Solution()

string = "Hello World"
target = 5 #Output: 5
print (s.lengthOfLastWord(string))
string = "   fly me   to   the moon  " #Output: 4
print (s.lengthOfLastWord(string))
string = "luffy is still joyboy" #Output: 6
print (s.lengthOfLastWord(string))