# -*- coding: utf-8 -*-
"""PredioSupesticioso.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b9AkOfkvMFWDnBQ33c--0yt_ul8J-G9M

Laço For
"""

for i in range(1, 21):
  if i == 13:
    continue
  print(i)

"""LAÇO WHILE"""

andar = 1

while(andar < 21):
  if (andar != 13):
    print(andar)
  andar = andar + 1

"""Laço For Decrescente"""

for i in range(20, 0, -1):
  if (i == 13):
    continue
  print(i)

"""Laço While Decrescente"""

andarDesc = 20

while(andarDesc > 0):
  if(andarDesc != 13):
    print(andarDesc)
  andarDesc = andarDesc - 1