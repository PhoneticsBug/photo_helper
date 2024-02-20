# python setup.py build 
# 위 커맨드를 실행하여 build 파일 생성

from cx_Freeze import setup, Executable

setup(
    name="File_n_Folder",
    version="1.0",
    description="this app makes making year and month folder easily and move files into them from dropbox camera upload",
    executables=[Executable("main.py")]
)
