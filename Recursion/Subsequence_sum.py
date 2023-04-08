def sub_seq_sum(i,sub,nums,total):
    if i == len(nums):
        if sum(sub) == total:
            print(sub)
            return True #Prints only one subsequence    
        return False
    sub.append(nums[i])
    if (sub_seq_sum(i+1,sub,nums,total) is True):
        return True #We need return True whoever call.
    sub.pop()
    if (sub_seq_sum(i+1,sub,nums,total) is True):
        return True
    return False #None of the functions retuned true

sub_seq_sum(0,[],[1,2,1],2)
