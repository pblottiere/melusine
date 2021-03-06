import sys
from cliff.app import App
from cliff.commandmanager import CommandManager
import cmd2
from mscli import settings


class MsCli(App):

    def __init__(self):
        super().__init__(
            description='mscli',
            version='0.1',
            command_manager=CommandManager('mscli'),
            deferred_help=True,
            )
        settings.init()

    def initialize_app(self, argv):
        self.LOG.debug('initialize_app')
        print('mscli (0.1)')
        print('Type "help" for help')
        print()

    def prepare_to_run_command(self, cmd):
        self.LOG.debug('prepare_to_run_command %s', cmd.__class__.__name__)

    def clean_up(self, cmd, result, err):
        self.LOG.debug('clean_up %s', cmd.__class__.__name__)
        if err:
            self.LOG.debug('got an error: %s', err)

    def write(self, msg):
        self.stdout.write('{}'.format(msg))

    def error(self, msg):
        self.LOG.error('ERROR:  {}\n'.format(msg))

    def success(self):
        self.stdout.write('SUCCESS\n\n')

def main(argv=sys.argv[1:]):
    myapp = MsCli()
    return myapp.run(argv)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
