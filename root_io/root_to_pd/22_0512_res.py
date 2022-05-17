import pathlib

import numpy as np
import pandas as pd
import uproot
from configs import *

# Prepare
ntup_dir = pathlib.Path(
    "/eos/atlas/atlascerngroupdisk/phys-hdbs/diHiggs/bbll/ntuples/220512_nn_input_2tag_res"
)
ntup_name = "ntup"
df_dir = pathlib.Path(f"/data1/LOCAL/yangz/hh_bbll_mva/data_frames/22_0512_res")
df_dir.mkdir(parents=True, exist_ok=True)

# Settings
step_size = "200 MB"

# Convert
for region in ["sr1", "sr2", "topcr", "zllcr"]:
    file_path = ntup_dir / f"2tag_{region}.root"
    sample_dfs = list()
    n_events = 0
    print(f"Converting {file_path} with step {step_size} ...")
    for chunk_pd in uproot.iterate(
        f"{file_path}:{ntup_name}", feature_list, library="pd", step_size=step_size
    ):
        n_events += chunk_pd[chunk_pd.columns[0]].count()
        print(f"{n_events} events processed.")
        # convert float64 to float32
        f64_cols = chunk_pd.select_dtypes(include="float64").columns
        chunk_pd[f64_cols] = chunk_pd[f64_cols].astype("float32")
        # tag sample name
        chunk_pd["sample_name"] = chunk_pd["process_id"].map(pid_to_sample)
        # tag sample_type
        sig_condition = (
            (chunk_pd["process_id"] >= 10) & (chunk_pd["process_id"] <= 60)
        ) | ((chunk_pd["process_id"] >= 210) & (chunk_pd["process_id"] <= 282))
        chunk_pd["is_sig"] = np.where(sig_condition, True, False)
        chunk_pd["is_mc"] = np.where(chunk_pd["process_id"] > 0, True, False)
        # add physical parameter
        chunk_pd["m_truth"] = chunk_pd["m_bbllmet"]
        chunk_pd.loc[chunk_pd["is_sig"], "m_truth"] = chunk_pd["truth_mhh"]
        # add to output
        sample_dfs.append(chunk_pd)

        # debug
        test_pd = chunk_pd.sample(n=10)
        result = test_pd.head(10)
        print(str(result))
        # break

    # Merge and save
    print(f"Merging {len(sample_dfs)} chunks...")
    output_df = pd.concat(sample_dfs)
    save_path = df_dir / f"2tag_{region}.feather"
    print(f"Saving to {save_path}...")
    output_df.to_feather(save_path)
