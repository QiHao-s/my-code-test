import os
import shutil

# 智能获取桌面路径
try:
    import winreg
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
    desktop_path = winreg.QueryValueEx(key, 'Desktop')[0]
    desktop_path = os.path.expandvars(desktop_path)
except Exception:
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# 分类规则
rules = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "文档": [".doc", ".docx", ".pdf", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "视频": [".mp4", ".mkv", ".avi", ".mov"],
    "音乐": [".mp3", ".wav", ".flac"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "代码": [".py", ".cpp", ".c", ".html", ".js", ".json", ".md"]
}

def organize_desktop():
    print(f"当前正在整理的桌面路径是: {desktop_path}")
    print("开始整理桌面...")
    
    # 遍历桌面上的所有文件
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)
        
        # 1. 如果是文件夹，直接跳过
        if os.path.isdir(file_path):
            continue
            
        # 2. 防止脚本把正在运行的自己给移走了
        if filename == os.path.basename(__file__):
            continue

        # 3. 获取文件的后缀名，并转小写
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # 4. 跳过快捷方式和网页链接（绝不乱动你的图标）
        if extension in [".lnk", ".url"]:
            continue

        # 5. 开始按规则归类
        moved = False
        for folder_name, ext_list in rules.items():
            if extension in ext_list:
                target_folder = os.path.join(desktop_path, folder_name)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"已移动: {filename} -> {folder_name}文件夹")
                moved = True
                break
                
        # 6. 没匹配上的文件扔进“其他”
        if not moved and extension != "":
            target_folder = os.path.join(desktop_path, "其他")
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            shutil.move(file_path, os.path.join(target_folder, filename))
            print(f"已移动: {filename} -> 其他文件夹")

    print("桌面整理完成！✨")

if __name__ == "__main__":
    organize_desktop()