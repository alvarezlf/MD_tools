import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument("a", type=float)
parser.add_argument("b", type=float)
parser.add_argument("c", type=float)

args = parser.parse_args()

ATOMS=list()

A=args.a
B=args.b
C=args.c

X=list()
Y=list()
Z=list()

with open(args.filename, 'r') as xyz_old:
    print(xyz_old.readline().strip())
    print(xyz_old.readline().strip())
    for i in xyz_old:
        line=i.replace('\n','').split()
        ATOMS.append(line[0])
        X.append(float(line[1]))
        Y.append(float(line[2]))
        Z.append(float(line[3]))

X_MIN=(A-max(X)+min(X))/2
Y_MIN=(B-max(Y)+min(Y))/2
Z_MIN=(C-max(Z)+min(Z))/2
DX=X_MIN-min(X)
DY=Y_MIN-min(Y)
DZ=Z_MIN-min(Z)
for j in range(len(X)):
        text=' '+ATOMS[j]+' '*(3-len(ATOMS[j]))
        text+=' '*(15-len(format(X[j]+DX, '.5f')))+format(X[j]+DX, '.5f')
        text+=' '*(15-len(format(Y[j]+DY, '.5f')))+format(Y[j]+DY, '.5f')   
        text+=' '*(15-len(format(Z[j]+DZ, '.5f')))+format(Z[j]+DZ, '.5f')   
        print(text)
