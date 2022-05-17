import pandas as pd
import numpy as np
# Input
input_pd = "/data1/LOCAL/yangz/hh_bbll_mva/data_frames/22_0512_res/2tag_sr1.feather"
df = pd.read_feather(input_pd)
pid_dict = {
    11: "sig_res_251_bbWW",
    12: "sig_res_260_bbWW",
    13: "sig_res_300_bbWW",
    14: "sig_res_400_bbWW",
    15: "sig_res_500_bbWW",
    16: "sig_res_600_bbWW",
    17: "sig_res_800_bbWW",
    18: "sig_res_1000_bbWW",
    21: "sig_res_251_bbtautau",
    22: "sig_res_260_bbtautau",
    23: "sig_res_300_bbtautau",
    24: "sig_res_400_bbtautau",
    25: "sig_res_500_bbtautau",
    26: "sig_res_600_bbtautau",
    27: "sig_res_800_bbtautau",
    28: "sig_res_1000_bbtautau",
    31: "sig_res_251_bbZZ",
    32: "sig_res_260_bbZZ",
    33: "sig_res_300_bbZZ",
    34: "sig_res_400_bbZZ",
    35: "sig_res_500_bbZZ",
    36: "sig_res_600_bbZZ",
    37: "sig_res_800_bbZZ",
    38: "sig_res_1000_bbZZ",
}

for sample in pid_dict.values():
    wt = df[df["sample_name"] == sample]["weight"]
    print(f"Total weight for {sample}: {np.sum(wt)}")
