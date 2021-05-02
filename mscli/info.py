from cliff.command import Command

from mscli import settings


class Info(Command):

    def get_parser(self, prog_name):
        print("Info.get_parser")
        parser = super(Info, self).get_parser(prog_name)
        parser.add_argument('layer', nargs='?')
        return parser

    def take_action(self, parsed_args):
        if not settings.SERVER:
            self.app.error('Not connected')
            return

        if parsed_args.layer:
            self.__layer(parsed_args.layer)
        else:
            self.__server()

    def __server(self):
        self.app.write('Server information\n')

        server = settings.SERVER.server
        self.app.write('  url         {}\n'.format(server))

        title = settings.SERVER.identification.title
        self.app.write('  title       {}\n'.format(title))

        abstract = settings.SERVER.identification.abstract
        self.app.write('  abstract    {}\n'.format(abstract))

        type = settings.SERVER.identification.type
        self.app.write('  type        {}\n'.format(type))

        version = settings.SERVER.identification.version
        self.app.write('  version     {}\n'.format(version))

        nlayers = len(settings.SERVER.contents)
        self.app.write('  layers      {}\n'.format(nlayers))

        self.app.write('\n')

    def __layer(self, name):
        if name not in list(settings.SERVER.contents):
            self.app.error('Invalid layer name \'{}\''.format(name))
            return

        layer = settings.SERVER[name]

        self.app.write('Layer information for \'{}\'\n'.format(name))
        self.app.write('  title       {}\n'.format(layer.title))
        self.app.write('  crs         {0}\n'.format(', '.join(layer.crsOptions)))
        self.app.write('  extent      {}\n'.format(layer.boundingBox))
        self.app.write('  styles      {}\n'.format(', '.join(list(layer.styles.keys()))))
        self.app.write('\n')
