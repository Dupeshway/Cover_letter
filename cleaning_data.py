#!/usr/bin/env python3

#Yobi Livingstone
import re

class clean_data:
    '''Every function is intended to join, remove, replace iterables (strings, lists etc)
    to make the data easier to handle after capturing/parsing'''


    def join_strings(raw_data):
        '''Join strings
        input: raw_data be multiple strings or lists
        output: raw_data turned into a single string: clean_data'''

        clean_data=''
        clean_data=clean_data.join(raw_data)
        return clean_data


    def clean_cds_region(raw_data):
        '''remove special characters and letters from captured CDS regions
        input: captured CDS region strings from genbank file
        output: CDS region strings in this format: 1..10
        '''
        raw_data=str(raw_data)
        clean_data=re.sub('[joincmplement()<>+{}]','', raw_data)
        return clean_data

    def hyphenise(raw_data):
        '''Intended for CDS region database format
        input: captured CDS region data with periods seperating the integers
        output: double periods replaced by a hyphen
        '''
        raw_data=str(raw_data)
        clean_data = raw_data.replace('..', '-')
        return clean_data


    def remove_apost(raw_data):
        '''Removing apostraphes from string
        input: string
        output: string absent of apostraphes
        '''
        clean_data = raw_data.replace('"','')
        return clean_data


    def remove_version(acc_no):
        '''Accession numbers captured have a version number after a decimal point
        at the end of the number i.e AB12345678.1 This removes the version number [.1]
        input:Accession numbers with version number attached
        output: Accession number without version number attached
        '''
        acc_no=str(acc_no)
        for i in acc_no:
            if i=='.':
                acc_no = acc_no[:-2] #captures all except the last two places
        return acc_no


    def clean_wspace(dna_seq):
        '''Remove white space and line seperators in all forms
        input: raw DNA sequence
        output: raw DNA sequence without whitespace or line seperation'''
    
        dna_seq = dna_seq.replace('\n', '')
        dna_seq = dna_seq.replace(' ', '')
        return(dna_seq)


    def clean_lines(raw_data):
        '''Remove line seperators in all forms
        input: raw DNA sequence
        output: raw DNA sequence without empty lines seperation'''
    
        raw_data = raw_data.replace('\n', '')
        return(raw_data)



    def clean_nos(raw_data):
        '''Remove all numbers from FASTA format DNA sequence
        input: raw DNA sequence in FASTA
        output: raw DNA sequence without FASTA numbers'''
    
        nos = ['0','1','2','3','4','5','6','7','8','9']
        dna_seq = dna_seq.replace(nos, '')

        return(dna_seq)

    def capitalise(raw_data):
        '''Entire string is capitalised
        input: single string in upper and lowercase forms
        output: single string all uppercase
        '''
        uppercase=''
        for i in raw_data:
            dna_seq=raw_data.upper()
        return dna_seq

    

    def ignore_nnn(raw_data):
        '''ignore database codon entries with N
        Input: string(DNA seq) is read from text file
        Output: clean_string without N is passed through, codons with N is ignored
        '''
        clean_string=''
    
        for i in raw_data:
            if i!='N' or 'n':
                clean_string.append(string)
            else:
                continue
    
        return clean_string



