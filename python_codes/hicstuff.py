import os

path_read = "/pasteur/homes/rradjasa/hicstuff/read"
file_read = os.chdir(path_read)

for read in file_read:

    os.system("Read : ",read)

    #os.system("~/sratoolkit.2.9.6-ubuntu64/bin/fastq-dump {} --split-3 -O fastq".format(read))
    