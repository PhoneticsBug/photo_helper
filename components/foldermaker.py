import os

def monthmaker():
    month = []
    for i in range(1, 13):
        if i < 10:
            month.append(f'0{i}')
        else:
            month.append(str(i))
    return month

def create_year_folders(year, location):
    year_folder = os.path.join(location, str(year))
    try:
        os.mkdir(year_folder)
        print(f"폴더 '{year_folder}'가 생성되었습니다.")
    except FileExistsError:
        print(f"폴더 '{year_folder}'는 이미 존재합니다.")

    months = monthmaker()
    for month in months:
        month_folder = os.path.join(year_folder, f"{year}.{month}")
        try:
            os.mkdir(month_folder)
            print(f"폴더 '{month_folder}'가 생성되었습니다.")
        except FileExistsError:
            print(f"폴더 '{month_folder}'는 이미 존재합니다.")

def create_folder(year, location):
    if year and location:
        create_year_folders(year, location)
