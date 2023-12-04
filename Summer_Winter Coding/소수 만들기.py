def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                for n in range(2, int(num**0.5) + 1):
                    if num % n == 0:
                        break
                else:
                    answer += 1
    return answer
