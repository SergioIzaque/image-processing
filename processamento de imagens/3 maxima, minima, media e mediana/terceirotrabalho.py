# -*- coding: utf-8 -*-
"""terceirotrabalho.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TictOJgrKU1BxRu184aiXZ853OLGZxe0
"""

import numpy as np
import cv2
import os

"""importanto as bibliotecas necessárias para o funcionamento do código."""

from google.colab import files
uploaded = files.upload()
for fn in uploaded.keys():
  print('Arquivo carregador("name") com tamanho de (length) bytes'.format(name=fn, length=len(uploaded[fn])))

"""aqui importa a imagem diretamente do google colab.

"""

filename = next(iter(uploaded))
print(filename)

"""aqui guarda a imagem e mostra o nome dela.

"""

from matplotlib import pyplot as plt
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)

"""aqui apresenta a imagem original"""

x = img.shape [0]
y = img.shape [1]
z = img.shape [2]

img1 = np.zeros((x,y), dtype = np.uint8)

for a in range(0,x-1):
  for b in range(0,y-1):
    for c in range(0,z):
      img_vetor = [img[a,b,c]*1, img[a+1,b,c]*1, img[a,b+1,c]*1, img[a+1,b+1,c]*1, img[a-1,b,c]*1, img[a,b-1,c]*1, img[a-1,b-1,c]*1, img[a+1,b-1,c]*1, img[a-1,b+1,c]*1]
      img_minima = img_vetor[0]
      for l in range(0,9):
        if(img_vetor[l]<img_minima):
          img_minima = img_vetor[l]

      img1[a,b] = img_minima

plt.imshow(img1, cmap='gray')

"""aqui aplica o filtro de minima, que retira os pixels brancos e dá ênfase nos pretos.
isso ocorre pois o valor de cada pixel é substituído pelo menor valor dentre os valores de intensidade dos pixels ao redor.
"""

x = img.shape [0]
y = img.shape [1]
z = img.shape [2]

img2 = np.zeros((x,y), dtype = np.uint8)

for a in range(0,x-1):
  for b in range(0,y-1):
    for c in range(0,z):
      img_vetor = [img[a,b,c]*1, img[a+1,b,c]*1, img[a,b+1,c]*1, img[a+1,b+1,c]*1, img[a-1,b,c]*1, img[a,b-1,c]*1, img[a-1,b-1,c]*1, img[a+1,b-1,c]*1, img[a-1,b+1,c]*1]
      img_maxima = img_vetor[0]
      for l in range(0,9):
        if(img_vetor[l]>img_maxima):
          img_maxima = img_vetor[l]

      img2[a,b] = img_maxima

plt.imshow(img2, cmap='gray')

"""aqui aplica o filtro de máxima, que retira os pixels pretos e dá ênfase nos brancos.
isso ocorre pois o valor de cada pixel é substituído pelo maior valor dentre os valores de intensidade dos pixels ao redor.
"""

x = img.shape [0]
y = img.shape [1]
z = img.shape [2]

img3 = np.zeros((x,y), dtype = np.uint8)

for a in range(0,x-1):
  for b in range(0,y-1):
    for c in range(0,z):
      img_vetor = [img[a,b,c]*1, img[a+1,b,c]*1, img[a,b+1,c]*1, img[a+1,b+1,c]*1, img[a-1,b,c]*1, img[a,b-1,c]*1, img[a-1,b-1,c]*1, img[a+1,b-1,c]*1, img[a-1,b+1,c]*1]

      soma = 0

      for i in range(0,9):
        soma = soma + img_vetor[i]

      media = soma/9

      img3[a,b] = media

plt.imshow(img3, cmap='gray')

"""aqui aplica o filtro de média, que soma todos os pixels adjacentes e divide pela quantidade de pixels somados, assim fazendo uma média e salvando em um pixel."""

x = img.shape [0]
y = img.shape [1]
z = img.shape [2]

img4 = np.zeros((x,y), dtype = np.uint8)

for a in range(0,x-1):
  for b in range(0,y-1):
    for c in range(0,z):
      img_vetor = [img[a,b,c]*1, img[a+1,b,c]*1, img[a,b+1,c]*1, img[a+1,b+1,c]*1, img[a-1,b,c]*1, img[a,b-1,c]*1, img[a-1,b-1,c]*1, img[a+1,b-1,c]*1, img[a-1,b+1,c]*1]

      for i in range(0,5):
        for j in range(0,9-1-i):
          if img_vetor[j] > img_vetor[j+1]:
            temp=img_vetor[j]
            img_vetor[j]=img_vetor[j+1]
            img_vetor[j+1]=temp

      img_mediana = img_vetor[4]

      img4[a,b] = img_mediana

plt.imshow(img4, cmap='gray')

"""aqui aplica o filtro de mediana, o filtro de mediana utiliza o valor central (nesse código, o quinto valor) dos pixels ordenados, assim fazendo uma mediana e salvando em um pixel."""