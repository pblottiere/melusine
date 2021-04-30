# mscli

## Install

````
$ git clone https://github.com/pblottiere/mscli
$ mkdir -p venv
$ virtualenv -p /usr/bin/python2 venv
$ source venv/bin/activate
$ pip install .
````

## Usage

Example:

````
$ mscli
(mscli) servers
  Geoserver
  Degree
  InteractiveInstruments
  OSM

(mscli) connect geoserver
SUCCESS

(mscli) info
Server information
  url         http://cite.demo.opengeo.org:8080/geoserver_wms13/wms
  title       None
  abstract    None
  type        WMS
  version     1.3.0
  layers      14

(mscli) layers
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

(mscli) info cite:Forests
Layer information for 'cite:Forests'
  title       cite:Forests
  crs         CRS:84, EPSG:4326
  extent      (-0.001, -0.002, 0.004, 0.002, 'CRS:84')
  styles      Forests

(mscli) operations
GetCapabilities
GetMap
GetFeatureInf

(mscli) map cite:Forests
GetMap request parameters
  output        /tmp/mscli.jpeg

(mscli) disconnect
````
