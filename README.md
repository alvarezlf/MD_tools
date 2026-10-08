# MD Tools
Set of scripts created to analyze and manipulate data obtained from CPMD calculations focusing on the energy and trajectory files.

## enerplot
Plot the energy from CPMD calculations. The options are -cpmd (Car-Parrinello MD, default), -nose (Nosé-Hoover thermostat with corrected energies), -bomd (Born-Oppenheimer MD).
## heat
Contains scripts to calculate the velocity and temperature of specific atoms, calculated as  
$$\frac{mv^2}{3 Nk} = T$$

It may differs from the overall temperature given in the outputs.
## overlapper
Overlaps several steps of a trajectory file into a single step. Useful to project the diffusion of particles through lattices.
## plt_distances
Plot atomic distances with default parameters. A list of values must be obtained with external programs and given in the script.
## ttotfreeze
Recalculate atomic coordinates relative to a given atom obtaining a "freeze" effect for the specified atom.
## ttotshort
Given a list of atoms, divides the specified trajectory file into a "file-main.xyz" and "file-side.xyz". Useful to separate reactive molecules from the solvent. An input template is included.
## ttotw
Given a trajectory file with Wannier centers, separates the atoms from the Wannier centers creating "file-atoms.xyz" and "file-wanc.xyz" files. Useful in the generation of movies.
## xyz2cpmd
Two scripts are provided. mol_center centers molecule to a given cell size. cpmdformat takes the coordinates in a file and convert them to CPMD format (X Y Z At in atomic units)

Have a nice day~  
L. Álvarez.
