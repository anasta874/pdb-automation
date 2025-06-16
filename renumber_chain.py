input_pdb = "2VOZ_chainC_NAG.pdb"
output_pdb = "renumbered_2VOZ_chainC_NAG.pdb"

# Начальный номер
new_resi = 67

# Уникальные остатки будут отслеживаться по (chain, resSeq, iCode)
residue_tracker = {}

with open(input_pdb, 'r') as infile, open(output_pdb, 'w') as outfile:
    for line in infile:
        if line.startswith(("ATOM", "HETATM")):
            chain_id = line[21]
            res_seq = line[22:26].strip()  # residue number (could include insertion codes)
            i_code = line[26]              # insertion code (column 27)

            # Use full key including insertion code
            key = (chain_id, res_seq, i_code)

            if key not in residue_tracker:
                residue_tracker[key] = new_resi
                new_resi += 1

            new_line = (
                line[:22] +
                f"{residue_tracker[key]:>4}" +  # new residue number
                line[26:]
            )
            outfile.write(new_line)
        else:
            outfile.write(line)



