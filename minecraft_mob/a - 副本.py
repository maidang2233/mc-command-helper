import os

folder_path = r'D:\我的世界相关\整合HTML\指令助手\minecraft_mob' 

for filename in os.listdir(folder_path):
    # .lower() 会把所有大写字母转为小写
    new_name = filename.lower()
    
    if new_name != filename:
        os.rename(os.path.join(folder_path, filename), 
                  os.path.join(folder_path, new_name))