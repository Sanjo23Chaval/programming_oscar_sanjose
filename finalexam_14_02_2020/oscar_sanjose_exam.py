#Exersice A
def NW_matrices(seq1,seq2,BLOSUM52,gap_value):
    rows = len(seq2) + 1
    columns = len(seq1) + 1
    F = [[0] * columns for i in range(rows)]
    P = [["S"] * columns for i in range(rows)]
    for i in range(1,len(F)):
        F[i][0] = gap_value*i
        P[i][0] = "N"
    for z in range(1,len(F[0])):
        F[0][z] = gap_value*z
        P[0][z] = "W"
    for i in range(1,len(F)):
        for z in range(1,len(F[0])):
            N = F[i-1][z] + gap_value
            W = F[i][z-1] + gap_value
            NW = F[i-1][z-1] + BLOSUM52[seq1[z-1]+seq2[i-1]]
            maximo = max(N,W,NW)
            if maximo == NW:
                F[i][z] = NW
                P[i][z] = "NW"
            elif maximo == N:
                F[i][z] = N
                P[i][z] = "N"
            else:
                F[i][z] = W
                P[i][z] = "W"
    return F,P
#Exersice B
def retrieve_align(F,P,seq1,seq2):
    seq1a = []
    seq2a = []
    last_row = len(F)-1
    last_col = len(F[0])-1
    starting_pos = [last_row,last_col]
    score = F[last_row][last_col]
    while P[starting_pos[0]][starting_pos[1]] != "S":
            if P[starting_pos[0]][starting_pos[1]] == "NW":
                seq1a.append(seq1[starting_pos[1]-1])
                seq2a.append(seq2[starting_pos[0]-1])
                starting_pos[0] -= 1
                starting_pos[1] -= 1
            elif P[starting_pos[0]][starting_pos[1]] == "N":
                seq1a.append("-")
                seq2a.append(seq2[starting_pos[0]-1])
                starting_pos[0] -= 1
            else:
                seq2a.append("-")
                seq1a.append(seq1[starting_pos[1]-1])
                starting_pos[1] -= 1
    return "".join(seq1a)[::-1],"".join(seq2a)[::-1],score
#Exersice C
from input_file import seq1,seq2,BLOSUM52
a = NW_matrices(seq1,seq2,BLOSUM52,-2) # I put -2 gap penalty, but it could be whatever
b= retrieve_align(a[0],a[1],seq1,seq2)
print b[0],"\n",b[1],"\n",b[2]
