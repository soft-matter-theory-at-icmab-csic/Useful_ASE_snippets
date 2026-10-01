from ase.io import read, write
from ase.build import make_supercell

# --- USER PARAMETERS ---

# Input PDB file
input_pdb = "FeO.cif"

# Repetition along x, y, z 
repeat = (3, 3, 3)

# Output file
output_file = "FeO_repeated.pdb"

# ------------------------

# Step 1: Load the PDB structure
atoms = read(input_pdb)

# Step 2: Repeat the unit cell
atoms_repeated = atoms.repeat(repeat)

# Step 3: Save the repeated structure
write(output_file, atoms_repeated)

print(f"Repeated structure saved to {output_file}")
