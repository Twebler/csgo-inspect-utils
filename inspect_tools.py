'''
    Quick disclaimer:
    iam not that experienced in writing actual pretty or readable code or even just customer grade code so if there are any improvements i can
    make to make this code better in any way even if its not about functionality but just about readability and such. 
    Help ot tips are greatly apreciated!
'''
import requests
import json
from resources import non_callable_funcs
import operator

class get_information:
    def __init__(self) -> None:
        pass

    #takes a steamid and returns all the information about the weaponskins in the given inventory that i think is relevant
    def information(self, steam_id: str, output_file=True, output_file_indent=3):
        #raw_inv_response = requests.get(f"https://steamcommunity.com/inventory/{steam_id}/730/2")
        #inv_response = raw_inv_response.json()

        #this line is used for prototyping so i dont have to request the api everytime i do a test
        inv_response = json.load(open("T:\\Development\\Python\\float_avg\\inventory.json", encoding="utf-8"))

        if inv_response == None:
            exit("Steam API didnt respond try again later")
        information_list = []
        description_indices, asset_indices = non_callable_funcs.relevant_indices(inv_response)
        for index in range(len(description_indices)):
            inspect_link = "steam://rungame/730/76561202255233023/+csgo_econ_action_preview "+"S"+steam_id+"A"+inv_response["assets"][asset_indices[index]]["assetid"]+inv_response["descriptions"][description_indices[index]]["actions"][0]["link"].split("%")[-1]
            #INCLUDE PROXIES HERE
            raw_invhelper_response = requests.get(f"https://floats.steaminventoryhelper.com/?url={inspect_link}")
            invhelper_response = raw_invhelper_response.json()
            if invhelper_response["success"] == False:
                invhelper_response = {
                    "iteminfo": {
                        "paintseed": "api didnt respond",
                        "floatvalue": "api didnt respond"
                    }
                }
            sticker_lst = []
            for i in range(len(invhelper_response["iteminfo"]["stickers"])):
                sticker_lst.append(
                    {
                        "slot": invhelper_response["iteminfo"]["stickers"][i]["slot"],
                        "stickerid": invhelper_response["iteminfo"]["stickers"][i]["stickerId"],
                        "scrape": invhelper_response["iteminfo"]["stickers"][i]["wear"],
                        "name": invhelper_response["iteminfo"]["stickers"][i]["name"]
                    }
                )
            information_list.append({
                    "inspectlink": inspect_link,
                    "assetid": inv_response["assets"][asset_indices[index]]["assetid"],
                    "classid": inv_response["assets"][asset_indices[index]]["classid"],
                    "instanceid": inv_response["assets"][asset_indices[index]]["instanceid"],
                    "market_hash_name": inv_response["descriptions"][description_indices[index]]["market_hash_name"],
                    "weapon_type": "",
                    "collection": "",
                    "rarity": "",
                    "condition": "",
                    "paintseed": invhelper_response["iteminfo"]["paintseed"],
                    "floatvalue": invhelper_response["iteminfo"]["floatvalue"],
                    "stickers": sticker_lst
                }
            )
            for tag in range(len(inv_response["descriptions"][description_indices[index]]["tags"])):
                if inv_response["descriptions"][description_indices[index]]["tags"][tag]["category"] == "Type":
                    information_list[index]["weapon_type"] = inv_response["descriptions"][description_indices[index]]["tags"][tag]["localized_tag_name"]
                elif inv_response["descriptions"][description_indices[index]]["tags"][tag]["category"] == "ItemSet":
                    information_list[index]["collection"] = inv_response["descriptions"][description_indices[index]]["tags"][tag]["localized_tag_name"]
                elif inv_response["descriptions"][description_indices[index]]["tags"][tag]["category"] == "Rarity":
                    information_list[index]["rarity"] = inv_response["descriptions"][description_indices[index]]["tags"][tag]["localized_tag_name"]
                elif inv_response["descriptions"][description_indices[index]]["tags"][tag]["category"] == "Exterior":
                    information_list[index]["condition"] = inv_response["descriptions"][description_indices[index]]["tags"][tag]["localized_tag_name"]
        if output_file:
            with open("output/response.json", "w", encoding="utf-8") as file:
                json.dump(information_list, file, indent = output_file_indent, ensure_ascii=False)
        else:
            return information_list
        
    #takes a inspect link list and returns a gen code list for those inspect links
    def gens_custom(self, inspect_links: list):
        gencodes = []
        for n in range(len(inspect_links)):
            steamid = inspect_links[n].split("S")[1].split("A")[0]
            assetid = inspect_links[n].split("S")[1].split("A")[1].split("D")[0]
            #raw_inv_response = requests.get(f"https://steamcommunity.com/inventory/{steamid}/730/2")
            #inv_response = raw_inv_response.json()

            #this line is used for prototyping so i dont have to request the api everytime i do a test
            inv_response = json.load(open("T:\\Development\\Python\\float_avg\\inventory.json", encoding="utf-8"))

            if inv_response == None:
                exit("Steam API didnt respond try again later")
            for asset in range(len(inv_response["assets"])):
                if assetid == inv_response["assets"][asset]["assetid"]:
                    classid = inv_response["assets"][asset]["classid"]
                    instanceid = inv_response["assets"][asset]["instanceid"]
            if (len(classid) == 0 and len(instanceid) == 0):
                return "Couldnt find given assetid in inventory/steamid given in the inspect-link"
            for description in range(len(inv_response["descriptions"])):
                if (classid == inv_response["descriptions"][description]["classid"] and 
                    instanceid == inv_response["descriptions"][description]["instanceid"]):
                    weapon = inv_response["descriptions"][description]["name"].split(" | ")[0].replace("StatTrak™ ", "")
                    raw_skin = inv_response["descriptions"][description]["name"].split(" | ")
                    for i in range(len(inv_response["descriptions"][description]["tags"])):
                        if inv_response["descriptions"][description]["tags"][i]["category"] == "Exterior":
                            exterior_index = i
                    skin = " ".join(raw_skin).replace("StatTrak™ ", "").replace(inv_response["descriptions"][description]["tags"][exterior_index]["localized_tag_name"], "")
            all_weaponids = json.load(open("T:\\Development\\Python\\float_avg\\resources\\weaponids.json"))
            all_skinids = json.load(open("T:\\Development\\Python\\float_avg\\resources\\skinids.json", encoding="utf-8"))
            raw_invhelper_response = requests.get(f"https://floats.steaminventoryhelper.com/?url={inspect_links[n]}")
            invhelper_response = raw_invhelper_response.json()
            sticker_lst = [["0", "0"], ["0", "0"], ["0", "0"], ["0", "0"], ["0", "0"]]
            counter = 0
            for i in range(len(sticker_lst)):
                if counter >= len(invhelper_response["iteminfo"]["stickers"]):
                    break
                if i == invhelper_response["iteminfo"]["stickers"][counter]["slot"]:
                    sticker_lst[i] = [str(invhelper_response["iteminfo"]["stickers"][counter]["stickerId"]),
                                    str(invhelper_response["iteminfo"]["stickers"][counter]["wear"])]
                    counter+=1

            stickers = " ".join([sticker_lst[0][0], sticker_lst[0][1], sticker_lst[1][0], sticker_lst[1][1], sticker_lst[2][0], sticker_lst[2][1], sticker_lst[3][0], sticker_lst[3][1], sticker_lst[4][0], sticker_lst[4][1]])
            gencode = " ".join(["!gen", all_weaponids[weapon], all_skinids[skin], str(invhelper_response["iteminfo"]["paintseed"]), str(invhelper_response["iteminfo"]["floatvalue"]), stickers])
            gencodes.append(gencode.rstrip("0 "))
        return gencodes
    
    #takes a steamid and returns the inspect links for all Weaponskins
    def inspectlinks_steamid(self, steam_id: str):
        information_list = self.information(steam_id, output_file=False)
        inspect_link_list = []
        for i in range(len(information_list)):
            inspect_link_list.append(information_list[i]["inspectlink"])
        return inspect_link_list
    
    #takes a steamid and returns the gen codes for all Weaponskins in the given inventory
    def gens_steamid(self, steamid: str):
        gen_code_list = []
        inspect_link_list = self.inspectlinks_steamid(steamid)
        gen_code_list = self.gens_custom(inspect_link_list)
        return gen_code_list

