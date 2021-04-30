import logging
from cliff.command import Command

from mscli import settings


class Servers(Command):

    log = logging.getLogger( __name__ )

    def take_action(self, parsed_args):
        self.app.write('List of reference servers\n')
        for l in settings.SERVERS:
            self.app.write('  {}\n'.format(l))
        self.app.write('\n')
