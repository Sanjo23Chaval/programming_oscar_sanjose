def read_row_column(text):
    f = open(text,"r")
    info = f.readline()
    info = info.rstrip()
    info = info.split()
    for i in range(len(info)):
        if info[i] == "rows":
            rows = info[i+2]
            rows = list(rows)
            if "," in rows:
                rows.remove(",")
        elif info[i] == "cols":
            cols = info[i+2]
            cols = list(cols)
            if "," in cols:
                cols.remove(",")
    return rows, cols, f

def pairs_from_matrix(rows, cols, file):
    matrix = {}
    col = 0
    for line in file:
        line = line.split()
        for z in range(len(line)):
            matrix[rows[z]+cols[col]] = line[z].replace(".","")
        col += 1
    return matrix

def fill_rest_matrix(matrix):
    for i in matrix.keys():
        if i[::-1] not in matrix.keys():
            matrix[i[::-1]] = matrix[i]
    return matrix

A = read_row_column("PAM.txt")
B = pairs_from_matrix(A[0], A[1], A[2])
C = fill_rest_matrix(B)
print C["TW"],C["WW"],C["WT"]
