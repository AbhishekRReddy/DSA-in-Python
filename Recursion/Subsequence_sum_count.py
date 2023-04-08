def subseq(i,nums,subsq,total):
    if i == len(nums):
        if sum(subsq) == total:
            return 1
        return 0
    subsq.append(nums[i])
    l = subseq(i+1, nums, subsq, total)
    subsq.pop()
    r = subseq(i+1, nums, subsq,total)
    return l+r

print(subseq(0,[1,2,1],[],2))
