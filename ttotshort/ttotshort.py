import argparse

parser = argparse.ArgumentParser()
parser.add_argument('INPUT', type=str)
args = parser.parse_args()

in_list=list()
with open(args.INPUT, 'r') as INPUT:
    in_traj=INPUT.readline().strip()
    in_atoms=int(INPUT.readline().strip())
    main_list=[int(line.strip()) for line in INPUT if not (line.startswith('#') or line.startswith('\n'))]
main_list.sort()
out_Nmain=len(main_list)

with open(in_traj,'r') as i_long:
    i_list=i_long.readlines()
steps=len(i_list)//(in_atoms+2)

with open(in_traj.replace('.xyz','')+'-main.xyz','w') as out_traj:
    for i in range(steps):
        out_traj.write(str(out_Nmain)+'\n')
        out_traj.write('  STEP: {0}\n'.format(i+1))
        for j in main_list:
                out_traj.write(i_list[i*(in_atoms+2)+j+1])

side_list=[i for i in range(1, in_atoms+1) if not i in main_list]
out_Nside=len(side_list)
with open(in_traj.replace('.xyz','')+'-side.xyz','w') as out_side:
    for i in range(steps):
        out_side.write(str(out_Nside)+'\n')
        out_side.write('  STEP: {0}\n'.format(i+1))
        for j in side_list:
                out_side.write(i_list[i*(in_atoms+2)+j+1])

######################
#INPUT TEMPLATE
######################
# TARJECTORY_FILE.xyz   Line 1: trajectory file to short
# N                     Line 2: number of atoms in the cell
#                       You can leave empty spaces as separations or # for comments
# 1                     Line 4 list of atoms to keep. 1 atom per line. 
# 2                     The numbering corresponds to their position in the trajectory file.
# ...                   Note that VMD begins numbering from 0!
######################
