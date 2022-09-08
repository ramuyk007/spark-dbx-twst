# Python-Spark

**Build:**
[https://acsbamboo.honeywell.com/plugins/servlet/wittified/build-status/HGZAGTDZ-GPJDMMHZ](https://acsbamboo.honeywell.com/browse/HGZAGTDZ-GPJDMMHZ)

The code in this pipeline was created from the [Python WebApi template](https://bitbucket.honeywell.com/projects/HGZAGTDZ/repos/Python-Spark/browse) as part of the CE DevOps Initiative. For more information see the [Design](https://confluence.honeywell.com/display/HDODRAFT/Python+Templates). For more information about the build scripts in general please see [Build Script Design](https://confluence.honeywell.com/display/HDO/Build+Script+Design)

## Getting Started

These instructions will allow you to build the Webapi component on your local machine for development and testing purposes.

This code is built using the [Cake](https://cakebuild.net/) build framework and [Maven](https://maven.apache.org/) as packet manager. It can be built using locally installed components or a containerized environment.

The recommended editor for working on this code is [Visual Studio Code](https://code.visualstudio.com/Download). The recommended extensions can be viewed by running the VSCode command "Extensions: Show Recommended Extensions". Once the Cake extension is installed, run the VSCode command "Cake: Install intellisense support" to make it easier to work on the build scripts.

VSCode commands can be executed on _command pallete_ which can be launched using Ctrl+Shift+P key combination.

### Containerized Enviornments

On Honeywell laptops, only Linux and Mac operating systems can be used to run the build in a containerized environment.  In most cases, Docker cannot be properly installed on Windows due to the policies installed by Cisco AnyConnect, which prevents local volume mounting. Users who have *full* admin access to their machines can disable AnyConnect whilst using Docker. But this means they often cannot be connected to the Honeywell network at the same time, leading to other complications.

For Windows users, it is possible to use a containerized evironment by using these [Vagrant Instructions](https://confluence.honeywell.com/display/HDO/Setting+up+Ansible+and+Docker+in+Vagrant+box+for+windows+clients).

### Building on Windows

Install the following prerequisites:

* [DotNetCore SDK](https://www.microsoft.com/net/download)
* [DotNet Framework 4.7.2](https://dotnet.microsoft.com/download/dotnet-framework-runtime)
* [Python version 3.7](https://www.python.org/downloads/)
* [pip version 19.1.1](https://pip.pypa.io/en/stable/installing/)


#### Build on windows locally

On domain joined developer machines, Enterprise IT has disabled unsigned Powershell script execution. 
As a workaround there is a batch file that calls the required powershell file which is executed on the build machine.

```
.\bootstrap.bat
```

#### Build without build scripts

```cmd
pip install -r ./src/requirements.txt --user
python ./src/setup.py build
```

### Building on Linux and Mac using Docker

Install the following prerequisites:

* Docker version 18+
* Powershell Core [Linux](<https://docs.microsoft.com/en-us/powershell/scripting/setup/installing-powershell-core-on-linux?view=powershell-6>)/[Mac](<https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-6>)

Then run the build

```cmd
pwsh bootstrap.ps1
```

### Building on Linux and Mac using Local Installs

Install the following prerequisites:

* Powershell Core [Linux](<https://docs.microsoft.com/en-us/powershell/scripting/setup/installing-powershell-core-on-linux?view=powershell-6>)/[Mac](<https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-macos?view=powershell-6>)
* Python version 3.7 [Linux](https://www.python.org/downloads/source/)/[Mac](https://www.python.org/downloads/mac-osx/)
* Pip version 19.1.1 [Linux/Mac](https://pip.pypa.io/en/stable/installing/)

### Running the API template Locally

#### From IDE

ToDo

#### From Command Line

```cmd
pip install -r ./src/requirements.txt --user
python ./src/setup.py build
python ./src/init_app.py --host 0.0.0.0
```

#### From Docker

1. Run `.\bootstrap.ps1` to download and execute the build scripts, perform Build and Package
2. Run `.\bootstrap.ps1 -Target Publish` to generate the docker image of the deployable application
3. From a command/powershell prompt you should be able to see your newly created image. It should look something like this:

    ```shell

    $ docker image ls
    REPOSITORY           TAG        IMAGE ID            CREATED             SIZE

    <bitbucket-repo-name> 0.1.0     2d2cfc645c50       2 hours ago         1.45GB

    ```
4. Create and run the docker container from the image as follows:

    ```shell
      docker run -it --rm -p 80:8000/tcp --name <bitbucket-repo-name>.0.1.0 <bitbucket-repo-name>
    ```

## Executing Acceptance Tests locally

Acceptance test are not yet implemented.

### Performance Testing

Locust is an open source load testing tool. User behaviour can be defined with Python code in filename named locustfile.py, and system can be swarmed with millions of simultaneous users. 

Locust supports running load tests distributed across multiple machines. To do this, start one instance of Locust in master mode using the --master flag. The master node doesn’t simulate any users itself. Instead you have to start one or most likely multiple worker Locust nodes, with the --master-host (to specify the IP/hostname of the master node).

A common set up is to run a single master on one machine, and then run one worker instance per processor core on the worker machines.

#### Running Performance Test locally

Locust testing can be initiated through docker-compose commands. docker-compose builds the application, performance containers and start the run in a distributed fashion.
prior to starting locust execution, application code has to be built.

Install the following prerequisites:
##### Docker Compose

* `https://docs.docker.com/compose/install/`

To run performance test locally on your machine

##### Linux/Mac

1. Run `pwsh ./bootstrap.ps1`
2. Run `pwsh ./src/test/performance/performance-local.ps1`

##### Windows

1. Run `./bootstrap.ps1`
2. Run `./src/test/performance/performance-local.ps1`

##### Master variables
```
command: locust class name either TestLargeScale or TestSmallScale are the default acceptable values here. These classes are defined under locustfile.py

LOCUST_MODE_MASTER: Defines locust master.  Supports either true or false

LOCUST_HOST: URL of the application which test runs against

LOCUST_LOCUSTFILE: Path of the locust file(locustfile.py)

LOCUST_HEADLESS : Run locust without the web UI. Supports either true or false

LOCUST_EXPECT_WORKERS: Master will wait for the number of workers before beginning the test

LOCUST_USERS : Number of users testing your application. Each user opens a TCP connection to your application and tests it. 

LOCUST_HATCH_RATE : Users spawned/second. For each second, how many users will be added to the current users until the total amount of users. Each hatch Locust calls the on_start function if you have.

LOCUST_RUN_TIME:  Test duration

LOCUST_CSV: Path to the result cvs 

LOCUST_LOGFILE: Path to the log file

```

##### Worker variables
```
LOCUST_MODE_WORKER: Defines locust worker.  Supports either true or false

LOCUST_LOCUSTFILE: Path of the locust file(locustfile.py)

LOCUST_MASTER_NODE_HOST: Locust master host name 

LOCUST_MASTER_NODE_PORT: Locust master port(5557)

LOCUST_HOST: URL of the application which test runs against

LOCUST_HEADLESS: Run locust without the web UI.  Supports either true or false

```

## Debug CAKE Scripts

For debugging CAKE Scripts locally, please refer the documentation here [Debug](https://confluence.honeywell.com/display/HDO/FAQ:+How+to+debug+the+template+in+Visual+Studio+Code+and+Visual+Studio+2017)

## Contributing

TBD

## Versioning

We use [SemVer](http://semver.org/) for versioning using [GitVersion](https://github.com/GitTools/GitVersion). For the versions available, see the [artifactory repository](https://artifactory-na.honeywell.com/artifactory/webapp/#/artifacts/browse/simple/General/ce-devops-common-nuget-stable-local)

## AppHosting

For better understanding on AppHosting deployment essentials see the [AppHosting deployment](https://confluence.honeywell.com/display/HDO/Support+for+using+OpenShift+Templates)

## Support

For issues related to templates, please reach out us over [Microsoft Teams](https://teams.microsoft.com/l/channel/19%3aeb42116337a84772a896087fdc5d2fcb%40thread.skype/Template%2520Support?groupId=421e0c0f-e743-45c4-a738-979eb840fc11&tenantId=96ece526-9c7d-48b0-8daf-8b93c90a5d18)