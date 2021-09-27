#ex2

my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
res = []
for i in my_list:
	if i not in res:
		res.append(i)
print(my_list)		
print(res)

#ex3

my_list_1 = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
res_1 = []
for i in my_list_1:
	if type(i) == list:
		for j in i:
			res_1.append(j)
	elif type(i) != list:
		res_1.append(i)
print(res_1)		

#ex4

my_list_2 = [1, 1, 2, 3, 4, 4, 5, 1] # two part
a = my_list_2[:3]		#first list, lenght = 3
b = my_list_2[3:]		#second list 
res = (a,b)
print(res)