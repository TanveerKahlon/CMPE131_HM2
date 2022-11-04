def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 
# Driver function
input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()

print('list: ', user_list)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

n = len(user_list)

pos1, pos2  = int ((n-1)/2) , (n-1)
 
print(swapPositions(user_list, pos1-1, pos2-1))