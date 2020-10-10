
import os

name_map = "contacts2_Coli_PM35_2000_df.bg2.cool"
path_tf = "/home/ragou/Bureau/Stage_Hi-C/Pairs"

file_tf = os.listdir(path_tf)

for tf in file_tf:

	name_tf = tf.split("_")[2].split(".")[0]
	os.system("chromosight quantify ./../Pairs/{} {} ./results/{}_loops".format(tf,name_map,name_tf))
	
		
		
