def MajorityElement(nums):

    c_dict = {}
    major_element = 0
    for i in nums:
        if i not in c_dict:
            c_dict[i] = 1
        else:
            c_dict[i] += 1
    
    # print(c_dict)
    for key, value in c_dict.items():
        print(key, value, major_element)
        if value > major_element:
            key_val, major_element = key, value

    return key_val

nums = [2,2,1,1,1,2,2]
print(MajorityElement(nums))