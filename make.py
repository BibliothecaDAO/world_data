import os
import shutil
import json
import random

BUILD_DIR = "./build"

# LOOT BAGS
LOOT_BAGS_GEOJSON = "./datasources_geojson/loot_bags.geojson"

# GENESIS PROJECT
GA_BAGS_GRAPHQL = "./datasources_json/ga_bags.json"
GA_BAGS_GEOJSON = "./datasources_geojson/ga_bags.geojson"

# CRYPTS N CAVERNS
CNC_METADATA = "./cnc-images/metadata/dungeons.json"
LAND_CRYPTS_GEOJSON = "./datasources_geojson/crypts_land_order.geojson"
SEA_CRYPTS_GEOJSON = "./datasources_geojson/crypts_sea.geojson"

ORDERS = [ # random order here!
    "Rage",
    "Detection",
    "Anger",
    "Giants",
    "Skill",
    "Enlightenment",
    "Power",
    "Brilliance",
    "Perfection",
    "Titans",
    "Fury",
    "Reflection",
    "the Twins",
    "Vitriol",
    "the Fox",
    "Protection"
]

if os.path.isdir(BUILD_DIR):
    shutil.rmtree(BUILD_DIR)
os.mkdir(BUILD_DIR)

def load_json(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data

def save_json(data, path):
    with open(f"{BUILD_DIR}/{path}", "w") as file:
        json.dump(data, file, indent=2)

def allocate_genesis_adventurers():
    # load data sources
    graphdata = load_json(GA_BAGS_GRAPHQL)
    geodata = load_json(GA_BAGS_GEOJSON)
    
    # create fixed mapping
    for ga in graphdata["data"]["adventurers"]:
        for feature in geodata["features"]:
            if ga["order"] == feature["properties"]["order_name"]:
                if "ga_id" not in feature["properties"]:
                    feature["properties"]["ga_id"] = ga["id"]
                    break
    new_data = {
        "type": "FeatureCollection",
        "name": "ga_bags",
        "features": [
            {
                "properties": {
                    "ga_id": feature["properties"]["ga_id"],
                    "order": feature["properties"]["order_name"]
                },
                "geometry": feature["geometry"]
            }
            for feature in geodata["features"] if "ga_id" in feature["properties"]
        ]
    }
    save_json(new_data, "ga_bags.json")

def allocate_crypts():
    cnc_data = load_json(CNC_METADATA)
    land_data = load_json(LAND_CRYPTS_GEOJSON)
    sea_data = load_json(SEA_CRYPTS_GEOJSON)
    random.seed(42)
    random.shuffle(land_data["features"])

    # create some useful lists
    nones = []
    environments = []
    affinities = []

    for cidx, crypt in enumerate(cnc_data["dungeons"]):
        if crypt is None:
            nones.append(cidx)
            continue
        env, aff = crypt["environment"], crypt["affinity"]
        if env not in environments:
            environments.append(env)
        if aff not in affinities:
            affinities.append(aff)

    # sea crypts
    sea_crypts = []

    for idx, crypt in enumerate(cnc_data["dungeons"]):
        if crypt is None:
            continue
        if crypt["environment"] == "Underwater Keep":
            sea_crypts.append(crypt)
            cnc_data["dungeons"][idx] = None
            
    for idx, co in enumerate(sea_data["features"]):
        co["properties"].update(sea_crypts[idx])

    # land crypts
    ordered_crypts = {}
    other_crypts = []
    for idx, crypt in enumerate(cnc_data["dungeons"]):
        if crypt is None:
            continue
        order = crypt["affinity"]
        if order in ORDERS and order != "Underwater Keep":
            if order not in ordered_crypts:
                ordered_crypts[order] = [crypt]
            else:
                ordered_crypts[order].append(crypt)
        else:
            other_crypts.append(crypt)

    # give priority to crypts with a tied order
    for order, prio_crypts in ordered_crypts.items():
        for prio_crypt in prio_crypts:
            for cidx, feature in enumerate(land_data["features"]):
                if feature["properties"]["order_name"] == order and len(feature["properties"]) == 2:
                    land_data["features"][cidx]["properties"].update(prio_crypt)
                    break

    # allocate the residual crypts
    for sec_crypt in other_crypts:
        for cidx, feature in enumerate(land_data["features"]):
            if len(feature["properties"]) == 2:
                land_data["features"][cidx]["properties"].update(sec_crypt)
                break

    # combine everything
    all_features = sea_data["features"] + land_data["features"]
    all_features = [
        {
            "properties": {
                "tokenId": x["properties"]["tokenId"],
                "environment": x["properties"]["environment"]
            },
            "geometry": x["geometry"]
        } 
        for x in all_features if len(x["properties"]) > 2]

    combined = {'type': 'FeatureCollection',
        'name': 'crypts_all',
        'features': all_features
    }

    save_json(sea_data, "crypts_sea.json")
    save_json(land_data, "crypts_land.json")
    save_json(combined, "crypts_all.json")

def tidy_loot_bags():
    data = load_json(LOOT_BAGS_GEOJSON)

    data = {
        "type": data["type"],
        "name": data["name"],
        "features": [
            {
                "properties": {
                    "bag_id": feature["properties"]["id"] + 1,
                    "order": feature["properties"]["order_name"]
                },
                "geometry": feature["geometry"]
            }
            for feature in data["features"]
            ]
    }

    save_json(data,"loot_bags.json")

allocate_genesis_adventurers()
# allocate_crypts()
# tidy_loot_bags()
