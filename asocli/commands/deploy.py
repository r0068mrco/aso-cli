import os
import sys
import click

from .restart import restart

@click.command()
@click.argument('src', type=click.Path(exists=True))
@click.argument('container_name')
@click.option('--reload', default=False, help='Flag to restart the container after deploy. False by default.')
@click.pass_context
def deploy(ctx, src, container_name, reload):

    """
    \b
    Deploy a .jar file into container module specified.

    \b
    - src: .jar name to deploy into container. Ex. qzqp_myjar-1.0.0-sn.jar or qzqp_myjar-sn.jar
    - container_name: container name where deploy the .jar file.

    \b
    This command requires restart the jboss to take effect the changes.
    Use --reload=true or aso restart to do this
    """
    click.secho('Copying artifacts to <<service>> container module', fg='yellow')

    PATH_TO_DEPLOY_JARS='/opt/jboss/current/modules/bbva/ctqsrv01/arquitectura/servicios/main'
    MODULE_FILE='/opt/jboss/current/modules/bbva/ctqsrv01/arquitectura/servicios/main/module.xml'

    script_name = '/script/update-module-servicios-xml.sh'

    if os.path.isfile(src) == True:
        EXTENSION = src[src.find('.', len(src)-4):]
        if EXTENSION == ".jar":
            # copy jar file
            os.system('docker cp {} {}:{}'.format(src, container_name, PATH_TO_DEPLOY_JARS))
            # update module.xml reference
            os.system('docker exec -it {} sh {} {} \
                {}'.format(container_name, script_name, src, MODULE_FILE))
        else:
            click.secho('Error!. Only .jar files will be copied', fg='red')
            sys.exit(2)
    else:
        click.secho('Error! {} is not valid'.format(src), fg='red')
        sys.exit(1)

    click.secho('Artifacts copied successfully', fg='green')

    if reload:
        ctx.invoke(restart, containername=container_name)
    else:
        click.secho('Remember to restart container {} to apply changes'.format(container_name), fg='magenta')
