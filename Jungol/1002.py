def GCD(x, y) :
    if(y==0) : 
        return x
    else : 
        return GCD(y, x%y)

count_num = int(input())
input_nums = list(map(int, input().split(' ', count_num)))
print(input_nums)

# 첫번째 방법
MEM_1 = input_nums.copy()
# 두번째 방법
MEM_2 = input_nums[:]
print(MEM_1)
LSM = 1

for i in range(0, count_num-1) :
    MEM_1[i] = GCD(MEM_1[i], MEM_1[i+1])

print(input_nums)
print('%d %d' %(MEM_1[count_num-1], LSM))
