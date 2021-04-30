class Server(object):
    def __init__(self, name, url, service, version):
        self.name = name
        self.url = url
        self.service = service
        self.version = version

def init():
    global SERVER
    SERVER=None

    # https://github.com/opengeospatial/cite/wiki/Reference-Implementations
    global SERVERS
    SERVERS={}

    geoserver = Server('Geoserver',
                       'http://cite.demo.opengeo.org:8080/geoserver_wms13/wms',
                       'WMS',
                       '1.3.0')
    SERVERS[geoserver.name] = geoserver

    degree = Server('Degree',
                    'http://cite.deegree.org/deegree-webservices-3.4-RC3/services/wms130',
                    'WMS',
                    '1.3.0')
    SERVERS[degree.name] = degree

    interactive = Server('InteractiveInstruments',
                         'http://services.interactive-instruments.de/cite-xs-410/cite/cgi-bin/wms/wms/wms',
                         'WMS',
                         '1.3.0')
    SERVERS[interactive.name] = interactive

    osm = Server('OSM',
                 'http://129.206.228.72/cached/osm',
                 'WMS',
                 '1.3.0')
    SERVERS[osm.name] = osm
