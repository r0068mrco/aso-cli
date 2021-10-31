import click
import docker

@click.command()
def images():

    """
    List all docker images
    """

    try:
        docker_client = docker.from_env()

        print('********************')
        print('Images name: version')
        print('********************')
        for image in docker_client.images.list():
            print('{}'.format(image.attrs['RepoTags']))

    except docker.errors.APIError:
        raise