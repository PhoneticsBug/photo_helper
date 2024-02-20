import os
import shutil
import tkinter as tk
from tkinter import filedialog

def monthmaker():
    month = []
    for i in range(1, 13):
        if i < 10:
            month.append(f'0{i}')
        else:
            month.append(str(i))
    return month

def create_year_folders():
    year = int(year_entry.get())
    location = filedialog.askdirectory(title="폴더를 생성할 위치를 선택하세요")
    if location:
        year_folder = os.path.join(location, str(year))
        try:
            os.mkdir(year_folder)
            result_label.config(text=f"폴더 '{year_folder}'가 생성되었습니다.")
        except FileExistsError:
            result_label.config(text=f"폴더 '{year_folder}'는 이미 존재합니다.")

def select_source_folder():
    source_folder = filedialog.askdirectory(title="옮길 파일이 있는 폴더를 선택하세요")
    source_folder_entry.delete(0, tk.END)
    source_folder_entry.insert(0, source_folder)

def select_dest_folder():
    dest_folder = filedialog.askdirectory(title="옮겨질 폴더를 선택하세요")
    dest_folder_entry.delete(0, tk.END)
    dest_folder_entry.insert(0, dest_folder)

def move_files():
    source_folder = source_folder_entry.get()
    dest_folder = dest_folder_entry.get()
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            shutil.move(source_file_path, dest_folder)
    result_label.config(text="파일 이동이 완료되었습니다.")

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("폴더 생성 및 파일 이동")

# 년도 입력
year_label = tk.Label(window, text="년도:")
year_label.grid(row=0, column=0)

year_entry = tk.Entry(window, width=30)
year_entry.grid(row=0, column=1)

# 폴더 생성 버튼
create_folder_button = tk.Button(window, text="폴더 생성", command=create_year_folders)
create_folder_button.grid(row=1, column=0, columnspan=2)

# 파일 이동 관련 위젯
source_folder_label = tk.Label(window, text="옮길 파일이 있는 폴더:")
source_folder_label.grid(row=2, column=0)

source_folder_entry = tk.Entry(window, width=50)
source_folder_entry.grid(row=2, column=1)

source_folder_button = tk.Button(window, text="폴더 선택", command=select_source_folder)
source_folder_button.grid(row=2, column=2)

dest_folder_label = tk.Label(window, text="옮겨질 폴더:")
dest_folder_label.grid(row=3, column=0)

dest_folder_entry = tk.Entry(window, width=50)
dest_folder_entry.grid(row=3, column=1)

dest_folder_button = tk.Button(window, text="폴더 선택", command=select_dest_folder)
dest_folder_button.grid(row=3, column=2)

move_files_button = tk.Button(window, text="파일 이동", command=move_files)
move_files_button.grid(row=4, column=0, columnspan=3)

result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=3)

window.mainloop()
