#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 12:41:08 2024

@author: manuelrocamoravalenti
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Asumiendo que has guardado el CSV en la misma carpeta que tu notebook
bici_data = pd.read_csv('Valenbici.csv', sep=';')
print(bici_data.head())
print(bici_data.describe())
print(bici_data.info())


# Histograma de disponibilidad de bicis
sns.histplot(bici_data['Bicis_disponibles'])
plt.show()


# Verificar y manejar valores nulos
print(bici_data.isnull().sum())
bici_data.fillna(method='ffill', inplace=True)  # Ejemplo de imputación

