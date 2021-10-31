import click
import docker

@click.command()
@click.argument('containername')
def start(containername):

    """Turns on the given container.

    \b
    - containername: container name to start.
    """

    click.secho('Starting the container <<{}>> ...'.format(containername), fg='yellow')
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get(containername)
        container.start()
    except docker.errors.NotFound:
        click.secho('Container <<{}>> not found. Please review the container name'.format(containername), fg='red')
        return
    except docker.errors.APIError as ex:
        click.secho('Error trying to start container <<{}>> due to {}'.format(containername, ex.explanation), fg='red')
        return

    click.secho('Container <<{}>> Started'.format(containername), fg='green')