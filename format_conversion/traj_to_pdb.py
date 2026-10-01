
#reading and writing structures and trajectories
from ase.io import write, read
from ase.io import Trajectory, trajectory

#Convert trajectory from traj to pdb
# Load all frames from the trajectory
frames = read("./run.traj", ":")

# Write a PDB trajectory file for VMD
write("./runtraj.pdb", frames)
