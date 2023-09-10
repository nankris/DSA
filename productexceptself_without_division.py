
def productExceptSelf(nums):
    # left product calculation first
    # right product calculation second
    # Then multiple corresponding elements

    left_product = [1]
    left_prod = 1
    for i in range(len(nums)):
        left_prod = left_prod*nums[i]
        left_product.append(left_prod)
    left_product = left_product[:-1]
    
    print(left_product)    
    right_product = []
    right_prod = 1
    for k in nums[::-1]:
        right_prod = right_prod*k
        right_product.append(right_prod)
    right_product = right_product[:-1]
    right_product = right_product[::-1]
    right_product.append(1)
    print(right_product)
    
    for i in range(len(left_product)):
        left_product[i] = left_product[i]*right_product[i]

    return left_product

nums = [1,2,3,4]

print(productExceptSelf(nums))


