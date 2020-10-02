import pandas as pd
import itertools


df = pd.read_table('position.dat',sep='\t',header=None)


list_pairs = list(itertools.combinations(range(len(df)) , 2))

with open("pairs_ecoli.bg2","w+") as f_out:
	for i in list_pairs:
		ind1,ind2 = i
		chr1,pos1,pos1_1 = df.iloc[ind1]
		chr2,pos2,pos2_1 = df.iloc[ind2]
		print(i)
		f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chr1,pos1,pos1_1,chr2,pos2,pos2_1))



