import numpy as np

# 일차원 list 생성
li = list(range(1, 10))
print(li)

#list를 이용해서 ndarray 를 생성
ar = np.array(li)
print(ar)

# array를 만들고 구조를 변경(3x3)
matrix = np.array(li).reshape((3, 3))
print(matrix)

# 인덱싱 - 이차원 배열에서 데이터 1개 가져오기
# 모두 결과는 동일
data1 = matrix[0]
print(data1)
data2 = matrix[0, 0]
data3 = matrix[0][0]
print(data2)
print(data3)

# 이차원 배열에서 행 하나 찾아오기
row = matrix[0][:] # matrix[0][:], matrix[0]
print(row)

# 이차원 배열에서 열 하나 찾아오기
column = matrix[:][0] # matrix[:,0]
print(column)

# 일반 인덱싱한 데이터는 파이썬의 기본 데이터와 동일하게 동작
# 파이선의 scalar data는 일반적으로 immutable
# scalar data는 다른 변수에 대입할 때 값을 복사해서 대입함
a = 10
b = a # b = 10
b = 20
print(a) # 10

# 파이썬의 vector 데이터는 다른 변수에 대입할 때 참조를 복사해서 대입

ax = [1, 2, 3, 4]
bx = ax # bx = [1, 2, 3, 4] 의 참조를 대입
bx[0] = 10
print(ax) # [10, 2, 3, 4]