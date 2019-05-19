import re
from config import config as cg
from file_management import file_management as fm
from parse_genfile import parse_data as pd 
from cleaning_data import clean_data as cl


class sql_format:


    def sql_parse_cds(datafile):
        '''This function converts the output of parse_cds(),
        input: text file with accession number and protein trnaslation in alternating lines
        output: returns an SQL format insertion for a database
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        cds_count=1

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:

                if acc_count==0:
                    clean_data+= "INSERT into CHROM8(ACCESSION, CDS_REGIONS) values ("+cl.clean_lines("'"+line+"',")
                    acc_count+=1
                    cds_count=0

                elif cds_count==0:
                    clean_data+= cl.clean_lines("'"+line+"')ON DUPLICATE KEY UPDATE CDS_REGIONS = '"+line+"';")+"\n"
                    cds_count+=1
                    acc_count=0
            
        return (clean_data)

    def sql_parse_prot_trans(datafile):
        '''This function converts the output of parse_prot_trans(),
        input: text file with accession number and protein trnaslation in alternating lines
        output: returns an SQL format insertion for a database
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        trans_count=1

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:

                if acc_count==0:
                    clean_data+= "INSERT into CHROM8(ACCESSION, TRANSLATION) values ("+cl.clean_lines("'"+line+"',")
                    acc_count+=1
                    trans_count=0

                elif trans_count==0:
                    clean_data+= cl.clean_lines("'"+line+"')ON DUPLICATE KEY UPDATE TRANSLATION = '"+line+"';")+"\n"
                    trans_count+=1
                    acc_count=0
            
        return (clean_data)


    def sql_parse_dna_seq(datafile):
        '''Convert data into an SQL table insertion
        input: file with each dna seq on a seperate line
        output: read each line as seperate string and write to SQL format
        '''
        count=0
        raw_data=[]
        clean_data=''
        acc_data=[]
        acc_count=0
        dna_count=0

        with open(datafile, 'r') as f:
            raw_data+=f.readlines()
            for line in raw_data:

                if acc_count==0:
                    clean_data+= "INSERT into CHROM8(ACCESSION, DNA_SEQUENCE) values ("+cl.clean_lines("'"+line+"',")
                    acc_count+=1
                    dna_count=0

                elif dna_count==0:
                    clean_data+= cl.clean_lines("'"+line+"')ON DUPLICATE KEY UPDATE DNA_SEQUENCE = '"+line+"';")+"\n"
                    dna_count+=1
                    acc_count=0
            
        return (clean_data)




    def parse_gene_id(datafile):
        '''Capture one copy of feature in each record of genbank file
        input: Genbank record
        output: seperate strings for each record
        '''
        
        p=re.compile(r'ACCESSION\s+\w+')
        pgene=re.compile(r'gene="[A-Z]') 
        gene_id=''
        acc_no=''
        
        gene_counter=0
        acc_count=0
        
        datafile=fm.open_file(datafile)

        for i in datafile:
            if acc_count==0:
                if p.findall(i): #finds Accession
                    gene_id+= "INSERT into CHROM8(ACCESSION, GENE_ID) values ('"+i[12:20]+"',"
                    acc_count+=1
                    gene_count=0

            elif gene_count==0:
                    if pgene.findall(i):
                        gene_id+= "'"+i[28:33]+"')ON DUPLICATE KEY UPDATE GENE_ID='"+i[28:33]+"'; \n" #finds gene="[A-Z] 
                        gene_count+=1
                        acc_count=0

        return cl.remove_apost(gene_id) #removing apostraphes



    def parse_chrom_loc(datafile):
        '''Capture one copy of feature in each record of genbank file
        input: Genbank record
        output: seperate strings for each record
        '''
        
        p=re.compile(r'ACCESSION\s+\w+')
        pchrom=re.compile(r'map=') 
        chrom_loc=''
        acc_no=''
        
        chrom_count=0
        acc_count=0
        
        datafile=fm.open_file(datafile)

        for i in datafile:
            if acc_count==0:
                if p.findall(i): #finds Accession
                    chrom_loc+= "INSERT into CHROM8(ACCESSION, CHROM_LOC) values ('"+i[12:20]+"',"
                    acc_count+=1
                    chrom_count=0
                

            elif chrom_count==0:
                    if pchrom.findall(i):
                        chrom_loc+= "'"+i[27:33]+"')ON DUPLICATE KEY UPDATE CHROM_LOC='"+i[27:33]+"'; \n" #finds chrom_loc (map= in genbank) 
                        chrom_count+=1
                        acc_count=0

        return cl.remove_apost(chrom_loc) #removing apostraphes and whitespaces
