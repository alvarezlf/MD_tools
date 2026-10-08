import argparse

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
    description='This program generates a file with the velocities in [a.u.] of every atom in a trajectory file. To use it, execute: "$ python tra2vel.py FILE_NAME -t TIMESTEP > OUTPUT_NAME"')
parser.add_argument('filename')
parser.add_argument("-t", "--timestep", type=str)
args = parser.parse_args()

input_name = args.filename
TIMESTEP = float(args.timestep)

in_file = list()
input_file = open(input_name, 'r')
for i in input_file:
	in_file.append(i.replace('\n',''))
input_file.close()

atoms =int(in_file[0]) # total amount of atoms
steps =len(in_file)/(atoms+2)

C_0 =list()

for step in range (1,int(steps)):
	C_1=list()
	print(' '*9+str(atoms))
	print()
	for atom in range (atoms):
		C_0=in_file[(step-1)*(atoms+2)+(atom+2)].split()
		C_1=in_file[(step)*(atoms+2)+(atom+2)].split()
		rate =((float(C_1[1])-float(C_0[1]))**2+(float(C_1[2])-float(C_0[2]))**2+(float(C_1[3])-float(C_0[3]))**2)**0.5/TIMESTEP/10#/.529177
		print(' '+C_0[0]+' '*4+f'{rate:e}')
