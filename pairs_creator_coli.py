# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:15:46 2018
@author: axel KournaK 
To create all possible pairs from genomic positions.
"""
import numpy as np
import matplotlib
from pylab import *
import pandas as pd
import itertools

BIN=1000

# Input: list of genomic positions :

df=pd.read_table('/home/axel/Bureau/matS_cell.dat4',header=None, delimiter="\t")


#------------------------------------------------------------------------------
# Intra and inter pairs :

f_out1 = open("pairs_intra_groupe_common_mats.bg2","w+")

len(df)
list_pairs = list(itertools.combinations( range(len(df)) ,2 ))
len(list_pairs)    

for e in list_pairs :
    e1, e2 = e
    chr1, pos1 = df.iloc[e1]
    chr2, pos2 = df.iloc[e2]
    if chr1 == chr2 : 
        f_out1.write(chr1 + '\t'+ str( int(pos1) )+ '\t' + str( int(pos1+BIN))+ '\t' + 
                     chr2 + '\t'+ str( int(pos2)) + '\t' + str( int(pos2+BIN))+ '\t' + "1" +'\n')

f_out1.close()






# varisous tests:  

list_all_chrms = ("chr5") 
BIN=1

chr="chr5"
bs = df.loc[(df[0] == chr)]
bs = bs[1]
len(bs)
combi_pos = list(itertools.combinations(bs , 2) )
for p in range(0, len(combi_pos) ):    #  to write pairs of positions of peaks and potential loops
    plot(int(combi_pos[p][0]/BIN), int(combi_pos[p][1]/BIN),'o', color="yellow")
