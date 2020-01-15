def matrix(filetxt):
   d_score = {}
   M1= open (filetxt, "r")
   first = M1.readline()
   first= first.split()
   for line in M1:
       line= line.rstrip()
       line= line.split()
       for i in range(len(first)):
           key= line[0]+first[i]
           value= int(line[i+1])
           d_score[key] = value
   return d_score

def score_alignment(seq_list1,seq_list2,matrix):
    score = 0
    for i in range(len(seq1_list)):
        couple = seq_list1[i] + seq_list2[i]
        if couple.count("_") == 1:
            score += -2
        elif couple.count("_") == 2:
            score += 0
        elif couple in matrix:
            score += matrix[couple]
    alignment = "".join(seq_list1) + "\n" + "".join(seq_list2)
    return score, alignment

def seqs_with_gaps(seq1,seq2):
    seq1_list = []
    seq2_list = []
    for i in range((len(seq1)+len(seq2))):
        if i in range(len(seq1)):
            seq1_list.append(seq1[i])
        else:
            seq1_list.append("_")

    for i in range((len(seq1)+len(seq2))):
        if i in range(len(seq2)):
            seq2_list.append(seq2[i])
        else:
            seq2_list.append("_")
    return seq1_list, seq2_list

def alignments_matrix(seqs_lists,seq1,seq2,seq1_list,seq2_list,matrix):
    scores = []
    scores.append(score_alignment(seq1_list,seq2_list, matrix))
    for i in range(len(seq2)):
        for i in range(len(seq1_list)-1,-1,-1):
            if seq1_list[i] != "_":
                seq1_list[i+1] = seq1_list[i]
                seq1_list[i] = "_"
        scores.append(score_alignment(seq1_list,seq2_list, matrix))

    seqs_lists = seqs_with_gaps(seq1,seq2)
    seq1_list = seqs_lists[0]
    seq2_list = seqs_lists[1]

    for i in range(len(seq1)-1):
        for i in range(len(seq2_list)-1,-1,-1):
            if seq2_list[i] != "_":
                seq2_list[i+1] = seq2_list[i]
                seq2_list[i] = "_"
        scores.append(score_alignment(seq1_list,seq2_list, matrix))
    return scores

def max_score(alignments):
    max_score_index = alignments[0]
    max_score = alignments[0][0]
    for i in alignments:
        if i[0] > max_score:
            max_score_index = i
            max_score = i[0]
    return max_score_index

def print_cool_output(max_score):
    print max_score[0]
    flag = True
    seq1 = []
    seq2 = []
    for i in max_score[1]:
        if i == "\n":
            flag = False
        if flag:
            seq1.append(i)
        else:
            seq2.append(i)
    seq2.remove("\n")
    for i in range(len(seq1)):
        

matrix = matrix("nuc_matrix.txt")
seq1 = "TCA"
seq2 = "GA"
seqs_lists = seqs_with_gaps(seq1,seq2)
seq1_list = seqs_lists[0]
seq2_list = seqs_lists[1]
alignments = alignments_matrix(seqs_lists,seq1,seq2,seq1_list,seq2_list,matrix)
print alignments
best_alignment = max_score(alignments)
print_cool_output(best_alignment)
