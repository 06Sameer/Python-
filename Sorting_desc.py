# Sort only multiples of 5 in descending order, keep others in place

class Solutions:
  def Five(nums):
    five= []

    for i in nums:
      if i%5 ==0:
        five.append(i)

    five.sort(reverse=True)

    j = 0

    for i in range(len(nums)):
        if nums[i]%5==0:
          nums[i] = five[j]
          j+=1

    return nums

obj = Solutions
obj.Five([1,5,12,17,25,55,13,35,60])
