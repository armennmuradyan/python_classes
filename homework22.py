#ex1


dict1 = {1:10, 2:20}
dict2={3:30, 4:40}
dict3={5:50,6:60}
dict4={7:70, 8:80}
list_of_dicts = [dict1, dict2, dict3, dict4]
for i in  list_of_dicts:
    dict1.update(i)
print(dict1)

#ex2 


num_ = int(input("tell me any number: "))
my_dictionary = {}
for i in range(1, num_ + 1):
    my_dictionary[i] = i*i
print(my_dictionary)    

#ex3

#ex4 

txt = str.split(input("enter any text\n"))
my_dict = {}
for i in txt:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)