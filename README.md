# Melusine

## Install

````
$ git clone https://github.com/pblottiere/melusine
$ mkdir -p venv
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
$ pip install .
````

## Usage

Example:

````
$ melusine
(melusine) servers
  Geoserver
  Degree
  InteractiveInstruments
  OSM
(melusine) connect geoserver
SUCCESS
(melusine) layers
List of available layers
  cite:Autos
  cite:BasicPolygons
  cite:Bridges
  cite:BuildingCenters
  cite:Buildings
  cite:DividedRoutes
  cite:Forests
  cite:Lakes
  cite:LakesWithElevation
  cite:MapNeatline
  cite:NamedPlaces
  cite:Ponds
  cite:RoadSegments
  cite:Streams

(melusine) info cite:Forests
Layer information for 'cite:Forests'
  title       cite:Forests
  crs         CRS:84, EPSG:4326
  extent      (-0.001, -0.002, 0.004, 0.002, 'CRS:84')
  styles      Forests

(melusine) map cite:Forests
GetMap request parameters
  output        /tmp/melusine.jpeg
````
