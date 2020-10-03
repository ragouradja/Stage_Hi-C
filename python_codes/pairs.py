import pandas as pd
import itertools


df = pd.read_table('position.dat',sep='\t',header=None)

list_pairs = list(itertools.combinations(range(len(df)) , 2))

# Initialize TF
TF = "AcrR"

f_out = open("Pairs/pairs_tf_{}.bg2".format(TF),"w+")


for i in list_pairs:
	ind1,ind2 = i
	tf1,chr1,pos1,pos1_1 = df.iloc[ind1]
	tf2,chr2,pos2,pos2_1 = df.iloc[ind2]

	if TF != tf1:
		f_out.close()
		TF = tf1
		f_out = open("Pairs/pairs_tf_{}.bg2".format(TF),"w+")


	f_out.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(chr1,pos1,pos1_1,chr2,pos2,pos2_1))







