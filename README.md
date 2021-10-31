# What is aso-cli?
  
The ASO Command Line Interface (CLI) is a unified tool to manage your local environment of ASO architecture.
With just one tool to download and configure, you can debug and test your local develop service.

## IMPORTANT

For earlier versions of the 5.7.5.19 architecture, **version 0.1** should be used. For version 5.7.5.19 and above use version 1.0.

You can clone the repository to get the latest version, or download a specific version with **git checkout &lt;version&gt;**. For example: `git checkout 0.1`

## Installation guide

The full installation guide is available on [BBVA platform documentation site](https://platform.bbva.com/en-us/developers/engines/aso/documentation/building-business-services/local-development-environment/installation-guide).

## Common operations

### See service logs

To see logs, you hace to connect to the docker container with this command:

```bash
docker exec -it $ASO_CONTAINER_NAME bash
```

This command connect to the aso container running in your local environment at main folder

```bash
/logs/app/producto/JBOSS/JBOSS62/QSRV_A02
```

It' possible to see the server boot information doing:

```bash
cat localhost/localhost.log
```

Or with a `tail -f`, and you could see something like that

```text
JBoss EAP 7.0.0.GA (WildFly Core 2.1.2.Final-redhat-1) started in 41548ms - Started 460 of 465 services
```

And to check your service deployment log information:

```bash
cd /var/log/app/
```

And then search your service name and see the log, for example:

```bash
cat qsrv_grantingTickets_localhost.log
```
