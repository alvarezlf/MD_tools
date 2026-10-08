def plotter(datafile):
    try:
        data = loadtxt(datafile)
    except:
        print('Error reading file {0}}'.format(datafile))
        return
    col_1=data[:,0]
    if args.timestep:
        x=col_1*2.418884254E-5*args.timestep
    else:
        x=col_1
    col_2=data[:,1]
    col_3=data[:,2]
    col_4=data[:,3]
    col_5=data[:,4]
    col_6=data[:,5]
    col_7=sqrt(data[:,6])
    col_8=data[:,7]

    font1 = {'weight':'bold', 'size':9}
    font2 = {'weight':'regular', 'size':9}

    rcParams['font.size'] = font2['size']
    rcParams['font.weight'] = font2['weight']
    fig, ax = subplots(figsize=(14/2.54,7.88/2.54)) #paper
    ax.tick_params(which='major')
    lwidth=.7
    margin = 0.05 # 5%

    if args.cpmd:
        y1=col_4
        y2=col_5
        y3=col_6
        max_y=max(max(y1), max(y2), max(y3))
        min_y=min(min(y1), min(y2), min(y3))
        Dy = max_y-min_y
        max_y = min_y + Dy * (1.0 + margin)
        min_y = min_y - Dy * margin
        ax.plot(x, y3, lw=lwidth, color='blue', label='E$_{Ham}$')
        ax.plot(x, y2, lw=lwidth, color='red', label='E$_{Classic}$')
        ax.plot(x, y1, lw=lwidth, color='black', label='E$_{KS}$')
        ax.set_ylabel('Energy [a.u.]', fontdict=font1)
        ax.legend(loc='upper right')

    elif args.nose:
        if args.Nparticles:
            N=args.Nparticles
        else:
            print('Number of particles missing for {0}'.format(datafile))
            N = int(input('Number of Particles (first line in trajectory file): '))
        k=3.166811563e-6
        y1=col_4
        y2=col_4+3/2*N*k*col_3
        y3=col_4+3/2*N*k*col_3+col_2
        max_y=max(max(y1), max(y2), max(y3))
        min_y=min(min(y1), min(y2), min(y3))
        Dy = max_y-min_y
        max_y = min_y + Dy * (1.0 + margin)
        min_y = min_y - Dy * margin
        ax.plot(x, y3, lw=lwidth, color='blue', label='E$_{Ham}$')
        ax.plot(x, y2, lw=lwidth, color='red', label='E$_{Classic}$')
        ax.plot(x, y1, lw=lwidth, color='black', label='E$_{KS}$')
        ax.set_ylabel('Energy [a.u.]', fontdict=font1)
        ax.legend(loc='upper right')

    elif args.bomd:
        y1=col_4
        y2=col_5
        max_y=max(max(y1), max(y2))
        min_y=min(min(y1), min(y2))
        Dy = max_y-min_y
        max_y = min_y + Dy * (1.0 + margin)
        min_y = min_y - Dy * margin
        ax.plot(x, y2, lw=lwidth, color='red', label='E$_{Classic}$')
        ax.plot(x, y1, lw=lwidth, color='black', label='E$_{KS}$')
        ax.set_ylabel('Energy [a.u.]', fontdict=font1)
        ax.legend(loc='upper right')

    elif args.temp:
        y1=col_3
        max_y=(max(y1)*1.00//10+1)*10
        min_y=0
        ax.plot(x, y1, lw=lwidth, color='black')
        ax.set_ylabel('Temperature [K]', fontdict=font1)

    elif args.disp:
        y1=col_7
        max_y=max(y1)*1.1
        min_y=0
        ax.plot(x, y1, lw=lwidth, color='black')
        ax.set_ylabel('Displacement [a.u.]', fontdict=font1)

    if args.y_min:
        min_y = args.y_min
    if args.y_max:
        max_y = args.y_max
    ax.set_ylim(min_y, max_y)

    min_x = args.x_min
    if args.x_max:
        max_x = args.x_max
    else:
        max_x = round(x[-1],)

    ax.set_xlabel('MD step', fontdict=font1)

    if args.timestep:
        x_ticks=[i for i in range(int(min_x), round(max_x,)+1)]
        i = 0
        if len(x_ticks) <= 3:
            x_ticks += [i+0.5 for i in range(int(min_x), round(max_x,)+1)]
        ax.set_xticks(x_ticks)
        ax.set_xlabel('Time [ps]', fontdict=font1)

    ax.set_xlim(min_x, max_x)

    max_y=round(max_y+.0499,1)
    min_y=round(min_y-.0499,1)
    D_y=(max_y-min_y)/4
    ax.set_yticks([round(min_y,2), round(min_y+1*D_y,2), round(min_y+2*D_y,2), round(min_y+3*D_y,2), round(min_y+4*D_y,2)])

    ax.ticklabel_format(useOffset=False)

#    ax.set_title(abspath(datafile), fontdict=font2)
    tight_layout()

    if args.save:
        outname=datafile.replace('txt','').replace('.ssv','')+'.svg'
        savefig(outname, format="svg")
        print ('{} saved'.format(outname))
    if not args.no_display:
        show()
    close()
    return

if __name__ == '__main__':
    from argparse import ArgumentParser
    from os.path import abspath
    from numpy import loadtxt, array, sqrt
    from matplotlib.pyplot import rcParams, subplots, show, savefig, tight_layout, close
    from sys import exit

    parser = ArgumentParser()
    parser.add_argument('Datafile', nargs = '*', help="Path(s) to energy file(s).")
    parser.add_argument('-t', '--timestep', type=int, help = 'Molecular Dynamics time step in atomic units.')
    parser.add_argument('-cpmd', action='store_true', default = True, help = 'Plot energies from CPMD calculations.')
    parser.add_argument('-nose', action='store_true', help = 'Plot energies from CPMD calculations using Nosé thermostats. Scpecify the number of particles with -N.')
    parser.add_argument('-bomd', action='store_true', help = 'Plot energies from BOMD calculations.')
    parser.add_argument('-temp', action='store_true', help = 'Plot temperature.')
    parser.add_argument('-disp', action='store_true', help = 'Plot displacement.')
    parser.add_argument('-N', '--Nparticles', type=int)
    parser.add_argument('-s', '--save', action='store_true', help = 'Saves plot as .svg image.')
    parser.add_argument('--x_min', type=float, default = 0)
    parser.add_argument('--x_max', type=float)
    parser.add_argument('--y_min', type=float)
    parser.add_argument('--y_max', type=float)
    parser.add_argument('--no_display', action='store_true', help='Plot is not shown.')

    args = parser.parse_args()

    if  not args.Datafile:
        print("Error: Specify energy file!")
        exit()

    if args.nose or args.bomd or args.temp or args.disp:
        args.cpmd = False

    if (args.cpmd + args.nose + args.bomd + args.temp) >1:
        print('Error: Use -cpmd, -nose, -bomd or -temp to specify only one layout. Default layour: cpmd.')
        exit()

    for dfile in args.Datafile:
        try:
            plotter(dfile)
        except KeyboardInterrupt:
            print('KEYBOARD INTERRUPT!')
            exit()
        except:
            print('Error loading {0}'.format(dfile))
            continue

#Have a nice day ~
#L. Alvarez 2025
