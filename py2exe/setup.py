from distutils.core import setup
import py2exe

setup(
    console=['main.py'],  # main.py를 콘솔 응용 프로그램으로 지정
    options={'py2exe': {'bundle_files': 1}},  # 실행 파일을 하나의 파일로 묶음
    zipfile=None  # 묶음 파일이 아닌 별도의 디렉토리에 저장
)

# https://github.com/py2exe/py2exe/blob/master/README.md 
# 위 코드 참조해서 하나의 파일로 컴파일되게 + 추후 버전에서도 사용 가능하게 수정할 것