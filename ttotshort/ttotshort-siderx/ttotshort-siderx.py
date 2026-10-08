import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

in_list=list()
in_read=open(args.filename, 'r')
in_name=in_read.readline().replace('\n', '')
in_atoms=int(in_read.readline())

for i in in_read:
	if i!= '\n':    
		in_list.append(int(i.replace('\n','')))

side_rx=list()
for i in range (1,in_atoms+1):
	if i not in in_list:
		side_rx.append(i)

out_atoms=len(side_rx)
in_read.close()
####
i_long=open(in_name,'r')
o_short=open(in_name+'siderx','w')
o_short.write('')
o_short.close()
o_short=open(in_name+'siderx','a')

i_list=list()
for i in i_long:
        i_list.append(i)
steps=len(i_list)/(in_atoms+2)
#print ('N of steps  '+str(steps))

for i in range(int(steps)):
        o_short.write(' '*9+str(out_atoms)+'\n')
        o_short.write(' STEP: '+str(i+1)+'\n')
        for j in side_rx:
                o_short.write(i_list[i*(in_atoms+2)+j+1])

i_long.close()
o_short.close()

#pending to change the names so it is not so redundant
