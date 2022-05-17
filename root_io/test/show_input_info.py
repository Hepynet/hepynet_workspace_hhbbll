import collections
import pathlib

import uproot

# Input
input = "/eos/atlas/atlascerngroupdisk/phys-hdbs/diHiggs/bbll/ntuples/220213_nn_input_2tag/2tag_sr1.root:ntup"
#input = "/eos/atlas/atlascerngroupdisk/phys-hdbs/diHiggs/bbll/ntuples/220512_nn_input_2tag_res/2tag_sr1.root:ntup"

# Show branches
with uproot.open(input) as ntup:
    br_list = ntup.branches
    print("##### Branches #####")
    for br in br_list:
        print(br.name)
    arr = ntup.arrays(["process_id"], library="np")
    process_cnt = collections.defaultdict(int)
    for pid in arr["process_id"]:
        process_cnt[pid] += 1
with open("branch_list1.txt", "w") as f:
#with open("branch_list2.txt", "w") as f:
    for br in br_list:
        f.write(br.name + "\n")
with open("process_cnt1.txt", "w") as f:
#with open("process_cnt2.txt", "w") as f:
    for key in sorted(process_cnt.keys()):
        value = process_cnt[key]
        f.write(f"{key} {value}\n")