class generate:
    def __init__(self) -> None:
        pass
    #takes a weapon name, skin name, patternseed, floatvalue, and up to 5 stickers with this syntax [stickerid, slot, scrape] and returns a gen code
    def gen(self, weapon: str, skin: str, pattern: str, floatvalue: str, sticker_lst1=["0","1","0"], sticker_lst2=["0","2","0"], sticker_lst3=["0","3","0"], sticker_lst4=["0","4","0"], sticker_lst5=["0","4","0"]):
        weaponid = json.load(open("T:\\Development\\Python\\float_avg\\resources\\weaponids.json"))[weapon]
        skinid = json.load(open("T:\\Development\\Python\\float_avg\\resources\\skinids.json", "r", encoding="utf-8"))[" ".join([weapon, skin])]
        
        all_stickers = sorted([sticker_lst1, sticker_lst2, sticker_lst3, sticker_lst4, sticker_lst5], key=operator.itemgetter(1))
        for i in range(len(all_stickers)):
            del all_stickers[i][1]
            all_stickers[i] = " ".join(all_stickers[i])
        final_stickers = " ".join(all_stickers)
        
        return " ".join(["!gen", weaponid, skinid, pattern, floatvalue, final_stickers])

class buy:
    def __init__(self) -> None:
        pass
    #https://steamcommunity.com/market/listings/<app_id>/<hashname>#buylisting|<marketlisting_id>|<app_id>|<context_id>|D


t = get_information()
p = t.gens_steamid("76561199118473343")
print(p)