from cliff.command import Command
from owslib.wms import WebMapService
from mscli import settings


class Connect(Command):

    def get_parser(self, prog_name):
        parser = super(Connect, self).get_parser(prog_name)
        parser.add_argument('server', nargs='?')
        return parser

    def take_action(self, parsed_args):
        server = parsed_args.server

        if not server:
            self.app.error('No server URL or server name')
            return

        for s in settings.SERVERS.keys():
            if server.lower() == s.lower():
                server = settings.SERVERS[s].url

        try:
            settings.SERVER = WebMapService(server, version='1.3.0')
        except Exception as e:
            self.app.error('Invalid URL ({})'.format(e))
            return

        settings.SERVER.server = server

        if settings.SERVER:
            self.app.success()


class Disconnect(Command):

    def take_action(self, parsed_args):
        settings.SERVER = None
        self.app.success()
