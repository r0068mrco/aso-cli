import click
import docker
import os

@click.command()
@click.argument('username')
@click.argument('version')
@click.argument('country_code')
@click.argument('container')
@click.option('--ports', nargs=3, type=int)
@click.option('--api-key', nargs=1, type=str)
def pull(username, version, country_code, container, ports=None, api_key=None):

    """
    Pull and Run the ASO version image indicated

    \b
    - username: username of artifactory.
    - version: number version of the image to pull.
    - country_code: Country code to pull localized image. [ es, mx, ... ]
    - container: name for the container to be created.
    \b
    Optionally:
    - ports: A list with exactly three customs ports to avoid port collisions in the same machine
    - api-key: The artifactory api-key (this value can be obtained from ARTIFACTORY_API_KEY env var)
    """

    # Remove country_code parameter when each country has their own docker bucket repositories
    # at HOME / docker-repo / / aso / es / aso-image
    # at HOME / docker-repo / / aso / mx / aso-image
    # at HOME / docker-repo / / aso / co / aso-image

    # At this moment is needed:  HOME / docker-repo / / aso / es / aso-image-$COUNTRY_CODE  (allocated at `es` bucket)

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

    # Getting ARTIFACTORY API KEY from several sources
    password = ''
    if api_key is not None:
        password = api_key
    elif "ARTIFACTORY_API_KEY'" in os.environ:
        password = os.environ['ARTIFACTORY_API_KEY']
    else:
        password = click.prompt('PLEASE enter your Artifactory API KEY', hide_input=True, confirmation_prompt=False)

    try:
        docker_client = docker.from_env()

        click.secho('Login user {}'.format(username), fg='green')

        dev_tools_endpoint = 'globaldevtools.bbva.com:5000'

        docker_client.login(username=username, password=password, registry=dev_tools_endpoint)

        image = dev_tools_endpoint + '/aso/' + country_code.lower() + '/aso-image-' + country_code.lower() + ':' + version

        click.secho('Pulling the image from Docker Registry...'.format(image), fg='green')

        docker_client.images.pull(image)

        click.secho('Pulled image successfully {}'.format(image), fg='green')
        click.secho('Run the image in a container {}'.format(container), fg='green')

        docker_client.containers.run(image, name=container, ports={7500:p1, 8789:p2, 10249:p3}, tty=True, detach=True, stdout=True)
    except docker.errors.APIError as ex:
        click.secho('Error trying to run container {} due to {}'.format(container, ex.explanation), fg='red')
        return

    click.secho('Container {} started in ports {} {} {}'.format(container,p1,p2,p3), fg='green')