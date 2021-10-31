import click
import docker

@click.command()
@click.argument('image')
@click.argument('container')
@click.option('--ports', nargs=3, type=int)
def run(image, container, ports=None):

    """
    Runs the docker local image for DATABASE DEV environment mode, or offline FILE mode.

    \b
    - image: local image name. Ex: globaldevtools.bbva.com:5000/aso/es/aso-image-es:5.2.2
    - container: container name.
     \b
    Optionally:
    - ports: A list with exactly three customs ports to avoid port collisions in the same machine
    """

     # Default ports
    p1 = 7500
    p2 = 8789
    p3 = 10249

    if ports is not None and len(ports) != 0:
        if len(ports) == 3:
            p1 = ports[0]
            p2 = ports[1]
            p3 = ports[2]
            click.secho('Ports {} {} {} allocated'.format(p1,p2,p3), fg='green')
        else:
            click.secho('Number of ports must be exactly 3', fg='red')

    try:
        docker_client = docker.from_env()
        docker_client.containers.run(image, name=container, ports={7500:p1, 8789:p2, 10249:p3}, tty=True, detach=True, stdout=True)
    except docker.errors.APIError as ex:
        click.secho('Error trying to run container {} due to {}'.format(container, ex.explanation), fg='red')
        return

    click.secho('Container {} started in ports {} {} {}'.format(container,p1,p2,p3), fg='green')