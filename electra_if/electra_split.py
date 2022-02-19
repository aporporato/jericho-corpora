import json

import pandas as pd

data = pd.read_csv('actions_stripped_set_sorted_aug-ann.csv', sep=';', header=0)
base = pd.read_csv('common_commands.csv', sep=';')
base_action = set([s.replace('_', ' ').lower() for c in base['VERB'].tolist() if not pd.isna(c) for s in c.split(',')])
base_action.union([s.lower() for c in base['ABBR'].tolist() if not pd.isna(c) for s in c.split(',')])
base_wn = set([s.lower() for c in base['WN_OFFSET'].tolist() if not pd.isna(c) for s in c.split(',')])
base_vn = set([s.lower() for c in base['VERBNET'].tolist() if not pd.isna(c) for s in c.split(',')])
base_fn = set([s.lower() for c in base['FRAMENET'].tolist() if not pd.isna(c) for s in c.split(',')])

wn_dict = {}
vn_dict = {}
fn_dict = {}
npc_dict = {}
for index, row in data.iterrows():
    # Wordnet
    wn_offsets = row['WN_OFFSET']
    if pd.isna(row['WN_OFFSET']):
        wn_offsets = 'null'
    wn_offsets = wn_offsets.split(',')
    for wn_offset in wn_offsets:
        if wn_offset not in wn_dict.keys():
            wn_dict[wn_offset] = []
        wn_dict.get(wn_offset).append(row['ACTION'])
    # Verbnet
    vn_offsets = row['VERBNET']
    if pd.isna(row['VERBNET']):
        vn_offsets = 'null'
    vn_offsets = vn_offsets.split(',')
    for vn_offset in vn_offsets:
        if vn_offset not in vn_dict.keys():
            vn_dict[vn_offset] = []
        vn_dict.get(vn_offset).append(row['ACTION'])
    # Framenet
    fn_offsets = row['FRAMENET']
    if pd.isna(row['FRAMENET']):
        fn_offsets = 'null'
    fn_offsets = fn_offsets.split(',')
    for fn_offset in fn_offsets:
        if fn_offset not in fn_dict.keys():
            fn_dict[fn_offset] = []
        fn_dict.get(fn_offset).append(row['ACTION'])
    # Third person command
    npc_offsets = row['NPC']
    if pd.isna(row['NPC']):
        npc_offsets = 'null'
    else:
        npc_offsets = str(int(npc_offsets))
    npc_offsets = npc_offsets.split(',')
    for npc_offset in npc_offsets:
        if npc_offset not in npc_dict.keys():
            npc_dict[npc_offset] = []
        npc_dict.get(npc_offset).append(row['ACTION'])

with open("wn\\wn_full.json", "w") as file:
    file.write(json.dumps(wn_dict, indent=2))

with open("wn\\wn.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in wn_dict.items() if len(v) >= 5 or k in base_wn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("wn\\wn_base.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in wn_dict.items() if k in base_wn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("vn\\vn_full.json", "w") as file:
    file.write(json.dumps(vn_dict, indent=2))

with open("vn\\vn.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in vn_dict.items() if len(v) >= 5 or k in base_vn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("vn\\vn_base.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in vn_dict.items() if k in base_vn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("fn\\fn_full.json", "w") as file:
    file.write(json.dumps(fn_dict, indent=2))

with open("fn\\fn.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in fn_dict.items() if len(v) >= 5 or k in base_fn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("fn\\fn_base.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in fn_dict.items() if k in base_fn or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("npc\\npc_full.json", "w") as file:
    file.write(json.dumps(npc_dict, indent=2))

with open("npc\\npc.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in npc_dict.items() if len(v) >= 5 or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))

with open("npc\\npc_base.json", "w") as file:
    file.write(json.dumps({k: v for (k, v) in npc_dict.items() if len(v) >= 5 or \
                           len(set(v).intersection(base_action)) > 0}, indent=2))
