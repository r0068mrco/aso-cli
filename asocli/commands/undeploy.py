import os
import click

from .restart import restart

@click.command()
@click.argument('artifact_name')
@click.argument('container_name')
@click.option('--reload', default=False, help='Flag to restart the container after deploy. False by default.')
@click.pass_context
def undeploy(ctx, artifact_name, container_name, reload):

    """
    Remove previously artifact if exists

    \b
    artifact_name: .jar name to undeploy without version and without -sn or -facade. Ex. qzqp_transaction
    container_name: container name where rollback the .jar file.
    Flag --reload=true to reload the container
    """

    # pero si no existe previous, tenemos que eliminarlo del module
    click.secho('Artifact to remove {}'.format(artifact_name), fg='green')

    os.system('docker exec -it {} sh /script/undeploy-service-jar.sh {}'.format(container_name, artifact_name))

    if reload:
        ctx.invoke(restart, containername=container_name)
    else:
        click.secho('Remember to restart container {} to apply changes'.format(container_name), fg='magenta')
