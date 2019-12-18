def seq_score(seq1,seq2):
    if len(seq1) == len(seq2):
        score = 0
        for i in range(len(seq1)):
            if seq1[i] == seq2[i]:
                score += 1
            else:
                score -= 1
        return score
    else:
        return False

seq1 = raw_input("Write a DNA sequence: ")
seq2 = raw_input("Write a DNA sequence: ")

print seq_score(seq1,seq2)
