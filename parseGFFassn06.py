#! /usr/bin/env python3

import csv
import argparse
from Bio import SeqIO

# this script will parse s GGG file and extract each feature from the genome
# inputs: 1) GFF file, 2) corresponding genome sequence (FASTA format)

# create an argument parser object
parser = argparse.ArgumentParser(description='This script will parse a GFF file and extract each feature')

# add positional arguments
parser.add_argument("gff", help='name of the GFF file')
parser.add_argument("fasta", help='name of the FASTA file')

# parse the arguments
args = parser.parse_args()




# read in Fasta file
genome = SeqIO.read(args.fasta, 'fasta')
	
print(genome.seq)

# open and read in GFF file
with open(args.gff, 'r') as gff_in:

	#create a csv reader object
	reader = csv.reader(gff_in, delimiter='\t')
     
    # loop over all the lines in our reader objest (i.e., parsed file)
	for line in reader:
		start  = line[3]
		end    = line[4]
		strand = line[6]
		
		#extract the sequence
		

lines = [ ]
with open('watermelon.gff') as f:
	lines = [line for line in f]
	line1 = lines[0]


print(genome.id)

print(line1[44: ])



outfile =open('parseGff.fasta', 'w')

outfile.write( ">" + str(genome.id) + " " + str(line1[44: ]) )

outfile.write(str(genome.seq))

outfile.close()






	



	
	


             
             
             

