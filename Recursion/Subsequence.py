'''
TC will be 2^n where n is number of elements in given array
For every element we will be having two choices, that is to take it or not take it.
So 2^N 
'''

def subsequence(index, sub_seq,nums):
    if index == len(nums):
        print(sub_seq)
        return
    sub_seq.append(nums[index])
    subsequence(index+1, sub_seq, nums)
    sub_seq.remove(nums[index])
    subsequence(index+1, sub_seq, nums)

nums= [3,1,2]
my_list=[]
subsequence(0, my_list, nums)