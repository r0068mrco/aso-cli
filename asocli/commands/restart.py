import click
import docker

@click.command()
@click.argument('containername')
def restart(containername):

    """Restarts the given container.

    \b
    - containername: container name to re-start.

    """

    click.secho('Restarting the container <<{}>> ...'.format(containername), fg='yellow')
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get(containername)
        container.restart()
    except docker.errors.NotFound:
        click.secho('Container <<{}>> not found. Please review the container name'.format(containername), fg='red')
        return
    except docker.errors.APIError as ex:
        click.secho('Error trying to restart container <<{}>> due to {}'.format(containername, ex.explanation), fg='red')
        return

    click.secho('Container <<{}>> restarted successfully'.format(containername), fg='green')