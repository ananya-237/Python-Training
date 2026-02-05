nums= [1, 2, 3, 4]
n = len(nums)
ans = [1] * n
for i in range(1, n):
    ans[i] = ans[i - 1] * nums[i - 1]

    suffix = 1
    for j in range(n - 2, -1, -1):
        suffix = nums[j + 1] * suffix
        ans[j] = ans[j] * suffix
    print(ans)