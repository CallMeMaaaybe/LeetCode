# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 19:44:15 2019

@author: M_Y
"""

def BigChildArray(inputlist):
    "--寻找最大子串--"
    Index = 0
    Allsum = 0
    Alllist =[]
    while Index < len(inputlist):
        #length = len(inputlist)
        SumElement = 0
        indexlist = []
        index = Index
        index2 = 0
        SumElement1 = 0 #第二个子串的
        indexlist1 = [] #第二个子串的
        #找到inputlist第一个及其后面几个大于0的元素的sum与index
        for index2 in range(index, len(inputlist)-1):
            if inputlist[index2] > 0:
                SumElement += inputlist[index2]
                indexlist.append(index2)
                Index += 1
                if inputlist[index2+1] < 0:
                    index2 += 1
                    for temp in range(index2, len(inputlist)-1):
                        Index = temp
                        if inputlist[temp]>0:
                            break
                    break
        #后面可以添加的元素
        for index1 in range(index2, len(inputlist)-1):
            SumElement1 += inputlist[index1]
            indexlist1.append(index1)
            if SumElement1 >= 0:
                if inputlist[index1+1] < 0:
                    SumElement += SumElement1
                    indexlist.extend(indexlist1)
                    SumElement1 = 0
                    indexlist1.clear()
        if SumElement > Allsum:
            Allsum = SumElement
            Alllist = indexlist
    return([Allsum,Alllist])
        
        #return [SumElement,indexlist]





if __name__ == "__main__":
    a = BigChildArray([-10,-9,23,1,1,2,-3,4,-6,9,-10])
    


'''
 def FirstArray(inputlist):
     
     for index in range(len(inputlist)):
        if inputlist[index] > 0:
            SumElement += inputlist[index]
            indexlist.append(index)
            if inputlist[index+1] < 0:
                index += 1
                break
     
               
    
    
    
    
    
    for index in range(len(inputlist)):#range(start,stop[,step])创建一个整数列表
        SumElement = 0
        indexlist = []
        #SumElement += inputlist[index]
        if inputlist[index] > 0:
            SumElement += inputlist[index]
            indexlist.append(index)
        else:
            SumElement = 0
            indexlist.clear()
'''   








         