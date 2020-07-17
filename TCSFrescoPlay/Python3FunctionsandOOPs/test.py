word_list = ['2', '3', '4', '4', '5', '5', '6', '6', '6', '7', '7', '7', '8', '8', '8', '8', '8',]
temp_list = []
for str1 in word_list:
    if word_list.count(str1) <= 3:
        temp_list.append(str1)
new_list = sorted(temp_list, key=temp_list.count, reverse=True)
unique_list = []
for x in new_list:
    # check if exists in unique_list or not
    if x not in unique_list:
        unique_list.append(x)
print(unique_list[-4:])
