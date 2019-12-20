def matrix (filetxt):
    d_score={}
    M1= open (filetxt, "r")
    first = M1.readline ()
    first= first.split()
    for line in M1:
        line= line.rstrip()
        line= line.split()
        for i in range(len(first)):
            key= line[0]+first[i]
            value= int(line[i+1])
            d_score[key] = value
    return d_score

def score_seq(dicti,seq1,seq2):
    if len(seq1)==len(seq2):
        totalscore=0
        for i in range(len(seq1)):
            couple= seq1[i]+seq2[i]
            if couple in dicti.keys():
                totalscore+= dicti[couple]
    return totalscore

dictionary= matrix ("./Blosum.txt")
sequence1= input ("insert a sequence: ")
sequence2= input ("insert a sequence: ")
print score_seq(dictionary,sequence1,sequence2) 