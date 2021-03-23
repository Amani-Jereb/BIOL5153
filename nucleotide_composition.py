#! /usr/bin/env python3

# This script generate a PBS file for the AHPCC Razor cluster

# This section prints the header/required info for the PBS script
print('#PBS -N test') # job name
print('#PBS -q tiny12core') # queue
print('#PBS -j oe') # prefix for the output file, which should match the job name
print('#PBS -o ahjereb.$PBS_JOBID') # number of nodes
print('#PBS -l nodes=1:ppn=1') # number of processors
print('#PBS -l walltime=1:00:00') # walltime
print()

# cd into working directory
print('cd $PBS_O_WORKDIR')
print()

# Read the file and get the DNA nucl count
file = open('dna.txt')
dna = file.read()

# Print the nucl DNA count
print "DNA String: ", dna

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()




# Print the count of each letter
print "Count of A: ", dna.count("A")
print "Count of C: ", dna.count("C")
print "Count of G: ", dna.count("G")
print "Count of T: ", dna.count("T")

# Read the file and get the DNA string
file = open("sample_dna.txt", "r")
dna = file.read()

# Print the original DNA string
print "DNA String: ", dna

