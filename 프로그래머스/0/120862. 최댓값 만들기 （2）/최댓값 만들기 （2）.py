def solution(numbers):
    answer = 0
    nums = sorted(numbers)
    answer = max((nums[0]*nums[1]), (nums[-2]*nums[-1]))
    return answer