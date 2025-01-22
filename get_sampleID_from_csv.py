
''' This script reads a specific file line by line
	splits each line at "_" to get the first element
	after the underline, which in this case is the
	sample ID.
	
	It outputs a file with one sample ID per line.
	
	Next I will transform the code below into a
	function to be added to a module.
	'''

import os
from sys import argv


if __name__ == "__main__":
	if len(argv) != 3:
		print("Usage: python3 get_sampleID_from_csv.py input.csv output.csv")
		exit(1)

infile = argv[1]
outfile = argv[2]

sampleID = []

with open(infile, "r") as runs_path:
	for line in runs_path:
		sampleID.append(line.split('_')[1])


#outfile = f'sequenced_sampleIDs.csv'
header = "sampleIDs"
with open(outfile, "w") as outf:
	outf.write(header + '\n')
	for i in sampleID:
		if i == 'path':
			continue
		outf.write(f'{i}\n')