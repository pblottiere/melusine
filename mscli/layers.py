from cliff.command import Command
from mscli import settings


class Layers(Command):

    def take_action(self, parsed_args):
        if not settings.SERVER:
            self.app.error('Not connected')
            return

        self.app.write('List of available layers\n')
        for l in settings.SERVER.contents:
            self.app.write('  {}\n'.format(l))
        self.app.write('\n')
