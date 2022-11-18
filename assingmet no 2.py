#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Given a string str, your task is to write a program which takes a string str as its only input and returns 
#an integer denoting the no of palindromic subsequence (need not necessarily be distinct) which could be formed 
#from the string str.

#Input Format:

#The first and only line of input contains string str.

#Output Format:

#The output will be an integer denoting the no of palindromic subsequence which could be formed from the string str.

#Sample Input :

#abcdef

#Sample Output :

#6

#Explanation:

#For string 'abcdef' palindromic subsequence are : "a" ,"b", "c" ,"d","e","f"


def countP_subs(sub_str, sub_str_2, s):

    if (sub_str > sub_str_2):
        #    Invalid substring.
        return 0

    if (sub_str == sub_str_2):
        #    Every single character in the string is a palindrome itself.
        return 1

    elif (s[sub_str] == s[sub_str_2]):
        return (1 + countP_subs(sub_str + 1, sub_str_2, s) + countP_subs(sub_str, sub_str_2 - 1, s))
    else:
        return ((countP_subs(sub_str + 1, sub_str_2, s) + countP_subs(sub_str, sub_str_2 - 1, s))- countP_subs(sub_str + 1, sub_str_2 - 1, s))
def countP_subs1(s):

    return countP_subs(0, len(s) - 1, s)

countP_subs1("ancdef")

