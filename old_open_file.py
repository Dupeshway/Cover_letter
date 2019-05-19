class variables:
'''To store all the variables necessary'''




class file_management:
'''To open, read and write files'''


    def __int__(variable, write_file, read_file):
        vairable.read_file= 'test_chrom8.txt'
        variable.write_file= 'acc_no.txt'
        

    def open_file(read_file):
        '''Input: text file of chromosome
        Output: string of each line in text file for parsin some types of data'''


        with open(read_file,'r') as f:
            datafile = f.read().splitlines()
            return datafile


    def write_to_file(read_file):
        '''Writes to the file parameter
        input: takes input(text file) as file to write to,
        output: database written into file'''

        
        f=open(write_file,'w')
        f.write(read_file)

