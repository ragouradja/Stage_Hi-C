with open("BindingSiteSet.txt","r") as f_in, open("position.dat","w") as f_out:
	for line in f_in:
		if not line.startswith("#"):
			item = line.split("\t",maxsplit = 6)
			if "NA" not in item:
				f_out.write("{}\t{}\t{}\n".format("chr1",item[4],item[5]))


