import re

from open_file import open_file, write_to_file



def parse_acc_no(data):
    '''This function is to capture lines that begin
    with the string: Accession
    input: database
    ouput: return captured accession numbers
    '''
    p=re.compile(r'ACCESSION *') # captures the whole line
        
    for i in data:
        if p.findall(i):
            return i


write_to_file(parse_acc_no(open_file('chrom_CDS_8.txt')))
#works well enough, has trouble copying the output(acc_no) to a file.
#issue is with write to file but may provide, perhaps a LOOP statement to write 


def parse_dna_seq():
    '''This function captures DNA sequences from a variable database
    input: database
    output: return captured DNA sequences
    '''
#use Biopython here
    p=re.compile(r'Origin *')
    p.findall(database)
    print(p)



