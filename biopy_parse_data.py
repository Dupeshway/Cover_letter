#!/usr/bin/env python3

#Yobi Livingstone

import re
from Bio import SeqIO
from config import config as cg
from cleaning_data import clean_data as cl
from file_management import file_management as fm

class parsing:
    '''Each function parses Genbank format files, usually employing Biopython
    to write into files for SQL table building'''


    def describe_genbank():
        '''Quick descriptor of the genbank file'''

        for i in SeqIO.parse(cg.r_file, "genbank"):
            print("Accession:", i.name)
            print("Description:", i.description)
            print("Length of Sequence:", len(i.seq))
            print("Length of coding seq:", len(feature.location.extract(rec).seq))# define the feature


    def parse_CDS(file):
        '''Function to parse the CDS numbers along with their accession numbers
        input: read file, genbank
        output: CDS description
        '''
        write_file= cg.cds_file
        fm.wipe_file(write_file) #wipe write file
        for rec in SeqIO.parse(file, "genbank"):# for every entry(rec) run though the following
            if rec.features:
                for feature in rec.features:
                    #gathering and cleaning accession
                    if feature.type=='CDS':
                        
                        acc= cl.remove_version(rec.id)
                        fm.write_file("insert into CDS values ('"+ acc + "',", write_file)
                        #Accession numbers
                        
                        cds_region= cl.clean_cds_region(feature.location)
                        fm.write_file("'"+cds_region+"',", write_file)
                        #CDS regions

                        try:
                            cds_seq=str(feature.location.extract(rec).seq)
                            fm.write_file("'"+cds_seq+"'); \n", write_file)
                            #CDS sequence

                        except:
                            fm.write_file("'CDS ERROR; FULL DNA SEQUENCE:"+str(rec.seq) +"');\n", write_file)
                            continue


    def parse_acc():
        '''Using Biopython to parse Accession numbers
        input: empty, indirectly
        output: Accession numbers
        '''
        fm.wipe_file(cg.acc_file)

        for i in SeqIO.parse(cg.r_file, "genbank"):
            acc= cl.remove_version(i.id)
            fm.write_file(acc + '\n', cg.acc_file)

    def parse_dna_seq():
        '''This function captures whole DNA sequences from a variable database
        input: database
        output: return captured DNA sequences
        '''

        fm.wipe_file(cg.dna_file)
        for dnaseq in SeqIO.parse(cg.r_file, "genbank"):
            fm.write_file(str(dnaseq.seq) +'\n'+'\n', cg.dna_file)


    def parse_acc_dna(r_file):
        '''This function captures Accession numbers and whole DNA sequences
        from a variable database
        input: read file, containing sequences
        output: return captured DNA sequences
        '''
        write_file=cg.gene_file
        fm.wipe_file(write_file)
        for record in SeqIO.parse(cg.r_file, "genbank"):
            acc= cl.remove_version(record.id)
            fm.write_file("insert into GENE values ('"+ acc + "', '", write_file)
            fm.write_file(str(record.seq) +"'); \n", write_file)


    def parse_CDS(file):
        '''Function to parse the CDS numbers along with their accession numbers
        input: read file, genbank
        output: CDS description
        '''
        fm.wipe_file(cg.cds_file)
        for rec in SeqIO.parse(file, "genbank"):
            if rec.features:
                for feature in rec.features:
                    acc= cl.remove_version(rec.id)
                    fm.write_file("insert into CDS values ("+"'"+ acc + "' ,", cg.cds_file)
                    #gathering and cleaning accession
                    if feature.type == "CDS":

                        aa_seq=feature.qualifiers['translation']                        
                        fm.write_file("'"+aa_seq[0]+"')", cg.cds_file) #captures string inside the list []
                        
                    else:
                        cds_region= cl.clean_cds_region(feature.location)
                        fm.write_file("'"+cds_region+"'", cg.cds_file) #Where the CDS regions are

                        fm.write_file("'"+feature.location.extract(rec).seq+"');", cg.cds_file) #CDS sequences



    def parse_CHROM8(file):
        '''Function to parse the CDS numbers along with their accession numbers
        input: read file, genbank
        output: CDS description
        '''

        #write_file= cg.cds_file
        #fm.wipe_file(write_file) #wipe write file
        for rec in SeqIO.parse(file, "genbank"):# for every entry(rec) run though the following
            if rec.features:
                for feature in rec.features:

                    if feature.type=='CDS':


                        #Accession numbers
                        acc= cl.remove_version(rec.id)
                        print(acc)


                        #chromosomal location
                        try:
                            
                            chroma_loc= feature.source["map"]
                            print(chroma_loc[0])
                        except:
                            print('chroma_loc not found')
                        



