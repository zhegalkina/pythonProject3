# new_list_1 = [int(i) for i in input().split()]
# new_list = [new_list_1[i] for i in range(1,len(new_list_1)) if new_list_1[i] > new_list_1[i-1]]
# print(new_list)


new_list_1 = [int(i) for i in input().split()]
print(max(new_list_1))
print(new_list_1.index(max(new_list_1)))