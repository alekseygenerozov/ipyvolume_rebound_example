import rebound 

import numpy as np
import sys
import shlex
import matplotlib.pyplot as plt
import subprocess

def bash_command(cmd):
	'''Run command from the bash shell'''
	process=subprocess.Popen(['/bin/bash', '-c',cmd],  stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	return process.communicate()[0]

##Load simulation archive at a user specified location
loc=sys.argv[1]
sa=rebound.SimulationArchive(loc+'/archive.bin')
frames=len(sa)
##Number of points per orbit
pts=200
##Number of particles (excluding the central body)
samp=sa[0].particles
##Arrays storing xyz positions of all particle 
x=np.empty([frames, len(samp)-1, pts+1])
y=np.empty([frames, len(samp)-1, pts+1])
z=np.empty([frames, len(samp)-1, pts+1])
##New simulation object; Will sample orbits 
##one at a time add them to simulation archive. 
sim=rebound.Simulation()

for idx in range(frames):
	##Load snapshot data from simulation archive
	sim0=sa[idx]
	parts=sim0.particles
	##Adding central body (I believe we all follow the convention
	##that the most massive body would be the central one).
	sim.add(x=parts[0].x, y=parts[0].y, z=parts[0].z,\
		vx=parts[0].vx, vy=parts[0].vy, vz=parts[0].vz, m=parts[0].m)

	for i in range(1, len(parts)):
		##Add data for one of the bodies
		sim.add(x=parts[i].x, y=parts[i].y, z=parts[i].z,\
			vx=parts[i].vx, vy=parts[i].vy, vz=parts[i].vz, m=parts[i].m)
		##Sampling orbit
		p=sim.particles[1]
		pos=np.array(p.sample_orbit(pts, primary=sim.particles[0]))
		
		sim.remove(1)
		##Insert nans; Otherwise all of the orbits would be connected!!
		x[idx,i-1,:-1] = pos[:,0]
		x[idx,i-1][-1]=np.nan
		y[idx,i-1,:-1] = pos[:,1]
		y[idx,i-1][-1]=np.nan
		z[idx,i-1,:-1] = pos[:,2]
		z[idx,i-1][-1]=np.nan

##Save the x,y,z data
np.savez(loc+'/x.npz', x)
np.savez(loc+'/y.npz', y)
np.savez(loc+'/z.npz', z)
