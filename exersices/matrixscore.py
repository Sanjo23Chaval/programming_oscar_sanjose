def find_frequence (seq1, seq2):
    n_nucleotides= len(seq1) + len(seq2)
    d_residues= {}
    for i in range(len(seq1)):
        d_residues[seq1[i]]= d_residues.get(seq1[i],0)+1
        d_residues[seq2[i]]= d_residues.get(seq2[i],0)+1
    for i in d_residues.keys():
        d_residues[i]= d_residues[i]/float(n_nucleotides)
    return d_residues

def observed_value (seq1,seq2):
    raw_dict={}
    prob_dict={}
    for i in range(len(seq1)):
        couple= seq1[i] +seq2[i]
        raw_dict[couple]= raw_dict.get(couple,0)+1
    for i in raw_dict.keys():
        rkey= i[::-1]
        if rkey in raw_dict:
            prob_dict[i]= 1+(raw_dict[i]+raw_dict[rkey])/float(len(seq1))
        else:
            prob_dict[i]= 1+(raw_dict[i])/float(len(seq1))
    return prob_dict

def add_nonobserved (dicti):
    col_raw= "ATGC"
    for letter in col_raw:
        for letter1 in col_raw:
            if letter+letter1 not in dicti.keys():
                if letter1+letter in dicti.keys():
                    dicti[letter+letter1] = dicti[letter1+letter]
                else:
                    dicti[letter+letter1] = 1
    return dicti

def log_odd (dicti1,dicti2):
    from math import log10
    list_key= dicti1.keys()
    list_key.sort()
    total_list=[]
    for el in list_key:
        score= log10((dicti1[el])/(dicti2[(el[0])]*dicti2[(el[1])]))
        total_list.append(score)
    for el in range(0,len(total_list),4):
        print total_list[el], total_list[el+1],total_list[el+2], total_list[el+3]

sequence1="ACAGGTGGACCTCTATATGG"
sequence2="ACTGGTCGACTTCCGGATCG"

d_frequences= find_frequence(sequence1,sequence2)
print d_frequences
dictionary=observed_value(sequence1,sequence2)
sorted_d= add_nonobserved(dictionary)
log_odd(sorted_d, d_frequences)
