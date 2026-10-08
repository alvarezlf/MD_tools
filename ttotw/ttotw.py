import argparse

parser = argparse.ArgumentParser()
parser.add_argument('TRAJECTORY', type=str)
#parser.add_argument('N', type=int)
args = parser.parse_args()

traj_name=args.TRAJECTORY
atom_name=args.TRAJECTORY.replace('.xyz','')+'-atoms.xyz'
wann_name=args.TRAJECTORY.replace('.xyz','')+'-wancs.xyz'
#traj_N=args.N

with open(traj_name,'r') as traj_inp, open(atom_name,'w') as atom_out, open(wann_name,'w') as wann_out:
    step=1
    traj_list=[traj_inp.readline()]
    traj_N=int(traj_inp[0])
    traj_list+=[traj_inp.readline() for _ in range(traj_N+1)][2:]
    while traj_list[0]:
        atom_list=[i for i in traj_list if not i.strip().startswith('X')]
        atom_N=len(atom_list)
        wann_list=[i for i in traj_list if i.strip().startswith('X')]
        wann_N=len(wann_list)
        atom_out.write('{0}\n'.format(atom_N))
        atom_out.write('STEP: {0}\n'.format(step))
        for i in atom_list:
            atom_out.write(i)
        wann_out.write('{0}\n'.format(wann_N))
        wann_out.write('STEP: {0}\n'.format(step))
        for i in wann_list:
            wann_out.write(i)
        step+=1
        traj_list=[traj_inp.readline() for _ in range(traj_N+2)][2:]
