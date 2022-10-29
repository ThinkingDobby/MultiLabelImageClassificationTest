# 메모리 사용량 감당하기 어려움 - 주의해서 사용할 것
# 원래 비어있는 파일명도 있음 - 모든 파일을 생성하는 것은 권장하지 않음
# 대체  - 본문에 오류 파일 제외하고 DataFrame 구성하는 코드 추가함

import os
import shutil

dir_path = './data/movie_poster/images/'
base_file = dir_path + "3.jpg"

start = int(input("start: "))
end = int(input("end: "))

for i in range(start, end + 1):
    target_file = dir_path + str(i) + ".jpg"
    check = os.path.exists(target_file)

    if not check:
        shutil.copy(base_file, target_file)