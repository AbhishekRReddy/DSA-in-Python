def sub_seq_sum(i,sub,nums,total):
    if i == len(nums):
        if sum(sub) == total:
            print(sub)
            return
        return
    sub.append(nums[i])
    sub_seq_sum(i+1,sub,nums,total)
    sub.pop()
    sub_seq_sum(i+1,sub,nums,total)

sub_seq_sum(0,[],[1,2,1],2)