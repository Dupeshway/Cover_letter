#!/usr/bin/env python3

#Yobi Livingstone

import re

from config import config as cg
from file_management import file_management as fm
from cleaning_data import clean_data as cl

class parse_data:

        def parse_cds(datafile):
            '''This function captures the CDS region in a genbank file
            input: text file in genbank format
            ouput: return captured CDS region numbers, indexed by Accession
            '''        

            pcds=re.compile(r'CDS\s+') #find multiple line CDS regions
            pacc=re.compile(r'ACCESSION\s+\w+') #find Accession numbers
            psincds=re.compile(r'CDS\s+join\(.*?\)|CDS\s+.*?[^,]$') #capture single line CDS

            cds_data=''
            datafile=fm.open_file(datafile)

            cds_count=0
            brack_count=0
            acc_count=0

            for line in datafile:
                if acc_count==0:
                    if pacc.findall(line):
                        cds_data+= line[12:20]+"\n"
                        acc_count+=1
                        cds_count=0


                elif cds_count==0: 
                    if psincds.findall(line): #first try to find single-line cds regions
                        cds_data+= line[21:]+"\n" #to negate the " at the end of single line cds
                        cds_count+=1
                        acc_count=0

                        
                    elif pcds.findall(line): #find multi-line cds
                        cds_data+= line[21:]
                        cds_count+= 1 #wont reset accession until all lines are captured
                            
                else:
                    for i in line:
                            
                        if i !=')': #if char is not ), collect i
                            cds_data += i.replace(' ', '')
                            

                        elif i == ')' and brack_count==0:
                            cds_data += "\n" #if char is ) and count=0, collect i
                            brack_count += 1
                            cds_count=0
                            acc_count = 0
                            break

                        elif i == ')' and brack_count>0:
                            cds_data += "\n" # if char is ) and count over 0, collect i
                            brack_count = 0
                            acc_count = 0
                            break

            cds_data= cl.clean_cds_region(cds_data)
            return cl.hyphenise(cds_data)


        def parse_prot_trans(datafile):
            '''This function camptures the full dna sequence #KEEP WORKING ON THIS
            input: text file in genbank format
            ouput: return captured protein translation, indexed by Accession
            '''        

            ptrans=re.compile(r'translation="')
            pacc=re.compile(r'ACCESSION\s+\w+')
            pshtrans=re.compile(r'translation="\w+"')

            
            prod_trans=''
            datafile=fm.open_file(datafile)

            trans_count=0
            short_trans_count=0
            brack_count=0
            acc_count=0

            for line in datafile:
                if acc_count==0:
                    if pacc.findall(line):
                        prod_trans+= line[12:20]+"\n"
                        acc_count+=1
                        trans_count=0


                elif trans_count==0: 
                    if pshtrans.findall(line): #find single-line translations denoted by ending with [\W"]
                        prod_trans+= line[35:-1]+"\n" #to negate the " at the end of single line translations
                        trans_count+=1
                        acc_count=0
                        
                    elif ptrans.findall(line): #find multi-line translations
                        prod_trans+= line[35:]
                        trans_count+= 1
                            
                else:
                    for i in line:
                            
                        if i !='"': #if char is not ", collect i
                            prod_trans += i.replace(' ', '')
                            

                        elif i == '"' and brack_count==0:
                            prod_trans += "\n" #if char is " and count=0, collect i
                            brack_count += 1
                            acc_count = 0
                            break

                        elif i == '"' and brack_count>0:
                            prod_trans += "\n" # if char is " and count over 0, collect i
                            brack_count = 0
                            acc_count = 0
                            break


            return prod_trans
 


        def parse_product_name(datafile):
            '''Captures the protein product name from a Genbank file
            input: chromosomal data file (genbank)
            output: protein product names, indexed by Accession, in SQL insertion format
            '''

            pprod=re.compile(r'product="') #find product names (always single line)
            p=re.compile(r'ACCESSION\s+\w+')
            pro_prod=''
            acc_no=''
                
            prod_counter=0
            acc_count=0
                
            datafile=fm.open_file(datafile)

            for i in datafile:
                if acc_count==0:
                    if p.findall(i): #finds Accession
                        pro_prod+= "INSERT into CHROM8(ACCESSION, PRODUCT_NAME) values ('"+i[12:20]+"',"
                        acc_count+=1
                        prod_count=0
                        

                elif prod_count==0:
                    if pprod.findall(i):
                        pro_prod+= "'"+i[31:70]+"')ON DUPLICATE KEY UPDATE PRODUCT_NAME='"+i[31:70]+"'; \n" #finds product="[A-Z] 
                        prod_count+=1
                        acc_count=0

            return cl.remove_apost(pro_prod) #removing apostraphes and whitespaces


        def simpleparse_acc_no(datafile):
            '''This function is to capture lines that begin
            with the string: Accession
            input: text file in genbank format
            ouput: return captured accession numbers, each number on a new line
            '''
            p=re.compile(r'ACCESSION\s+\w+') 
            #there are between 6-8 letters/number in an acc_no

            acc_no=''
            datafile=fm.open_file(datafile)
            for i in datafile:
                if p.findall(i):
                    acc_no += i[12:20]+"\n"

            return acc_no


        def parse_acc_no(datafile):
            '''This function is to capture lines that begin
            with the string: Accession
            input: strings of each line in text file
            ouput: return captured accession numbers ready for SQL insertion
            '''
            p=re.compile(r'ACCESSION\s+\w+') 
            #there are between 6-8 letters/number in an acc_no

            acc_no=''
            datafile=fm.open_file(datafile)
            for i in datafile:
                if p.findall(i):
                    acc_no += "insert into CHROM8(ACCESSION) VALUES('"+i[12:20]+"');\n"

            return acc_no

        def parse_dna_seq(datafile):
            '''This function camptures the full dna sequence
            input: strings of each line in text file
            ouput: return captured dna seq numbers
            '''        

            pdna=re.compile(r'1 [agct][agct]') #find 1 followed by 2*[agct]
            #to negate false positives, 1*[agct] captures too much,
            #however this function does miss sequences that end with
            #a single nucleotide on the last line
            pbrack=re.compile(r'//')#each record is seperated by //, useful to reset counts and start capturing again
            pacc=re.compile(r'ACCESSION\s+\w+')
               
            dna_seq=''
            datafile=fm.open_file(datafile)

            brackcount=0
            acc_count=0

            for i in datafile:
                if acc_count==0:
                    if pacc.findall(i):
                        dna_seq+=i[12:20]+"\n"
                        acc_count+=1
                        brackcount=0

                    
                if pdna.findall(i):
                    dna_seq += cl.clean_wspace(i[10:75])

                if brackcount==0 and acc_count==1 :
                    if pbrack.findall(i):
                        dna_seq+="\n"
                        brackcount+=1
                        acc_count=0


            return cl.capitalise(dna_seq)



