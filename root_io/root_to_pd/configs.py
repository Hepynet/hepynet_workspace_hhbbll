# General
MB = 1024 * 1024
GB = MB * 1024

# Ntuple
feature_list = [
    "event_number",
    "is_sf",
    "n_electrons",
    "n_mus",
    "process_id",
    "vbf_veto",
    "lept_0_pt",
    "lept_0_eta",
    "lept_0_phi",
    "lept_1_pt",
    "lept_1_eta",
    "lept_1_phi",
    "bjet_0_pt",
    "bjet_0_eta",
    "bjet_0_phi",
    "bjet_1_pt",
    "bjet_1_eta",
    "bjet_1_phi",
    "ll_m",
    "ll_pt",
    "ll_deltar",
    "ll_deltaphi",
    "bb_m",
    "bb_pt",
    "bb_deltar",
    "bb_deltaphi",
    "deltar_min_bl",
    "met_met",
    "met_phi",
    "met_sig",
    "mmc_mlnu3p",
    "mmc_status",
    "mt_lep0_met",
    "mt_lep1_met",
    "mt_l_min",
    "mcoll",
    "met_phi_centrality",
    "dphi_met_ll",
    "sum_met_ptll",
    "ht2r",
    "pt_bbll_vector",
    "m_bbll",
    "m_bl",
    "pt_bbllmet_vector",
    "m_bbllmet",
    "m_t2_bb",
    "m_top",
    "klf_status",
    "truth_mhh",
    "weight",
]

# Process ID to sample name
pid_to_sample = {
    -1: "unknown",
    0: "data",
    10: "sig_nonres_bbWW",
    11: "sig_res_251_bbWW",
    12: "sig_res_260_bbWW",
    13: "sig_res_300_bbWW",
    14: "sig_res_400_bbWW",
    15: "sig_res_500_bbWW",
    16: "sig_res_600_bbWW",
    17: "sig_res_800_bbWW",
    18: "sig_res_1000_bbWW",
    19: "sig_kl10_bbWW",
    20: "sig_nonres_bbtautau",
    21: "sig_res_251_bbtautau",
    22: "sig_res_260_bbtautau",
    23: "sig_res_300_bbtautau",
    24: "sig_res_400_bbtautau",
    25: "sig_res_500_bbtautau",
    26: "sig_res_600_bbtautau",
    27: "sig_res_800_bbtautau",
    28: "sig_res_1000_bbtautau",
    29: "sig_kl10_bbtautau",
    30: "sig_nonres_bbZZ",
    31: "sig_res_251_bbZZ",
    32: "sig_res_260_bbZZ",
    33: "sig_res_300_bbZZ",
    34: "sig_res_400_bbZZ",
    35: "sig_res_500_bbZZ",
    36: "sig_res_600_bbZZ",
    37: "sig_res_800_bbZZ",
    38: "sig_res_1000_bbZZ",
    39: "sig_kl10_bbZZ",
    40: "sig_nonres_bbWW_1lep",
    50: "sig_nonres_bbtautau_0lep",
    51: "sig_nonres_bbtautau_1lep",
    60: "sig_nonres_bbyy",
    100: "bkg_prompt_top_ttbar",
    101: "bkg_prompt_top_stop",
    102: "bkg_prompt_top_ttbarV",
    110: "bkg_prompt_Zee",
    111: "bkg_prompt_Zmm",
    112: "bkg_prompt_Ztt",
    120: "bkg_prompt_diboson",
    130: "bkg_nonprompt",
    131: "bkg_ddFakes_data",
    132: "bkg_ddFakes_mc_prompt",
    140: "bkg_prompt_Higgs",
    210: "sig_vbf_old_bbWW",
    220: "sig_vbf_old_bbtautau",
    230: "sig_vbf_old_bbZZ",
    211: "sig_vbf_novhh_l1cvv1cv1_bbWW",
    212: "sig_vbf_novhh_l1cvv0cv1_bbWW",
    213: "sig_vbf_novhh_l1cvv0p5cv1_bbWW",
    214: "sig_vbf_novhh_l1cvv1p5cv1_bbWW",
    215: "sig_vbf_novhh_l1cvv2cv1_bbWW",
    216: "sig_vbf_novhh_l1cvv3cv1_bbWW",
    217: "sig_vbf_novhh_l0cvv1cv1_bbWW",
    218: "sig_vbf_novhh_l2cvv1cv1_bbWW",
    219: "sig_vbf_novhh_l10cvv1cv1_bbWW",
    240: "sig_vbf_novhh_l1cvv1cv0p5_bbWW",
    241: "sig_vbf_novhh_l1cvv1cv1p5_bbWW",
    242: "sig_vbf_novhh_l0cvv0cv1_bbWW",
    221: "sig_vbf_novhh_l1cvv1cv1_bbtautau",
    222: "sig_vbf_novhh_l1cvv0cv1_bbtautau",
    223: "sig_vbf_novhh_l1cvv0p5cv1_bbtautau",
    224: "sig_vbf_novhh_l1cvv1p5cv1_bbtautau",
    225: "sig_vbf_novhh_l1cvv2cv1_bbtautau",
    226: "sig_vbf_novhh_l1cvv3cv1_bbtautau",
    227: "sig_vbf_novhh_l0cvv1cv1_bbtautau",
    228: "sig_vbf_novhh_l2cvv1cv1_bbtautau",
    229: "sig_vbf_novhh_l10cvv1cv1_bbtautau",
    270: "sig_vbf_novhh_l1cvv1cv0p5_bbtautau",
    271: "sig_vbf_novhh_l1cvv1cv1p5_bbtautau",
    272: "sig_vbf_novhh_l0cvv0cv1_bbtautau",
    231: "sig_vbf_novhh_l1cvv1cv1_bbZZ_2l2v",
    283: "sig_vbf_novhh_l1cvv1cv1_bbZZ_2l2q",
    232: "sig_vbf_novhh_l1cvv0cv1_bbZZ",
    233: "sig_vbf_novhh_l1cvv0p5cv1_bbZZ",
    234: "sig_vbf_novhh_l1cvv1p5cv1_bbZZ",
    235: "sig_vbf_novhh_l1cvv2cv1_bbZZ",
    236: "sig_vbf_novhh_l1cvv3cv1_bbZZ",
    237: "sig_vbf_novhh_l0cvv1cv1_bbZZ",
    238: "sig_vbf_novhh_l2cvv1cv1_bbZZ",
    239: "sig_vbf_novhh_l10cvv1cv1_bbZZ",
    280: "sig_vbf_novhh_l1cvv1cv0p5_bbZZ",
    281: "sig_vbf_novhh_l1cvv1cv1p5_bbZZ",
    282: "sig_vbf_novhh_l0cvv0cv1_bbZZ",
    1100: "sys_top_ttbar_fastsim",
    1101: "sys_top_ttbar_PowhegHerwig7",
    1102: "sys_top_ttbar_aMCatNLOPythia8",
    1103: "sys_top_ttbar_hdamp517p5",
    1104: "sys_top_stop_PowhegPythia8_DS_Wt",
    1110: "sys_Zee_MGPy8",
    1111: "sys_Zmm_MGPy8",
}
