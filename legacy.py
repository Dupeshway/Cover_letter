#!/usr/bin/env python3

#Yobi Livingstone

#legacy functions

import re

from config import config as cg
from file_management import file_management as fm
from parse_data import parsing as pg
from cleaning_data import clean_data as cl


class legacy:


    def v2parse_gene_id(datafile):
        '''Capture one copy of feature in each record of genbank file
        input: Genbank record
        output: seperate strings for each record
        '''
        
        p=re.compile(r'//')
        pgene=re.compile(r'gene="[A-Z]') 
        gene_id=''

        gene_counter=0
        count=0
        datafile=fm.open_file(datafile)

        for i in datafile:
            if p.findall(i): #finds // 
                count=0
                

            elif count==0:
                    if pgene.findall(i):
                        gene_id+= i[28:33]+'\n' #finds gene="[A-Z] 
                        count+=1

        return cl.remove_apost(gene_id) #removing apostraphes and whitespaces           


    def v1parse_gene_id(datafile):
        '''This function captures lines the the gene_id
        input: strings of each line in text file
        ouput: 
        '''
        p=re.compile(r'gene="[A-Z]') 
        #there are between 6-8 letters/number in an acc_no

        gene_id=''
        raw_data=fm.open_file(datafile)
        for i in raw_data:
            if p.findall(i):
                gene_id += i[28:33]+'\n'

        return(cl.remove_apost(gene_id))
        return(cl.clean_wspace(gene_id))



    def parse_acc_no(datafile):
        '''This function is to capture lines that begin
        with the string: Accession
        input: strings of each line in text file
        ouput: return captured accession numbers
        '''
        p=re.compile(r'ACCESSION\s+\w+') 
        #there are between 6-8 letters/number in an acc_no

        acc_no=''

        for i in datafile:
            if p.findall(i):
                acc_no += i[:20]

        return acc_no



    def parse_dna_seq(datafile):

        p=re.compile(r'ORIGIN *')
        dna_seq=''
        
        for i in datafile:
            if p.findall(i):
                dna_seq += i
            
        return dna_seq


    def clean_cds_region(raw_data):
        dirt = ('j','o','i','n','{','}','(',')','+','[',']')
        for i in raw_data:
            if i == dirt:
                raw_data=raw_data.replace(i,'')
        print(raw_data)



print(legacy.parse_acc_no(cg.r_file))
