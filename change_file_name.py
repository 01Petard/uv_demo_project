# /// script
# requires-python = ">=3.13"
# dependencies = ["requests"]
# ///


import os

def rename_files(directory):
    # 遍历指定目录下的所有文件和子目录
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # 确保是文件而不是目录
        if os.path.isfile(file_path):
            # 查找第一个下划线的位置
            underscore_pos = filename.find('_')
            if underscore_pos != -1:
                # 截取 "_" 之后的内容
                new_filename = filename[underscore_pos + 1:]
                new_file_path = os.path.join(directory, new_filename)

                # 重命名文件
                os.rename(file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
            else:
                print(f"Skipped (no '_'): {filename}")

# 使用示例
if __name__ == "__main__":
    target_directory = "/Volumes/love/Doujinshi/kcccc/退魔美肉妖狐 & 美月IF篇/退魔美肉妖狐part15-CG/"  # 替换为你的目标文件夹路径
    rename_files(target_directory)