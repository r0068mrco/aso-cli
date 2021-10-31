import click
from .commands.deploy import deploy
from .commands.images import images
from .commands.pull import pull
from .commands.restart import restart
from .commands.run import run
from .commands.start import start
from .commands.stop import stop
from .commands.undeploy import undeploy
from .commands.version import version


@click.group()
def asocli():
    pass


asocli.add_command(deploy)
asocli.add_command(images)
asocli.add_command(pull)
asocli.add_command(restart)
asocli.add_command(run)
asocli.add_command(start)
asocli.add_command(stop)
asocli.add_command(undeploy)
asocli.add_command(version)
