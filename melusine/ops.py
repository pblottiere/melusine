import logging
from cliff.command import Command

from melusine import settings


class Operations(Command):

    log = logging.getLogger( __name__ )

    def take_action(self, parsed_args):
        if not settings.SERVER:
            self.log.error('Not connected')
            return

        for o in settings.SERVER.operations:
            self.app.stdout.write('{}\n'.format(o.name))
