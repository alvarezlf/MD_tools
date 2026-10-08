import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str)
parser.add_argument('interval', type=int)
args = parser.parse_args()

# def skip_line(N, inter, fname):
#     skipping=(N+1)*(inter-1)
#     for i in range(skipping):
#         fname.readline()
#
# def write_line(N, fname):
#     fname.readline()
#     fname.readline()
#     for i in range(N-2):
#         print(fname.readline().strip())

def overlapper():
    in_list=list()
    with open(args.filename,'r') as original:
        for line in original:
            in_list.append(line.strip())
    # print(len(in_list))
    traj_N=int(in_list[0])
    traj_S=len(in_list)/(traj_N+2)
    curr_step=0
    while curr_step<traj_S:
        curr_coords=curr_step*(traj_N+2)
        for i in range(traj_N):
            print(in_list[2+i+curr_coords])
        curr_step+=args.interval


if __name__ == "__main__":
    overlapper()

# in_list=list()
# with open(args.filename,'r') as original:
#     for line in original:
#         in_list.append(line.strip())
# print(len(in_list))
# traj_N=int(in_list[0])
# traj_S=len(in_list)/(traj_N+2)
# curr_step=0
# while curr_step<=traj_S:
#     for i in range(traj_N):
#         curr_coords=curr_step*(traj_N+2)
#         print(in_list[2+i+curr_coords])
#     curr_step+=args.interval
