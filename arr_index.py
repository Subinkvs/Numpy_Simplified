nested_lst = [[1, 2, 3], [4, 5, 6], [9, 8, 10]]
# print(nested_lst[0][1] + nested_lst[1][0])

# nested_str = [['A', 'B', 'C'], ['D', 'E', 'F']]
# print(nested_str[0][0]+nested_str[1][0])


# print([ [j* 5  for j in nested_lst[0]], [j * 5 for j in nested_lst[1] ]])

# print([[j * 5 for j in rows]for rows in nested_lst])


new_lst = []
for i in range(len(nested_lst)):
    summ = 0
    for j in nested_lst:
        summ = summ + j[i]      
    new_lst.append(summ)
    

print(new_lst)






