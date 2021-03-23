{
 "metadata": {
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.1"
  },
  "orig_nbformat": 2,
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9.1 64-bit",
   "metadata": {
    "interpreter": {
     "hash": "7812ea015bdcee6f23a998adcdd2ef97c151c0c241b7b7070987d9313e41299d"
    }
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2,
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [],
   "source": [
    "# set the name of the input DNA file\n",
    "filename = ('dna.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open the input file, assign to file handle called 'infile'\n",
    "infile = open(filename, 'r')\n",
    "# print(infile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [],
   "source": [
    "# read the file \n",
    "dna_sequence = infile.read().rstrip()\n",
    "# dna_sequence = dna_sequence.rstrip()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "ACGGATCCTATCAAATATTTCACATTTTCTATGATCATCTCTATTTTAGGTATTCGGGGAATCCTCCTTAATAGACGAAATATTCCTATTATGTCAATGCCAATTGAATCAATGTTATTAGCTGTGAATTCGAACTTTTTGGTATTTTCCGTTTCTTCGGATGATATGATGGGTCAATCATTTGCTTCATTGGTTCCAACGGTGGCAGCTGCGGAATCCGCTATTGGGTTAGCCATTTTCGTTATTACTTTCCGAGTCCGAGGGACTATTGCTGTAGAATTTATTAATAGCATTCAAGGTTAA\n"
     ]
    }
   ],
   "source": [
    "# print the dna sequence\n",
    "print(dna_sequence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
   "metadata": {},
   "outputs": [],
   "source": [
    "infile.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "ACGGATCCTATCAAATATTTCACATTTTCTATGATCATCTCTATTTTAGGTATTCGGGGAATCCTCCTTAATAGACGAAATATTCCTATTATGTCAATGCCAATTGAATCAATGTTATTAGCTGTGAATTCGAACTTTTTGGTATTTTCCGTTTCTTCGGATGATATGATGGGTCAATCATTTGCTTCATTGGTTCCAACGGTGGCAGCTGCGGAATCCGCTATTGGGTTAGCCATTTTCGTTATTACTTTCCGAGTCCGAGGGACTATTGCTGTAGAATTTATTAATAGCATTCAAGGTTAA\n"
     ]
    }
   ],
   "source": [
    "print(dna_sequence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 108,
   "metadata": {},
   "outputs": [],
   "source": [
    "seglen = len(dna_sequence)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Sequence length 303\n"
     ]
    }
   ],
   "source": [
    "print(\"Sequence length\", seglen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "76\n54\n58\n115\n"
     ]
    }
   ],
   "source": [
    "numA = dna_sequence.count('A')\n",
    "numC = dna_sequence.count('C')\n",
    "numG = dna_sequence.count('G')\n",
    "numT = dna_sequence.count('T')\n",
    "# print Number of A, C, G, T\n",
    "print(numA)\n",
    "print(numC)\n",
    "print(numG)\n",
    "print(numT)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "0.251\n0.178\n0.191\n0.380\n0.370\n1.0\n"
     ]
    }
   ],
   "source": [
    "freqA = numA / seglen\n",
    "freqC = numC / seglen\n",
    "freqG = numG / seglen\n",
    "freqT = numT / seglen\n",
    "freqA1 = \"{:.3f}\".format(freqA)\n",
    "freqC1 = \"{:.3f}\".format(freqC)\n",
    "freqG1 = \"{:.3f}\".format(freqG)\n",
    "freqT1 = \"{:.3f}\".format(freqT)\n",
    "freqCG = freqC + freqG \n",
    "freqCG1 = \"{:.3f}\".format(freqCG)\n",
    "\n",
    "# print frequences of A, C, G, T\n",
    "print(freqA1)\n",
    "print(freqC1)\n",
    "print(freqG1)\n",
    "print(freqT1)\n",
    "print(freqCG1)\n",
    "print(freqA + freqC + freqG + freqT)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "outfile =open('nucleotide_composition.txt', 'w')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "metadata": {},
     "execution_count": 115
    }
   ],
   "source": [
    "outfile.write('Sequence length: ' + str(seglen) + '\\n')\n",
    "outfile.write('Freq of A: ' + str(freqA1) + '\\n')\n",
    "outfile.write('Freq of C: ' + str(freqC1) + '\\n')\n",
    "outfile.write('Freq of G: ' + str(freqG1) + '\\n')\n",
    "outfile.write('Freq of T: ' + str(freqT1) + '\\n')\n",
    "outfile.write('G+C content: ' + str(freqCG1) + '\\n')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "outfile.close()"
   ]
  }
 ]
}