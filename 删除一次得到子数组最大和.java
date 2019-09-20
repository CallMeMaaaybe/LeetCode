# -*- coding: utf-8 -*-
/*
******************************************************************
Created on Fri Sep 13 19:44:15 2019

@author: M_Y

给你一个整数数组，返回它的某个 非空 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从原数组中
选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总
和是所有子数组之中最大的。注意，删除一个元素后，子数组 不能为空。

来源：力扣（LeetCode）

链接：https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion

著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
******************************************************************
*/

class Solution {
    public int maximumSum(int[] arr) {
        int len = arr.length;
        int[] f = new int[len];
        int[] g = new int[len];
        f[0] = arr[0];
        g[0] = -200001;
        for(int i=1;i<len;i++){
            f[i] = Math.max(f[i-1]+arr[i],arr[i]);//其实就是f(i-1)是否<0
            g[i] = Math.max(g[i-1]+arr[i],f[i-1]);
        }
        int res = Integer.MIN_VALUE; 
        for(int i=0;i<len;i++){
            res = Math.max(res,Math.max(f[i],g[i]));
        }
        return res;
    }
}