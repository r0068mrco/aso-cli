import click
import docker

@click.command()
@click.argument('containername')
def stop(containername):

    """Stops the given container.

    \b
    - containername: container name to stop
    """

    click.secho('Stopping the container [{}] ...'.format(containername), fg='yellow')
    try:
        docker_client = docker.from_env()
        container = docker_client.containers.get(containername)
        container.stop()
    except docker.errors.NotFound:
        click.secho('Container <<{}>> not found. Please review the container name'.format(containername), fg='red')
        return
    except docker.errors.APIError as ex:
        click.secho('Error trying to stop container <<{}>> due to {}'.format(containername, ex.explanation), fg='red')
        return

    click.secho('Container <<{}>> Stopped'.format(containername), fg='green')