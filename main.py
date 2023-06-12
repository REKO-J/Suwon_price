import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

print('Hi')
# 데이터 불러오기
# Jan = pd.read_csv('./data/경기도_수원시_물가동향_20230125.csv', encoding='cp949')
# Feb = pd.read_csv('./data/경기도_수원시_물가동향_20230228.csv', encoding='cp949')
# Mar = pd.read_csv('./data/경기도_수원시_물가동향_20230328.csv', encoding='cp949')
# Apr = pd.read_csv('./data/경기도_수원시_물가동향_20230428.csv', encoding='cp949')
# May = pd.read_csv('./data/경기도_수원시_물가동향_20230526.csv', encoding='cp949')

# # 데이터 병합
# suwon = pd.concat([Jan, Feb, Mar, Apr, May])

# # 데이터 결측치 처리
# suwon['물가동향'] = suwon['물가동향'].fillna(0)

# # 데이터 이상값 처리
# suwon[suwon['물가동향'] == '-'] = 0
# suwon[suwon['물가동향'] == ' - '] = 0

# # 데이터 타입 변경
# suwon['물가동향'] = suwon['물가동향'].astype('float')

# # 구별 짜장면 가격
# Gwonseon = suwon[suwon['시군구명'] == '권선구'].reset_index()
# Yeongtong = suwon[suwon['시군구명'] == '영통구'].reset_index()
# Jangan = suwon[suwon['시군구명'] == '장안구'].reset_index()
# Paldal= suwon[suwon['시군구명'] == '팔달구'].reset_index()
