import os
import shutil

# 获取桌面的路径（自动适配 Windows 和 Mac）
# 使用更智能的方法获取真实的桌面路径
try:
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
    desktop_path = winreg.QueryValueEx(key, 'Desktop')[0]
    desktop_path = os.path.expandvars(desktop_path)
except Exception:
    # 如果上面失败了，退回到原来的方法
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 定义各种文件类型对应的文件夹名
rules = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "文档": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "视频": [".mp4", ".mkv", ".avi", ".mov"],
    "音乐": [".mp3", ".wav", ".flac"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "代码": [".py", ".cpp", ".c", ".html", ".js", ".json", ".md"]
}

def organize_desktop():
    print("开始整理桌面...")
    # 遍历桌面上的所有文件
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        
        # 如果是文件夹，直接跳过
        if os.path.isdir(file_path):
            continue
            
        # 获取文件的后缀名（比如 .jpg）
        _, extension = os.path.splitext(filename)
        extension = extension.lower()
        
        # 防止脚本把自己给移走了
        if filename == os.path.basename(__file__):
            continue
            
        moved = False
        # 检查这个后缀属于哪个分类
        for folder_name, ext_list in rules.items():
            if extension in ext_list:
                target_folder = os.path.join(desktop_path, folder_name)
                # 如果没有这个文件夹，就新建一个
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                # 移动文件
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"已移动: {filename} -> {folder_name}文件夹")
                moved = True
                break
                
        # 如果没匹配上的文件，统一扔到“其他”文件夹
        if not moved and extension != "":
            target_folder = os.path.join(desktop_path, "其他")
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"已移动: {filename} -> 其他文件夹")

    print("桌面整理完成！✨")

if __name__ == "__main__":
    organize_desktop()