# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:44:15 2019

@author: M_Y

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

"""
def longestPalindrome(s):
    if len(s) == 0:
        return ""
    list11 = []
    list12 = []
    list21 = []
    list22 = []
    for i in range(len(s)):
        tempstr1 = s[i]
        tempstr2 = ""
        tempnum1 = 0
        tempnum2 = 0
        if i < len(s) - 1 - i:
            tempnum1 = i
        else:
            tempnum1 = len(s) - 1 - i
        if i < len(s) - 2 - i:
            tempnum2 = i
        else:
            tempnum2 = len(s) - 2 - i    
        #1:
        for j in range(1 , tempnum1 + 1):
            if s[i - j]==s[i + j]:
                tempstr1 = s[i - j] + tempstr1 + s[i + j]
            else:
                break
        #2:
        for k in range(tempnum2 + 1):
            if s[i - k] == s[i + k + 1]:
                tempstr2 = s[i - k] + tempstr2 + s[i + k + 1]
            else:
                break
        list11.append(tempstr1)
        list12.append(len(tempstr1))
        list21.append(tempstr2)
        list22.append(len(tempstr2))
    if max(list12) > max(list22):
        return list11[list12.index(max(list12))]
    else:
        return list21[list22.index(max(list22))]
    return 0

if __name__ == '__main__':
    print(longestPalindrome("ccc"))
    #print(len(a))