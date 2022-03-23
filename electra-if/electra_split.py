import json

import pandas as pd

data = pd.read_csv('actions_stripped_set_sorted_aug-ann.csv', sep=';', header=0)
base = pd.read_csv('common_commands.csv', sep=';')
base_action = set([s.replace('_', ' ').lower() for c in base['VERB'].tolist() if not pd.isna(c) for s in c.split(',')])
base_action.union([s.lower() for c in base['ABBR'].tolist() if not pd.isna(c) for s in c.split(',')])
base_wn = set([s.lower() for c in base['WORDNET'].tolist() if not pd.isna(c) for s in c.split(',')])
base_vn = set([s.lower() for c in base['VERBNET'].tolist() if not pd.isna(c) for s in c.split(',')])
base_fn = set([s.lower() for c in base['FRAMENET'].tolist() if not pd.isna(c) for s in c.split(',')])

wn_dict = {}
vn_dict = {}
fn_dict = {}
npc_dict = {}
for index, row in data.iterrows():
    # Wordnet
    wn_labels = row['WORDNET']
    if pd.isna(row['WORDNET']):
        wn_labels = 'unknown'
    wn_labels = wn_labels.split(',')
    for wn_label in wn_labels:
        if wn_label not in wn_dict.keys():
            wn_dict[wn_label] = []
        wn_dict.get(wn_label).append(row['ACTION'])
    # Verbnet
    vn_labels = row['VERBNET']
    if pd.isna(row['VERBNET']):
        vn_labels = 'unknown'
    vn_labels = vn_labels.split(',')
    for vn_label in vn_labels:
        if vn_label not in vn_dict.keys():
            vn_dict[vn_label] = []
        vn_dict.get(vn_label).append(row['ACTION'])
    # Framenet
    fn_labels = row['FRAMENET']
    if pd.isna(row['FRAMENET']):
        fn_labels = 'unknown'
    fn_labels = fn_labels.split(',')
    for fn_label in fn_labels:
        if fn_label not in fn_dict.keys():
            fn_dict[fn_label] = []
        fn_dict.get(fn_label).append(row['ACTION'])
    # Third person command
    npc_labels = row['NPC']
    if pd.isna(row['NPC']):
        npc_labels = 'unknown'
    else:
        npc_labels = str(int(npc_labels))
    npc_labels = npc_labels.split(',')
    for npc_label in npc_labels:
        if npc_label not in npc_dict.keys():
            npc_dict[npc_label] = []
        npc_dict.get(npc_label).append(row['ACTION'])

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
