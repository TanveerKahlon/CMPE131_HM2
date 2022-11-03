
def reverse_List(user_list):
    reverse = user_list[::-1]
    print('reverse list: ',reverse)

input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()

print('list: ', user_list)

for i in range(len(user_list)):
    user_list[i] = str(user_list[i])
    
reverse_List(user_list)


