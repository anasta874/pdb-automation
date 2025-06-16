input_pdb = "2VOZ_chainC_NAG.pdb"
output_pdb = "renumbered_2VOZ_chainC_NAG.pdb"

# Мапа старых номеров к новым — начинаем с 67
res_map = {}
new_resi = 67

with open(input_pdb, 'r') as infile, open(output_pdb, 'w') as outfile:
    for line in infile:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            res_no = line[22:26].strip()
            key = (line[21], res_no)  # (chain, residue_number)

            if key not in res_map:
                res_map[key] = new_resi
                new_resi += 1

            new_line = line[:22] + f"{res_map[key]:>4}" + line[26:]
            outfile.write(new_line)
        else:
            outfile.write(line)


