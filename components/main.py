import tkinter as tk
from tkinter import filedialog
import foldermaker
import filemover

def create_folder():
    year = int(year_entry.get())
    location = filedialog.askdirectory()
    foldermaker.create_folder(year, location)

def move_files():
    source_folder = source_folder_entry.get()  # 수정된 부분: 옮길 파일이 있는 폴더 경로를 입력란에서 가져옴
    dest_folder = dest_folder_entry.get()      # 수정된 부분: 옮겨질 폴더 경로를 입력란에서 가져옴
    filemover.move_files(source_folder, dest_folder)

def select_source_folder():
    source_folder = filedialog.askdirectory()
    source_folder_entry.delete(0, tk.END)      # 수정된 부분: 기존 내용을 지우고 새로운 경로로 업데이트
    source_folder_entry.insert(0, source_folder)

def select_dest_folder():
    dest_folder = filedialog.askdirectory()
    dest_folder_entry.delete(0, tk.END)        # 수정된 부분: 기존 내용을 지우고 새로운 경로로 업데이트
    dest_folder_entry.insert(0, dest_folder)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("폴더 생성 및 파일 이동")

# 년도 입력
year_label = tk.Label(window, text="년도:")
year_label.grid(row=0, column=0)

year_entry = tk.Entry(window, width=30)
year_entry.grid(row=0, column=1)

# 폴더 생성 버튼
create_folder_button = tk.Button(window, text="폴더 생성", command=create_folder)
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
