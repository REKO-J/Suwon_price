import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#################### 데이터 ####################
# 데이터 불러오기
Jan = pd.read_csv('./data/경기도_수원시_물가동향_20230125.csv', encoding='cp949')
Feb = pd.read_csv('./data/경기도_수원시_물가동향_20230228.csv', encoding='cp949')
Mar = pd.read_csv('./data/경기도_수원시_물가동향_20230328.csv', encoding='cp949')
Apr = pd.read_csv('./data/경기도_수원시_물가동향_20230428.csv', encoding='cp949')
May = pd.read_csv('./data/경기도_수원시_물가동향_20230526.csv', encoding='cp949')

# 데이터 병합
Suwon = pd.concat([Jan, Feb, Mar, Apr, May])

# 데이터 결측치 처리
Suwon['물가동향'] = Suwon['물가동향'].fillna(0)

# 데이터 이상값 처리
Suwon[Suwon['물가동향'] == '-'] = 0
Suwon[Suwon['물가동향'] == ' - '] = 0

# 데이터 타입 변경
Suwon['물가동향'] = Suwon['물가동향'].astype('float')

# 구별로 저장
Gwonseon = Suwon[Suwon['시군구명'] == '권선구'].reset_index()
Yeongtong = Suwon[Suwon['시군구명'] == '영통구'].reset_index()
Jangan = Suwon[Suwon['시군구명'] == '장안구'].reset_index()
Paldal= Suwon[Suwon['시군구명'] == '팔달구'].reset_index()

################################################
# title
st.title('수원시 물가 한눈에!')

# header
st.header('짜장면 가격')

# selectbox
option = st.selectbox('구를 선택하세요',
                      ('권선구', '영통구', '장안구', '팔달구'))

st.write('선택:', option)

if option == '권선구':
  # 짜장면 최대, 최소 가격
  st.write('==================== 권선구 ====================')
  st.write('권선구 짜장면의 최대 가격은', Gwonseon.loc[Gwonseon[Gwonseon['품목'] == '짜장면']['물가동향'].idxmax()]['기준일'], '의',
           Gwonseon.loc[Gwonseon[Gwonseon['품목'] == '짜장면']['물가동향'].idxmax()]['물가동향'], '원 입니다.')
  st.write('권선구 짜장면의 최저 가격은', Gwonseon.loc[Gwonseon[Gwonseon['품목'] == '짜장면']['물가동향'].idxmin()]['기준일'], '의',
           Gwonseon.loc[Gwonseon[Gwonseon['품목'] == '짜장면']['물가동향'].idxmin()]['물가동향'], '원 입니다.')

  # 짜장면 가격 변동 추이
  x = Gwonseon[Gwonseon['품목'] == '짜장면']['물가동향']
  y = Gwonseon[Gwonseon['품목'] == '짜장면']['기준일']

  st.write(len(x))
  st.write(len(y))
  
  chart_data = pd.DataFrame(x)
  st.line_chart(chart_data)

elif option == '영통구':
  st.write('==================== 영통구 ====================')
  st.write('영통구 짜장면의 최대 가격은', Yeongtong.loc[Yeongtong[Yeongtong['품목'] == '짜장면']['물가동향'].idxmax()]['기준일'], '의',
           Yeongtong.loc[Yeongtong[Yeongtong['품목'] == '짜장면']['물가동향'].idxmax()]['물가동향'], '원 입니다.')
  st.write('영통구 짜장면의 최저 가격은', Yeongtong.loc[Yeongtong[Yeongtong['품목'] == '짜장면']['물가동향'].idxmin()]['기준일'], '의',
           Yeongtong.loc[Yeongtong[Yeongtong['품목'] == '짜장면']['물가동향'].idxmin()]['물가동향'], '원 입니다.')

elif option == '장안구':
  st.write('==================== 장안구 ====================')
  st.write('장안구 짜장면의 최대 가격은', Jangan.loc[Jangan[Jangan['품목'] == '짜장면']['물가동향'].idxmax()]['기준일'], '의',
           Jangan.loc[Jangan[Jangan['품목'] == '짜장면']['물가동향'].idxmax()]['물가동향'], '원 입니다.')
  st.write('장안구 짜장면의 최저 가격은', Jangan.loc[Jangan[Jangan['품목'] == '짜장면']['물가동향'].idxmin()]['기준일'], '의',
           Jangan.loc[Jangan[Jangan['품목'] == '짜장면']['물가동향'].idxmin()]['물가동향'], '원 입니다.')

elif option == '팔달구':
  st.write('==================== 팔달구 ====================')
  st.write('팔달구 짜장면의 최대 가격은', Paldal.loc[Paldal[Paldal['품목'] == '짜장면']['물가동향'].idxmax()]['기준일'], '의',
           Paldal.loc[Paldal[Paldal['품목'] == '짜장면']['물가동향'].idxmax()]['물가동향'], '원 입니다.')
  st.write('팔달구 짜장면의 최저 가격은', Paldal.loc[Paldal[Paldal['품목'] == '짜장면']['물가동향'].idxmin()]['기준일'], '의',
           Paldal.loc[Paldal[Paldal['품목'] == '짜장면']['물가동향'].idxmin()]['물가동향'], '원 입니다.')
        
# 짜장면 지수
Suwon_Jan = Suwon[Suwon['품목'] == '짜장면'].reset_index()[0:12]
Suwon_Feb = Suwon[Suwon['품목'] == '짜장면'].reset_index()[12:24]
Suwon_Mar = Suwon[Suwon['품목'] == '짜장면'].reset_index()[24:36]
Suwon_Apr = Suwon[Suwon['품목'] == '짜장면'].reset_index()[36:48]
Suwon_May = Suwon[Suwon['품목'] == '짜장면'].reset_index()[48:60]
      
x = [Suwon_Jan.loc[Suwon_Jan['물가동향'].idxmax()]['물가동향'],
     Suwon_Feb.loc[Suwon_Feb['물가동향'].idxmax()]['물가동향'],
     Suwon_Mar.loc[Suwon_Mar['물가동향'].idxmax()]['물가동향'],
     Suwon_Apr.loc[Suwon_Apr['물가동향'].idxmax()]['물가동향'],
     Suwon_May.loc[Suwon_May['물가동향'].idxmax()]['물가동향']]
y = np.arange(1, 6)

chart_data = pd.DataFrame(x, y)
st.bar_chart(chart_data)
