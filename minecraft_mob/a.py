import os
import re

# 将路径改为你存放图片的文件夹路径
folder_path = r'D:\我的世界相关\整合HTML\指令助手\minecraft_mob' 

# 匹配规则：
# 1. ^\d+px-  匹配开头的像素值如 "480px-"
# 2. _[JB]E\d+ 匹配版本号如 "_JE2" 或 "_BE1"
# 3. (_[JB]E\d+)* 匹配可能出现多次的版本号
pattern = re.compile(r'^\d+px-|(_[JB]E\d+)+')

for filename in os.listdir(folder_path):
    # 执行替换，将匹配到的部分替换为空字符串
    new_name = re.sub(pattern, '', filename)
    
    if new_name != filename:
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # 防止重名冲突
        if not os.path.exists(new_file):
            os.rename(old_file, new_file)
            print(f'已重命名: {filename} -> {new_name}')

print("处理完成！")