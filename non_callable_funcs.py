'''
    this function is needed because some items dont have unique descriptions for example stickes and when requesting the api the asset-list will
    have more elements than the description-list and so you need to do some formatting also iam just interested in  weapon skins
    and the functions helps with that too. the return is a list of indices of all the relevant items for the asset-list and description-list
    but it also not a function that would be useful to a user so i put it in here so its not callable through the original class
'''

import numpy as np

def relevant_indices(inv_response):
    id_array = []
    for asset in range(len(inv_response["assets"])):
        id_array.append([inv_response["assets"][asset]["classid"], inv_response["assets"][asset]["instanceid"]])
    
    description_indices = []
    non_relevant_items = []
    for description in range(len(inv_response["descriptions"])):
        if ("collectible" in inv_response["descriptions"][description]["type"].lower()
            or "container" in inv_response["descriptions"][description]["type"].lower()
            or "pass" in inv_response["descriptions"][description]["type"].lower()
            or "gift" in inv_response["descriptions"][description]["type"].lower()
            or "music kit" in inv_response["descriptions"][description]["type"].lower()
            or "graffiti" in inv_response["descriptions"][description]["type"].lower()
            or "agent" in inv_response["descriptions"][description]["type"].lower()
            or "sticker" in inv_response["descriptions"][description]["type"].lower()
            or "tool" in inv_response["descriptions"][description]["type"].lower()
            or "★ Covert Knife" in inv_response["descriptions"][description]["type"].lower()
            or "★ Extraordinary Gloves" in inv_response["descriptions"][description]["type"].lower()):
            non_relevant_items.append(description)
        else:
            description_indices.append(description)

    raw_asset_indices = []
    for id_combo in range(len(id_array)):
        for asset in range(len(inv_response["assets"])):
            raw_asset_indices.append([])
            if (id_array[id_combo][0] == inv_response["assets"][asset]["classid"]
                and id_array[id_combo][1] == inv_response["assets"][asset]["instanceid"]):
                raw_asset_indices[asset].append(id_combo)
    for element in range(len(raw_asset_indices)):
        if raw_asset_indices[-1] == []:
            del raw_asset_indices[-1]
    asset_indices = []
    for element in range(len(raw_asset_indices)):
        asset_indices.append(raw_asset_indices[element][0])
    asset_indices = np.unique(asset_indices).tolist()
    for item in range(len(non_relevant_items)):
        del asset_indices[non_relevant_items[item]-item]

    return description_indices, asset_indices