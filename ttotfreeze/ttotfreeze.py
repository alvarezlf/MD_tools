def get_metadata(filename):
        with open(filename, 'r') as traj_file:
            N = int(traj_file.readline().strip())
            traj_lines = sum(1 for i in traj_file)+1
        S = int(traj_lines/(N + 2))
        return N, S
    
def step2coor(filename, N):
    line1 = filename.readline()
    line2 = filename.readline()
    coor = [filename.readline().split() for i in range(N)]
    return line1.strip(), line2.strip(), coor

def freeze_atom(coor_step, ID, N):
    coords = np.array([i[1:4] for i in coor_step]).astype(float)
    coords_frozen = coords - coords[ID]
    coords_new = [[coor_step[i][0]] + list(coords_frozen[i].round(4)) for i in range(N)]
    return coords_new

def print_coords(l1, l2, coords_new):
    print(l1)
    print(l2)
    for i in coords_new:
        print(f"      {i[0]:<2}{i[1]:>12}{i[2]:>12}{i[3]:>12}")

def ttotfreze():
    import numpy as np
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('trajectory', 
                        type=str, 
                        help='Path to trajectory file in .xyz format')
    parser.add_argument('ID', 
                        type=int, 
                        help='ID of the target atom')
    args = parser.parse_args()
    
    traj_N, traj_S = get_metadata(args.trajectory)
    if args.ID > traj_N or args.ID <= 0:
        print("Wrong ID")
        exit()

    with open(args.trajectory, 'r') as traj_file:
        for i in range(traj_S):
                md1, md2, stepcoords = step2coor(traj_file, traj_N)
                print_coords(md1, md2, freeze_atom(stepcoords, args.ID-1, traj_N))
    

if __name__=='__main__':
    ttotfreze()
    
# ~ Have a nice day ~
# L. Álvarez
# 10.2026
