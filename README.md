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

`datasources_geojson`

|filename|info|
|----------------:|:------------------|
|`buffered_zones.geojson` | Buffer zone with an inland offset to make sure random samples don't land on the coastline |
|`coast_2.geojson` | Buffer zone land outward of magnitude 2 |
|`ga_bags.geojson` | Sampled randomly in each respective order |
|`ocean.geojson` | Coarse ocean layer |
|`coast_3.geojson` | Buffer zone land outward of magnitude 3 |
|`order_highlights.geojson` | Layer to assist with order highlighting, not used
|`buffered_zones_separate.geojson` | buffer zones with separated geometry |
|`crypts_land.geojson` | Land crypts |
|`loot_bags.geojson` | Random loot bags scattered into the buffered zone |
|`sea_icons.geojson` | Unused
|`crypts_sea.geojson` | Sea crypts |
|`water_bodies.geojson` | Defines water bodies and backstories |
|`coast_1.geojson` | Buffer zone land outward of magnitude 1 |
|`fog.geojson` | Inland for of war layer |
|`no_borders.geojson` | Merge of whole continents |
