from ase.io import read, write

def concatenate_pdb(file1, file2, output_file):
    """
    Concatenates two PDB files into a single PDB file using ASE.
    """
    # Read the individual PDB files into ASE Atoms objects
    atoms1 = read(file1)
    atoms2 = read(file2)
    
    # Combine the two Atoms objects
    combined_atoms = atoms1 + atoms2
    
    # Write the combined structure to the output PDB file
    write(output_file, combined_atoms)
    print(f"Successfully concatenated {file1} and {file2} into {output_file}")

# Example usage
if __name__ == "__main__":
    concatenate_pdb("YSZ.pdb", "FeO.pdb", "system.pdb")
