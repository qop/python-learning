#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# print absolute value of an interger
heightS = input('height(m): ')
weightS = input('weight(kg): ')
height = float(heightS)
weight = float(weightS)
bmi = weight/(height*height)
bmi = round(bmi, 2)

if bmi < 18.5:
    print('您的BMI是',bmi,'过轻')
elif bmi < 25:
    print('您的BMI是',bmi,'正常')
elif bmi < 28:
    print('您的BMI是',bmi,'过重')
elif bmi < 32:
    print('您的BMI是',bmi,'肥胖')
else:
    print('您的BMI是',bmi,'严重肥胖')