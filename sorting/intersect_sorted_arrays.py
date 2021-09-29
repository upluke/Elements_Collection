# 13.1
# brute-force algorithms 
# time:O(mn) where m and n be the lengths of the two input arrays

def intersect_two_sorted_arrays(A, B):
  # res=[]
  # for i, a in enumerate(A): 
  #     if (i==0 or a!=A[i-1]) and a in B:
  #         res.append(a)
  # return res
  return [a for i, a in enumerate(A) if (i==0 or a!=A[i-1]) and a in B]
 

print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10])) # 5,6,8


# make some optimizations: iterate through the first array and use binary search in array to test if the element is present in the second array
# time:O(m log n), where m is the length of the array being iterated over. we can further imporve our run time by choosing the shorter array for the outer llop since if n i smuch smaller than m, then n log(m) is much smaller than m log(n)
import bisect

def intersect_two_sorted_arrays(A, B):
   def is_present(k):
     i=bisect.bisect_left(B,k)
     return i<len(B) and B[i]==k

   return [
     a for i, a in enumerate(A) if (i==0 or a !=A[i-1]) and is_present(a) 
   ]

print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10])) # 5,6,8


#however the previous solution is not the best when the array lengths are similar bc we're not exploiting the fact that both arrays are sorted. We can achieve linear runtime by simultaneously advancing through the two input arrays in increasing order.
# time: O(m+n)

def intersect_two_sorted_arrays(A, B):
  i, j , res=0,0,[]
  while i<len(A) and j <len(B):
    if A[i]== B[j]:
      if i==0 or A[i]!=A[i-1]:
        res.append(A[i])
      i,j=i+1, j+1
    elif A[i]<B[j]:
      i+=1
    else: # A[i]>B[j]
      j+=1
  return res

print(intersect_two_sorted_arrays([2,3,3,5,5,6,7,7,8,12],[5,5,6,8,8,9,10,10])) # 5,6,8