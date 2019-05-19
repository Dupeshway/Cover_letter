
import re
from Bio import SeqIO as bseq

from open_file import file_management as fm

class parsing:

    def parse_acc_no(datafile):
        '''This function is to capture lines that begin
        with the string: Accession
        input: strings of each line in text file
        ouput: return captured accession numbers
        '''
        p=re.compile(r'ACCESSION ') # captures the whole line
        #should be until 

        acc_no=''

        for i in datafile:
            if p.findall(i):
                acc_no += i

        return acc_no



    def parse_dna_seq(datafile):
        '''This function captures whole DNA sequences from a variable database, use Biopython to understand
        input: database
        output: return captured DNA sequences
        '''

        p=re.compile(r'ORIGIN *')

        dna_seq=''

        

        for i in datafile:
            if p.findall(i):
                dna_seq += i
            
        return dna_seq

    #print(parse_acc_no(fm.open_file('test_chrom8.txt')))

    #fm.write_to_file(parse_acc_no(fm.open_file(fm.read_file)))

    print('written into', fm.write_file)
#works well enough, has trouble copying the output(acc_no) to a file.
