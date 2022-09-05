# <예제 1-1> 딕셔너리 -> 시리즈 변환

# pandas 불러오기
import pandas as pd

# key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {"a": 1, "b": 2, "c": 3}

# 판다스 Series() 함수로 dictionary를 Series로 변환. 변수 sr에 저장
sr = pd.Series(dict_data)

# sr의 자료형 출력
print(type(sr))
print("\n")
# 변수 sr에 저장되어 있는 시리즈 객채를 출력
print(sr)

# <예제 1-2> 시리즈 인덱스

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)

# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)

# <예제 1-3> 시리즈 원소 선택

# 투플을 시리즈로 변환 (인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 원소를 1개 선택
print(sr[0]) # sr의 1번째 원소를 선택(정수형 위치 인덱스)
print(sr['이름']) # '이름' 라벨을 가진 원소를 선택(인덱스 이름)

# 여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]])
print('\n')
print(sr[['생년월일', '성별']])

# 여러 개의 원소를 선택(인덱스 범위 지정)
print(sr[1 : 2])
print('\n')
print(sr['생년월일' : '성별'])

# <예제 1-4> 딕셔너리 -> 데이터프레임 변환

# 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df))
print('\n')
# 변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)

# <예제 1-5> 행 인덱스/열 이름 설정

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index = ['준서', '예은'],
                  columns = ['나이', '성별', '학교'])

# 행 인덱스/열 이름 확인하기
print(df) # 데이터프레임
print('\n')
print(df.index) # 행 인덱스
print('\n')
print(df.columns) # 열 이름

# 행 인덱스/열 이름 변경하기
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df) # 데이터프레임
print('\n')
print(df.index) # 행 인덱스
print('\n')
print(df.columns) # 열 이름

# <예제 1-6> 행 인덱스/열 이름 변경

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                  index = ['준서', '예은'],
                  columns = ['나이', '성별', '학교'])

# 데이터프레임 df 출력
print(df)
print('\n')

# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns = {'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace = True)

# df의 행 인덱스 중에서, '준서'를 '학생1'로, '예은'을 '학생2'로 바꾸기
df.rename(index = {'준서':'학생1', '예은':'학생2'}, inplace = True)

# df 출력(변경 후)
print(df)