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

# load the necessary modules
print('# load modules')
print('module purge')
print('module load gcc/7.2.1')
print()

# command for this job
print('# insert commands here')


