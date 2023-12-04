def majority_elements(nums):
    if not nums:
        return []

    candidate1, candidate2, count1, count2 = 0, 1, 0, 0

    # First pass to find the potential candidates
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass to verify the candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    n = len(nums)
    result = []
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# User input
nums_str = input("Enter the integer array separated by spaces: ")
nums = list(map(int, nums_str.split()))

# Call the function with user input
result = majority_elements(nums)
print("Elements that appear more than ⌊ n/3 ⌋ times:", result)
