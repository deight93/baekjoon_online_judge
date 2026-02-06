def solution(nums):
    counter = len(nums)/2

    nums = len(set(nums))

    answer = counter if nums >= counter else nums
    return int(answer)