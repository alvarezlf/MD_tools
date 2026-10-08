import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
parser.add_argument("-a", "--a_lenght", type=float)

args = parser.parse_args()

input_name = args.filename

xyz_old=open(input_name, 'r')
ATOMS=list()
X=list()
Y=list()
Z=list()

#### CONVERSION FACTOR #####
conv=1
#conv=1/0.529177	#A to a.u.
############################

for i in xyz_old:
	line=i.replace('\n','').split()
	ATOMS.append(line[0])
	X.append(float(line[1])*conv)
	Y.append(float(line[2])*conv)
	Z.append(float(line[3])*conv)
xyz_old.close()

a=max(X)-min(X)
b=max(Y)-min(Y)
c=max(Z)-min(Z)

if type(args.a_lenght)==float:
	a=args.a_lenght; b=a; c=a

X_MIN=(a-max(X)+min(X))/2
Y_MIN=(b-max(Y)+min(Y))/2
Z_MIN=(c-max(Z)+min(Z))/2
DX=X_MIN-min(X)
DY=Y_MIN-min(Y)
DZ=Z_MIN-min(Z)

for j in range(len(X)):
        text=' '*4
        text+=' '*(8-len(format(X[j]+DX, '.4f')))+format(X[j]+DX, '.4f')
        text+=' '*(8-len(format(Y[j]+DY, '.4f')))+format(Y[j]+DY, '.4f')   
        text+=' '*(8-len(format(Z[j]+DZ, '.4f')))+format(Z[j]+DZ, '.4f')   
        text+=' '*4+ATOMS[j]
        print(text)
