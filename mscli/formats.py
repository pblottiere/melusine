from cliff.command import Command
from mscli import settings


class Formats(Command):

    def take_action(self, parsed_args):
        if not settings.SERVER:
            self.app.error('Not connected')
            return

        self.app.write('List of available formats\n')
        for f in settings.SERVER.getOperationByName('GetMap').formatOptions:
            self.app.write('  {}\n'.format(f))
        self.app.write('\n')
