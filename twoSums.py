
def twoSum(nums, target):

    out = [0, 0]
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                out = [i, j]
    return out


def testing(test, answer):
    out = []
    for i in test:
        out.append(twoSum(i[0], i[1]))
    print out
    print answer
    return (out == answer)


# Testing
test1 = [[0, 3, 4, 5, 6], 3]
test2 = [[4, 3, 5, 10, 14], 8]
test3 = [[1, 6, 10, 12, 45], 7]
test4 = [[54, 6, 3, 1], 55]
test = [test1, test2, test3, test4]
ans1 = [0, 1]
ans2 = [1, 2]
ans3 = [0, 1]
ans4 = [0, 3]
ans = [ans1, ans2, ans3, ans4]

rval = testing(test, ans)
print rval
