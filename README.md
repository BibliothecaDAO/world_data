# world_data

This repo holds all the information to put realms on the map.

You can use QGIS (version ^3.26) to open and edit `realms_world.qgs`.
This is evidently also the working repo for QGIS.

## geojson information

📁 `./datasources_json/`

|filename|info|
|----------------:|:------------------|
|`ga_bags.json`| Data pulled from graphql (manually updated)|
|`geo.json`| Defines order continents and islands |
|`realms.json`| Defines where all realms are situated |

📁 `./datasources_geojson/`

|filename|info|
|----------------:|:------------------|
|`buffered_zones_separate.geojson` | buffer zones with separated geometry |
|`buffered_zones.geojson` | Buffer zone with an inland offset to make sure random samples don't land on the coastline |
|`coast_1.geojson` | Buffer zone land outward of magnitude 1 |
|`coast_2.geojson` | Buffer zone land outward of magnitude 2 |
|`coast_3.geojson` | Buffer zone land outward of magnitude 3 |
|`crypts_land.geojson` | Land crypts |
|`crypts_sea.geojson` | Sea crypts |
|`fog.geojson` | Inland for of war layer |
|`ga_bags.geojson` | Sampled randomly in each respective order |
|`loot_bags.geojson` | Random loot bags scattered into the buffered zone |
|`no_borders.geojson` | Merge of whole continents |
|`ocean.geojson` | Coarse ocean layer |
|`order_highlights.geojson` | Layer to assist with order highlighting, not used
|`sea_icons.geojson` | Unused
|`water_bodies.geojson` | Defines water bodies and backstories |

## build

In order to prepare some files, run: `$ python make.py`
All necessary files will be put in the `build/` folder.

For the ga bags, go to [https://thegraph.com/hosted-service/subgraph/treppers/genesisproject]() and run:
```
{
  adventurers(first:1000, skip:0) {
    id
    order
  }
}
```

## mapbox

Most of the geojsons are used in the mapbox application.
Contact Pondering Democritus for access tokens if needed.

### tilesets

If you want to upload a bitmap to mapbox, you'll have to create a tileset.
Since the bitmaps are likely going to be over 300MB, you'll have to use the aws cli: [https://docs.mapbox.com/api/maps/uploads/]()

