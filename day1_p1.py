f = open("test.txt", "r")
lines = f.readlines()
new_list = []
for val in lines:
    nums = ""
    for char in val:
        if char.isdigit():
            nums += char
    if len(nums) > 1:
        temp = nums[0] + nums[-1]
        new_list.append(int(temp))
    elif len(nums) == 0:
        new_list.append(0)
    else:
        temp = nums * 2
        new_list.append(int(temp))
print(new_list)
print(sum(new_list))
