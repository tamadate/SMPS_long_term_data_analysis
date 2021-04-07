import math
import numpy as np
import pandas as pd
import glob
import csv
import PyGnuplot as gp

with open("general.dat", mode="w") as f:
	for f_name in sorted(glob.glob('./datas/*')):
		data=pd.read_csv(f_name,header=None)
		for i in data.index:
			if "Sample #\t1\t2\t3" in data[0][i]:
				start=int(i)
		data=pd.read_table(f_name,header=start)

		for j in np.arange(3,100,1):
			f.write("\n"+data["1"][0]+"/"+data["1"][1]+"\t"+"0"+"\t"+data["1"][j]+"\n")
		f.write("\n")

		for i in data:
			if i == "Sample #":
				continue
			for j in np.arange(3,100,1):
				f.write(data[i][0]+"/"+data[i][1]+"\t"+data["Sample #"][j]+"\t"+data[i][j]+"\n")
			f.write("\n")
		for j in np.arange(3,100,1):
			f.write(data[i][0]+"/"+data[i][1]+"\t0\t"+data[i][j]+"\n")


gp.c('load "graph.gpi"')
