#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.

def remove(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
    
      
def sherlockAndAnagrams(s):
    cnt = 0
    for i in range(1 ,len(s)) :
        for j in range(0 ,len(s)  ) :
            st = s[j: j+i]
            for k in range(j+1 , len(s)) :
                st1 = s[k : k+i]
                if(len(st) == len(st1)) :
                    if( st == st1 or st[::-1] == st1) :
                        cnt+=1
                    else :
                        chk = False 
                        for m in st :
                            chk = False 
                            for n in range(len(st1)) :
                                if(m == st1[n]) :
                                    chk = True 
                                    st1 = remove(st1 , n )
                                    break
                            if(not chk):
                                break 
                        if(chk) :
                            cnt += 1
                            
                                
                                
    return cnt 
                
                
                
            
            
            

if __name__ == '__main__':
   

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)
        print(result)
       