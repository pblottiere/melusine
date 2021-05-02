from cliff.command import Command
from owslib.wms import WebMapService
from mscli import settings
import subprocess


class Map(Command):

    def get_parser(self, prog_name):
        parser = super(Map, self).get_parser(prog_name)
        parser.add_argument('layers', nargs='*')
        parser.add_argument('--crs', nargs='?')
        parser.add_argument('--bbox', nargs='?')
        parser.add_argument('--transparent', nargs='?', default=False)
        parser.add_argument('--width', nargs='?')
        parser.add_argument('--height', nargs='?')
        parser.add_argument('--format', nargs='?')
        parser.add_argument('--output', nargs='?')
        return parser

    def take_action(self, parsed_args):
        layers = parsed_args.layers
        server = settings.SERVER

        if not server:
            self.app.error('Not connected')
            return

        if not layers:
            self.app.error('At least 1 layer is necessary')
            return

        for l in layers:
            if l not in server.contents:
                self.app.error('Invalid layer \'{}\''.format(l))

        print(0)
        default_layer = server[layers[0]]
        print(1)
        default_layer = server[layers[0]]
        bbox = parsed_args.bbox
        print(2)
        crs = parsed_args.crs
        print(3)

        if not crs:
            crs = default_layer.boundingBox[4]

        print(4)
        if not bbox:
            bbox = (default_layer.boundingBox[0],
                    default_layer.boundingBox[1],
                    default_layer.boundingBox[2],
                    default_layer.boundingBox[3])
        else:
            bbox = list( map(float, bbox.split(',')) )

        print(5)
        height = parsed_args.height
        if not height:
            height = 400

        width = parsed_args.width
        if not width:
            width = 400

        size=(width,height)

        format = parsed_args.format
        if not format:
            format='image/jpeg'

        output = parsed_args.output
        if not output:
            output = '/tmp/melusine.jpeg'

        self.app.write('GetMap request parameters\n')
        self.app.write('  output        {}'.format(output) )

        print(layers)
        print(crs)
        print(bbox)
        print(size)
        print(format)

        img = server.getmap(layers=layers,
                            srs=crs,
                            bbox=bbox,
                            size=size,
                            format=format,
                            styles = [''],
                            transparent=parsed_args.transparent)

        out = open(output, 'wb')
        out.write(img.read())
        out.close()

        command = 'tycat /tmp/melusine.jpeg'
        subprocess.call(command.split())

        self.app.write('\n')
