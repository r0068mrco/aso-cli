import click
import pkg_resources

@click.command()
def version():
    """Returns aso-cli installed version.

    \b
    """
    print("Current aso-cli version:")
    version = pkg_resources.require("aso-command-cli")[0].version
    print(version)