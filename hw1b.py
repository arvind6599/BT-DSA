#BT3051 Assignment 1b
#Roll number: EP17B017 
#Collaborators: - 
#Time: 3:00

import sys
import doctest



def read_FASTA(fname):
    ''' str --> list of tuples'''
    f=open(fname,'r')
    l=f.read().rsplit('\n')

    sequences=[]

    for i in range(0,len(l),2):

        #forming the tuples
        t=(l[i][1:],l[i+1])
        sequences.append(t)
    #print(sequences)
    return sequences

def identify_orfs(dnaStrand):

    k=0
    s=0
    frames=[]

    while(k<3):
        
        r=[]
        r1=[]
        w=0 #flag for start of the ORF
        x=0
        f=""
        #forming different reading frames
        for i in range(k,len(dnaStrand),3):
            c=dnaStrand[i:i+3]
            if(len(c)==3):
                r.append(c)
        
        while(x<len(r)):
            
            #start of ORF
            if(r[x]=='ATG'):
                #for starts that are between a start and stop
                if(w==1):
                    r1.append(x) #Stores all the indices of starts in between
                w=1

            #end of ORF
            if(r[x]=='TAA' or r[x]=='TAG' or r[x]=='TGA'):
                #print(f)
                if(w==1):
                    frames.append(f)
                    f=""
                    if(r1!=[]):
                        for i in r1:
                            for j in range(i,x):
                                f+=r[j]
                            frames.append(f)
                            f=""
                        r1=[]
                w=0
                f=""
            
            #appending ORF
            if(w==1):
                f+=r[x]
            
            x+=1

        k+=1
        if(k==3 and s==0):
            s=1
            #print(dnaStrand)
            #revsersing the string and running the process again for next three reading frames
            dnaStrand=dnaStrand[::-1]
            #print(dnaStrand)
            #inverting the dna strand
            l=""
            for x in dnaStrand:
                if(x=='A'):
                    l=l+'T'
                elif(x=='T'):
                    l=l+'A'
                elif(x=='G'):
                    l=l+'C'
                else:
                    l=l+'G'

            dnaStrand=""
            #print(l)

            #to avoid shallow copy i assigned element wise
            for x in range(len(l)):
                dnaStrand+=l[x]
            #print(dnaStrand)
            k=0
    print(frames)
    return frames

def translate_DNA(dnaStrand,translation_table='DNA_TABLE.txt'):
    """
    function body including documentation and test cases
    >>> translate_DNA('ATGTATGATGCGACCGCGAGCACCCGCTGCACCCGCGAAAGCTGA')
    'MYDATASTRCTRES'
    """

    #dictionary to store the corresponding protein for each codon
    d={'TTT':'F','CTT':'L','ATT':'I','GTT':'V','TTC':'F','CTC':'L','ATC':'I','GTC':'V','TTA':'L','CTA':'L','ATA':'I','GTA':'V','TTG':'L','CTG':'L','ATG':'M','GTG':'V','TCT':'S','CCT':'P','ACT':'T','GCT':'A','TCC':'S','CCC':'P','ACC':'T','GCC':'A','TCA':'S','CCA':'P','ACA':'T','GCA':'A','TCG':'S','CCG':'P','ACG':'T','GCG':'A','TAT':'Y','CAT':'H','AAT':'N','GAT':'D','TAC':'Y','CAC':'H','AAC':'N','GAC':'D','TAA':'Stop','CAA':'Q','AAA':'K','GAA':'E','TAG':'Stop','CAG':'Q','AAG':'K','GAG':'E','TGT':'C','CGT':'R','AGT':'S','GGT':'G','TGC':'C','CGC':'R','AGC':'S','GGC':'G','TGA':'Stop','CGA':'R','AGA':'R','GGA':'G','TGG':'W','CGG':'R','AGG':'R','GGG':'G'}
    protiens=""
    for i in range(0,len(dnaStrand),3):
        #extracting each codon
        s=dnaStrand[i:i+3]
        if(d[s]!="Stop"):
            protiens+=d[s]

    return protiens

def compute_protien_mass(protien_string):
    """
    test case
    >>> compute_protien_mass('SKADYEK')
    821.392
    """

    p={'A':'71.03711','C':'103.00919','D':'115.02694','E':'129.04259','F':'147.06841','G':'57.02146','H':'137.05891','I':'113.08406','K':'128.09496','L':'113.08406','M':'131.04049','N':'114.04293','P':'97.05276','Q':'128.05858','R':'156.10111','S':'87.03203','T':'101.04768','V':'99.06841','W':'186.07931','Y':'163.06333'}
    mass=0
    for x in protien_string:
        mass=mass+float(p[x])
    
    #to change number of values after decimel point to 3
    mass=round(mass,3)
    return mass 

if __name__ == '__main__':
    
    for seq_name , seq in read_FASTA("hw1.faa"):
        print(seq_name+":")
        for orf in identify_orfs(seq):
            protien=translate_DNA(orf)
            print(protien, compute_protien_mass(protien))
    #for test cases
    doctest.testmod()
    
#CGCTACGTCTTACGCTGGAGCTCTCATGGATATGCGGTTCGGTAGTAGGGCTCGATCACATCGCTAGCCAT