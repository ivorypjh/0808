#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[5]:


series1 = pd.Series([0, 1, 2, 3, 4, 5]) # 인덱스 없이 0, 1, 2, 3, 4, 5 로 접근하도록 생성
series2 = pd.Series([1, 2, 3, 4], index = ["one", "two", "three", "four"])
print(series1)
print(series2)

series3 = pd.Series({'7일':'해', "8일" : '해', '9일' : '비'}) # dict 를 가지고 Series 생성
print(series3) # key 가 인덱스, values 가 values 가 됨


# In[8]:


# 인덱싱
print(series3[2]) # 일련번호를 가지고 접근
print(series3['9일']) # 인덱스를 가지고 접근
print(series3[0:2]) # 인련번호는 뒤의 종료 번호가 범위에 포함되지 않음 - 7 ~ 8일이 출력
print(series3['7일':'9일']) # 인덱스는 종료 위치가 범위에 포함됨 - 7 ~ 9일이 출력


# In[13]:


# 연산

print(series1.values) # 값들(values)만 추출

# 연산은 ndarray 와 동일하게 수행되는데
# values 속성의 멤버를 가지고 연산
print(series1 + 20) # 20, 21 ... 25
print(series1.values + 20)

print(np.sum(series1)) # 15
print(np.cumsum(series1)) # 0 1 3 6 10 15


# In[19]:


ser1 = pd.Series({'7일' : 32, '8일' : 35, '9일' : 36, '10일' : 30})
ser2 = pd.Series({'7일' : np.nan, '9일' : 34, '8일' : 37, '10일' : 28})
print(ser1)
print(ser2)
# 순서대로 더하는게 아니라 인덱스(key)를 가지고 values를 연산
# 한 쪽이 NaN(Null)인 경우에는 결과도 NaN
print(ser1 + ser2)


# In[21]:


# DataFrame 을 만들기 위한 dict 생성
items = {
    'day' : ['7일', '8일', '9일', '10일'],
    'weather' : ['해', '해', '구름', '비'],
    'temp' : [34, 35, 32, 28]
}

# dict 를 사용해서 DataFrame 생성
DF = pd.DataFrame(items)
print(DF)

# 0, 1, 2, 3 은 index, day, weather, temp 는 columns


# In[23]:


print(DF.index)
print(DF.columns)

DF.index = range(1, 5) # 인덱스 1 ~ 4 로 변경
DF.columns = ['Date', 'Weather', 'Temp'] # columns 이름 변경
print(DF.index)
print(DF.columns)


# In[26]:


# head 나 tail 함수는 데이터가 제대로 불러졌는지 확인할 때 이용
# 전체를 불러오기에는 데이터가 너무 많은 경우 head 나 tail 을 통해 일부만 부름
print(DF.head(2)) # 7일과 8일
print(DF.tail(2)) # 9일과 10일

# 이 데이터를 머신러닝을 하려고 하면 numpy 의 ndarray 로만 가능함
print(type(DF.values)) # numpy.ndarray 클래스

# 데이터를 가져오면 분석을 하기 전에 데이터에 대한 정보를 확인해야 함
# RangeIndex 는 행의 갯수, columns 는 열의 갯수
# non-null count 에서 null 의 갯수를 알 수 있음 - 결측치 처리에 이용
DF.info()


# In[27]:


import os
print(os.getcwd())


# In[30]:


# 일반적으로 code 는 primary key 이지만 분석 대상이 아니므로
# 아래와 같이 index 로 옮길 수 있음
items = pd.read_csv('./data/item.csv', index_col = 'code')
print(items)


# In[33]:


# good.csv 파일은 첫번째 행도 컬럼이 아닌 일반 데이터이므로
# 첫번째 행이 헤더가 아니라고 설정한 다음 names 를 이용해서 헤더의 이름의 설정해줘야 함
goods = pd.read_csv('./data/good.csv', header = None, names = ['제품명', '개수', '가격'])
print(goods)


# In[35]:


# 2개씩 데이터를 읽어오도록 chunksize 를 지정
# goods 는 이전처럼 데이터 전체를 읽어오는게 아니라 TextFileReader 라는 객체를 갖게 됨
goods = pd.read_csv('./data/good.csv', header = None, chunksize = 2)
print(goods)
# 객체를 가지게 됐기 때문에 반복문을 사용해야 함
# 데이터를 2개씩 3번 읽어옴
for pieces in goods:
    print(pieces)
    print()


# In[37]:


gap = pd.read_csv('./data/gapminder.tsv', sep = '\t')
print(gap)


# In[40]:


elec = pd.read_csv('./data/한국전력거래소_시간별 전력수요량_20211231.csv', encoding = 'cp949')
print(elec)


# In[ ]:





# In[ ]:




