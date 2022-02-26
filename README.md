# world_data

This repo holds all the information to put realms on the map.

You can use QGIS to open and edit `realms_world.qgs`.

## geojson information

`datasources_json`

|filename|info|
|----------------:|:------------------|
|`crypts_all.json` | All crypt locations |
|`crypts_land.json` | Crypts located on land, with crypts of a specific order given priority |
|`crypts_sea.json` | Sea crypts |
|`geo.json`| Defines order continents and islands |
|`realms.json`| Defines where all realms are situated |
|`ga_bags.json`| Data pulled from graphql (manually updated)|

`datasources_geojson`

|filename|info|
|----------------:|:------------------|
|`loot_bags.geojson` | Random loot bags scattered into the buffered zone |
|`ga_bags.geojson` | Sampled randomly in each respective order |
|`crypts_land.geojson` | Land crypts |
|`crypts_sea.geojson` | Sea crypts |
|`buffered_zones.geojson` | Buffer zone with an inland offset to make sure random samples don't land on the coastline |
|`sea_icons.geojson` | Unused
|`order_highlights.geojson` | Layer to assist with order highlighting, not used
|`buffered_zones_separate.geojson` | buffer zones with separated geometry |
|`water_bodies.geojson` | Defines water bodies and backstories |
|`no_borders.geojson` | Merge of whole continents |
|`fog.geojson` | Inland for of war layer |
|`coast_1.geojson` | Buffer zone land outward of magnitude 1 |
|`coast_2.geojson` | Buffer zone land outward of magnitude 2 |
|`coast_3.geojson` | Buffer zone land outward of magnitude 3 |
|`ocean.geojson` | Coarse ocean layer |

## build

In order to prepare all files, run: `$ python make.py`
All necessary files will be put in the `build/` folder.

For the ga bags, go to `https://thegraph.com/hosted-service/subgraph/treppers/genesisproject` and run:
```
{
  adventurers {
    id
    order
    currentOwner {
      id
    }
  }
}
```