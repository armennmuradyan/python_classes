import os

user_input = input('do you want to delete folder a and all folders in a? yes for yes \n')
if user_input == 'yes':
   cwd = os.getcwd()
   list_cwd = os.listdir(cwd)
   for i in list_cwd:
      if os.path.isdir(os.path.join(cwd, i)):
         cwd_1 = cwd + "\\{}".format(i)
         list_cwd_1 = os.listdir(cwd_1)
         cwd_2 = cwd_1 + f'\\{list_cwd_1[1]}'  
         list_cwd_2 = os.listdir(cwd_2)
         cwd_3 = cwd_2 + f'\\{list_cwd_2[0]}'
         cwd_b = cwd_1 +'\\b'
         os.rmdir(cwd_3)
         os.rmdir(cwd_2)
         os.rmdir(cwd_b)
         os.rmdir(cwd_1)