import pathlib
import uproot


# Input
input = "/eos/atlas/atlascerngroupdisk/phys-hdbs/diHiggs/bbll/ntuples/220213_nn_input_2tag/2tag_sr1.root:ntup"
input = 

# Show branches
with uproot.open(input) as ntup:
    br_list = ntup.branches
    for br in br_list:
        print(br.name)
with open("branch_list2.txt", "w") as f:
    for br in br_list:
        f.write(br.name + "\n")
