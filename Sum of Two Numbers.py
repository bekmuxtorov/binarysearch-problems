"""
@user: Asadbek Muxtorov
Sum of Two Numbers

@problem: Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. You may not use the same element twice.
@link: https://binarysearch.com/problems/Sum-of-Two-Numbers

@status: easy

"""
def solve(nums: list[int], k: int) -> bool:
    if len(nums) == 1:
        return False

    # for i in range(len(nums)):
    #     for j in range(len(nums)-1):
    #         if nums[i] + nums[j] == k:
    #             return True
    #
    # return  False
    for i in range(len(nums)):
        if (k - nums[i]) in nums:
            nums.remove(nums[i])
            return True

    return False





nums = [35, 8, 18, 3, 22]
k = 11
print(solve(nums,k))