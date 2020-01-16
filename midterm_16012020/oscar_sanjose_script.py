def read_matrix(file_matrix):
    f = open(file_matrix,"r")
    listas = []
    dictio = {}
    line1 = f.readline()
    aa = line1[9:29]
    for line in f:
        line = line.rstrip()
        line = line.replace(".","")
        line = line.split()
        listas.append(line)
    for i in range(len(listas)):
        for z in range(len(listas[i])):
            dictio[aa[i]+aa[z]] = int(listas[i][z])
    for i in dictio.keys():
        if i[::-1] not in dictio.keys():
            dictio[i[::-1]] = dictio[i]
    return dictio

def read_align(fasta_file):
    f = open(fasta_file,"r")
    alignments = []
    seqs = []
    for line in f:
        if line[0] != ">" and line[0] != "\n": #The line[0] != "\n" step was because when I copied the file ther was two \n at the end
            line =line.rstrip()
            seqs.append(line)
    for i in range(0, len(seqs),2):
        seq1 = seqs[i]
        seq2 = seqs[i+1]
        alignments.append([seq1,seq2])
    return alignments

def score_align(alignments, matrix):
    score = 0
    scores = []
    for i in range(len(alignments)):
        for z in range(len(alignments[i][0])):
            if alignments[i][0][z] == "-" or alignments[i][1][z] == "-":
                score += -2
            else:
                score += matrix[alignments[i][0][z] + alignments[i][1][z]]
        scores.append(score)
        score = 0
    return scores

def score_align_extended_gaps(alignments, matrix):
    score = 0
    scores = []
    flag = False
    for i in range(len(alignments)):
        for z in range(len(alignments[i][0])):
            if alignments[i][0][z] == "-":
                if alignments[i][0][z-1] != "-":
                    flag = False
                if flag:
                    score += -0.5
                else:
                    score += -2
                    flag = True
            elif alignments[i][1][z] == "-":
                if alignments[i][1][z-1] != "-":
                    flag = False
                if flag:
                    score += -0.5
                else:
                    score += -2
                    flag = True
            else:
                score += matrix[alignments[i][0][z] + alignments[i][1][z]]
        scores.append(score)
        score = 0
    return scores

def print_aligns(alignments, score_PAM,score_BLOSUM):
    for i in range(len(alignments)):
        print alignments[i][0]
        print alignments[i][1]
        print "PAM250:" + str(score_PAM[i])
        print "BLOSUM62:" + str(score_BLOSUM[i])

PAM250 = read_matrix("PAM250.txt")
BLOSUM62 = read_matrix("BLOSUM62.txt")
SEQS = read_align("alignments.fasta")
PAM_score = score_align_extended_gaps(SEQS, PAM250)
BLOSUM62_score = score_align_extended_gaps(SEQS, BLOSUM62)
print_aligns(SEQS, PAM_score, BLOSUM62_score)
