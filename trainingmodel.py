# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 13:35:36 2020

@author: casti
"""

from sklearn.datasets import load_wine
import pandas as pd

d = load_wine()
print(d['DESCR'])
df = pd.DataFrame(d['data'], columns=d['feature_names'])
y = d['target']  # cultivator