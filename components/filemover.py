import os
import shutil

def move_files_by_year_month(source_folder, dest_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.jpg'):  # 이동할 파일 확장자 설정
                year_month = file.split('.')[0]  # 파일 이름에서 "연도-월" 부분 추출
                source_file_path = os.path.join(root, file)
                dest_folder_path = os.path.join(dest_folder, year_month)

                # 연도-월에 해당하는 폴더가 없다면 생성
                if not os.path.exists(dest_folder_path):
                    os.makedirs(dest_folder_path)

                # 파일 이동
                shutil.move(source_file_path, dest_folder_path)

def move_files(source_folder, dest_folder):
    if source_folder and dest_folder:
        move_files_by_year_month(source_folder, dest_folder)
        print("파일 이동이 완료되었습니다.")
