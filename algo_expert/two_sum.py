def two_sum(array, sum):
    print(sum)
    for i in array:
        print('-->', i)
        # diff_dict = {}
        # print('---',array[i])
        diff = array[i] - sum
        print('diff', diff)

nums = [3,4,2,5,3,2]
k = 8
two_sum(nums, k)
