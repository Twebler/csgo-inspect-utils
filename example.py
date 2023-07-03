import inspect_tools as i


get_information = i.get_information


#writes information about weaponskins in a inventory into a output file if given a steamid
get_information.information("76561199118473343")


#writes information about only Consumer Grade weaponskins in a inventory into a output file if given a steamid
import json
inventory = get_information.information("76561199118473343", output_file=False)
consumer_grade_lst = []
for n in range(len(inventory)):
    if inventory[n]["rarity"] == "Consumer Grade":
        consumer_grade_lst.append(inventory[n])
with open("response.json", "w", encoding="utf-8") as json_file:
    json.dump(consumer_grade_lst, json_file, indent=3, ensure_ascii=False) #ensure ascii and utf-8 are important because sometimes there are chinese or japanese characters in the skin names and they cant be encoded without this


#gets a all inspect links from a given inventory accociated to the given steamid
get_information.inspectlinks_steamid("76561199118473343")
#Output:
#[
#   steam://rungame/730/76561202255233023/+csgo_econ_action_preview S76561199118473343A30655339493D2496331251447853727, 
#   steam://rungame/730/76561202255233023/+csgo_econ_action_preview S76561199118473343A30654135650D9415595817228188845, 
#   steam://rungame/730/76561202255233023/+csgo_econ_action_preview S76561199118473343A30653367322D16889851714948743458, 
#   steam://rungame/730/76561202255233023/+csgo_econ_action_preview S76561199118473343A30652669466D16900543212568003837, 
#   steam://rungame/730/76561202255233023/+csgo_econ_action_preview S76561199118473343A30442114345D12297088180031719184
#]


#gets a all gen codes from a given inventory accociated to the given steamid
get_information.gens_steamid("76561199118473343")
#Output:
#[
#    "!gen 27 1245 216 0.2328414022922516 5918 0.7280449271202087 5918 0.7072139978408813 5918 0.7743327617645264 5918 0.7776358127593994 0 0", 
#    "!gen 9 838 884 0.4426316022872925 7045 0 7045 0 7045 0 7045 0 0 0", 
#    "!gen 4 799 852 0.03141592815518379 7169 0 7169 0 7169 0 0 0 0 0", 
#    "!gen 19 593 950 0.13865140080451965 179 0 0 0 7169 0 4982 0 0 0", 
#    "!gen 38 46 14 0.36654868721961975 0 0 0 0 0 0 0 0 0 0"
#]


#gets all the gencodes from a list of inspect links
get_information.gens_custom(["steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561199118473343A30653367322D16889851714948743458", 
                             "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561199118473343A30654135650D9415595817228188845", 
                             "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20S76561199118473343A30655339493D2496331251447853727"])
#Output:
#[
#   "!gen 4 799 852 0.03141592815518379 7169 0 7169 0 7169 0 0 0", 
#   "!gen 9 838 884 0.4426316022872925 7045 0 7045 0 7045 0 7045 0", 
#   "!gen 27 1245 216 0.2328414022922516 5918 0.7280449271202087 5918 0.7072139978408813 5918 0.7743327617645264 5918 0.7776358127593994"
#]



#==============================================================


generate = i.generate()

#3x 9ine holo Paris 2023
generate.gen("Desert Eagle", "Printstream", "387", "0.05347336083651", ["6638", "1", "0"], ["6638", "2", "0"], ["6638", "3", "0"])
#Output:
#!gen 1 962 387 0.05347336083651 0 0 6638 0 6638 0 6638 0



#4x scraped Avangar Boston 2018
generate.gen("AK-47", "Bloodsport", "661", "0.05347336083651", ["2508", "2", "0.8"], ["6638", "1", "0.8"], ["6638", "3", "0.8"], ["6638", "0", "0.8"])
#Output:
#!gen 7 639 661 0.05347336083651 2508 0.8 2508 0.8 2508 0.8 2508 0.8



#1x Virtus.Pro Cologne 2014
generate.gen("AWP", "Asiimov", "666", "0.96999835968018", ["2508", "2", "0"])
#Output:
#!gen 9 279 666 0.96999835968018 0 0 0 0 134 0 0 0



#4x scraped seang@res gold Boston 2018
generate.gen("AK-47", "Case Hardened", "784", "0.00771540543064", ["2884", "0", "0.7"], ["2884", "1", "0.7"], ["2884", "2", "0.7"], ["2884", "3", "0.7"])
#Output:
#!gen 7 44 784 0.00771540543064 2884 0.7 2884 0.7 2884 0.7 2884 0.7



#5x Hellraisers holo Katowice 2014
generate.gen("R8 Revolver", "Blaze", "1", "0.03574906289577", ["58", "0", "0"], ["58", "2", "0"], ["58", "4", "0"], ["58", "1", "0"], ["58", "3", "0"])
#Output:
#!gen 64 37 1 0.03574906289577 58 0 58 0 58 0 58 0 58 0