# docker
[Docker](https://en.wikipedia.org/wiki/Docker_(software)) is a tool for [operating-system-level virtualization](https://en.wikipedia.org/wiki/OS-level_virtualization). This is more lightweight than a virtual machine because the guest operating system (called a container) shares some components with the host (often the kernel) and is minimalist in nature.

## Index
1. [Pull](#pull)
1. [Exit](#exit)
    1. [Graceful](#graceful)
    1. [Forceful](#forceful)
1. [Run](#run)
    1. [Environment Variables](#environment-variables)
    1. [Volume Mount](#volume-mount)
        1. [Copy](#copy)
    1. [Workdir](#workdir)
    1. [Port Map](#port-map)
    1. [Privileged Mode](#privileged-mode)
1. [Save](#save)
    1. [Tag](#tag)
1. [Push](#push)
1. [Images](#images)
    1. [Remove Images](#remove-images)
1. [See Also](#see-also)

# Pull
Docker images are stored in "registries" in the cloud.

You need to know the name of the image to download it from the cloud, which is just a URL.
```bash
sudo docker pull 'docker.io/library/ubuntu:22.04'
```
You will see docker download and extract one or more "layers" of the container.

# Exit
Containers are not saved when you exit, so be sure to [save](#save) before exiting or your changes will be lost.

## Graceful
Containers will exit when your script ends or, if you have an interactive shell, you can exit yourself.
```bash
exit
```

## Forceful
Sending [Ctrl] + [C] will pass through your shell to your container and can be used to kill a running process in the container. If that doesn't work, you can open another shell on the host and kill the container.
```bash
CONTAINER="$(sudo docker ps -l | tail -n '1' | rev | awk '{print $1}' | rev)"  # get a reference to the most recently launched RUNNING container
sudo docker kill "$CONTAINER"
```

# Run
Full documentation on the `docker run` command and all options described in this section is available [here](https://docs.docker.com/engine/reference/commandline/run).

The basic format for running docker image is:
```bash
sudo docker run "$IMAGE"
```
This will invoke your container's default command, which was defined when the container was created. You can give your own command instead.
```bash
sudo docker run "$IMAGE" "$COMMAND"
sudo docker run ubuntu:22.04 /bin/bash -c 'cat /etc/lsb-release'
```
Notice the container immediately exits. Most of the time you will want an interactive BASH shell, so add the `-it` flag for "interactive tty" to keep it running.
```
sudo docker run -it ubuntu:22.04 /bin/bash
```
Sometimes containers have an [entrypoint](https://medium.com/the-code-review/how-to-use-entrypoint-with-docker-and-docker-compose-1c2062aa17a2). An entrypoint is a command a container is set to execute the moment it is run. They can be very frustrating if you just want a shell. You have to use a special flag to override them.
```
sudo docker run --entrypoint /bin/bash -it ubuntu:22.04
```
Note that docker is picky about the order of the command-line arguments.

Finally, you should know how to list the currently running containers.
```bash
sudo docker ps
```
You'll see each container has two additional identifiers, a container ID (hexadecimal string) and a friendly name (dictionary tuple). These labels refer to the running instance of that image rather than to the image itself and are necessary for operations on an already-running container.

## Environment Variables
You can pass in existing or new environment variables to your guest using the `-e` flag.
```bash
sudo docker run -e CI=true -it ubuntu:22.04
export DOCKER='true'
sudo docker run -e DOCKER -it ubuntu:22.04
sudo docker run -e CI=true -e DOCKER -it ubuntu:22.04
sudo docker run -e CI=true -e DOCKER -e JOBS=$(nproc) -it ubuntu:22.04
```

## Volume Mount
You can mount portions of your host filesystem into your container. Add one or more `-v` flags:
```bash
sudo docker run -v "$HOST_PATH:$GUEST_PATH" -it "$IMAGE" /bin/bash
sudo docker run -v "$(pwd):/leap" -it ubuntu:22.04 /bin/bash
sudo docker run -v ~/Work/antelope/leap:/leap -it ubuntu:22.04 /bin/bash
sudo docker run -v ~/Work/antelope/leap:/leap -v ~/Work/antelop/cdt:/cdt -it ubuntu:22.04 /bin/bash
```
Files mounted into your container are not saved or pushed with the container, and are not available if you run the container again later without the volume mount. They exist and are modified on your host filesystem.

### Copy
It is best to keep containers lightweight by [mounting](#volume-mount) files you need into them, but you can also copy files into or out of a container. These files become a part of the container itself and increase container size.

You need to have a reference to the _running_ instance of the container, which is a container ID or friendly name that you can get from `docker ps`.
```bash
sudo docker ps
sudo CONTAINER="$(sudo docker ps -l | tail -n 1 | rev | awk '{print $1}' | rev)"
```
Copy files or folders between your host and guest using the same argument order as `cp` or `mv`:
```bash
sudo docker cp "$SOURCE" "$DESTINATION"
sudo docker cp /host/path "$CONTAINER:/guest/path"  # copy from host to guest
sudo docker cp "$CONTAINER:/guest/path" /host/path  # copy from guest to host
```

## Workdir
The `-w` flag allows you to set a default working directory when the container starts for a command, a script, or a shell.
```bash
sudo docker run -w "$GUEST_PATH" -it "$IMAGE" "$COMMAND"
```
This option is most often combined with the [volume mount](#volume-mount) command, but does not have to be.
```bash
sudo docker run -v ~/Work/antelope/leap:/leap -w /leap -it ubuntu:22.04 /bin/bash
```

## Port Map
If you try to bind a port from inside your container, it might bind but you won't be able to hit it from outside the container. In order to expose a port, you can use the `-p` flag to bind a host port to your guest.
```bash
sudo docker run -p "$HOST_PORT:$GUEST_PORT" -it "$IMAGE" /bin/bash
sudo docker run -p "$HOST_INTERFACE:$HOST_PORT:$GUEST_PORT" -it "$IMAGE" /bin/bash

sudo docker run -p 8080:80 -it ubuntu:22.04 /bin/bash
sudo docker run -p 127.0.0.1:8080:80 -it ubuntu:22.04 /bin/bash
```
Docker has more information on [container networking](https://docs.docker.com/config/containers/container-networking).

## Privileged Mode
⚠️ **Warning: Here be dragons!** ⚠️  
You _might_ run into permissions issues when trying to do certain tasks such as dumping memory, attaching a debugger to another process, setting `ulimit`, or the like. Container runtimes are lighter and faster than virtual machines because they share as many of the host's core operating system components with the guest as possible. So, even though you are root, operations involving kernel or hardware access are prohibited by default to protect the host. If you need to enable kernel operations or direct hardware access, you can pass the `--privileged` flag.
```bash
sudo docker run --privileged -it ubuntu:22.04 /bin/bash
```
This has a side-effect of exposing your host machine to all of your [container's vulnerabilities](https://blog.trendmicro.com/trendlabs-security-intelligence/why-running-a-privileged-container-in-docker-is-a-bad-idea/). A successful exploit of the container will result in host kernel-level root access while this flag is in use, so you should [be very hesitant to use it](https://medium.com/better-programming/docker-tips-mind-the-privileged-flag-d6e2ae71bdb4). Only use the `--privileged` flag for debugging inside containers that do not have ports mapped to the outside world, do not have services exposed, and are not in deployment.

# Save
Containers are not saved when you exit, so be sure to commit before exiting or your changes will be lost.

You can save a running container using `docker commit`.
```bash
CONTAINER="$(sudo docker ps -l | tail -n 1 | rev | awk '{print $1}' | rev)"  # get a reference to the most recently launched RUNNING container programmatically
sudo docker commit "$CONTAINER" "$REGISTRY:$TAG"
```
The `REGISTRY` and `TAG` labels can be anything you want locally. These labels are not validated as a URI until you try to push them to the cloud.

I follow this pattern for images on my local machine to keep them organized and give me some hope of understanding what they are weeks later when I am cleaning them up.
```
$PIPELINE:$TASK-$INDEX-$DESCRIPTION
    $REPO:$TASK-$INDEX-$DESCRIPTION
```
Here, `REPO` or `PIPELINE` are where this container lives or is normally used. `TASK` helps me group containers from the same task, project, or story together. `INDEX` forces docker to list these containers in the order I created them. `DESCRIPTION` is optional, but sometimes I add one or two words indicating why I saved it or what step I was at in my process. Remember, you have to type these. Keep them short, like 8.3 filenames.

## Tag
You can apply labels to docker images and versions of images. These labels consist of two parts, the name and the tag, separated by a colon '`:`'. The name can include the [registry](#pull), making it look like a URL, or not. Names which do not look like a URL are implicitly prefixed with `docker.io/` if you try to push them to the cloud.

The same docker image can have multiple labels. For example, one image might be tagged with its GitHub branch, GitHub commit hash, and `latest`. All three of these labels refer to the same docker image:
```
docker.io/antelope/leap:latest
docker.io/antelope/leap:main
docker.io/antelope/leap:4d114191606a3cdea4905b9b63d074fd234409e0
```
The docker image these three labels refer to can be identified absolutely by its SHA-256 hash...
```bash
HASH=1dd6a76c73450fe27fb4faa88589c4b6bda6e63ecb12ef3e636f29751389a1b0
```
...and can be [pulled](#pull) directly using this hash.
```
sudo docker pull docker.io/antelope/leap@sha256:$HASH
```
These labels can also be changed. If you run `leap:latest`, make some changes, then commit the upgraded image as `leap:latest`, now `leap:latest` will point to that new image instead of what you started with (at least locally). The first image is not deleted. Even if you remove all its tags, it will still remain on your computer or in the registry until you explicitly remove it.

Images are labeled when you build or [save](#save) them, but you can add labels after-the-fact, too.
```bash
sudo docker tag "$IMAGE" "$NEW_LABEL"
sudo docker tag 'docker.io/antelope/leap:main' 'leap:main'
sudo docker tag 'leap:zach-docker' 'docker.io/antelope/leap:zach-docker'
```

# Push
You can push your containers up to docker [registries](#pull) in the cloud to share them or make them available to systems. A push works the same way as a [pull](#pull), but in reverse, and you will have to be authenticated to the remote registry.
```bash
sudo docker push "$IMAGE"
```
Note that any `IMAGE` label must be a valid URI. Any `IMAGE` label which is not a valid URI is assumed to be an image on [Docker Hub](https://hub.docker.com), and is prepended with `docker.io/` before validation.

# Images
Docker images you have pulled, run, or built are cached and stored locally on your machine.

You can list all images cached on your host with `docker images`.
```bash
sudo docker images
```

To list only running images, use `docker ps`.
```bash
sudo docker ps
```
You'll see each container has two additional identifiers, a container ID (hexadecimal string) and a friendly name (dictionary tuple). These labels refer to the running instance of that image rather than to the image itself, and are necessary for operations on an already-running container.

## Remove Images
Even hundred-megabyte docker images can add up quickly so you will eventually want to delete some of them. This is done with the "remove image" command.
```bash
sudo docker rmi "$IMAGE"
```
Docker won't delete an image if its layers are in use by other images, so you also have the option to force-delete images.
```bash
sudo docker rmi -f "$IMAGE"
```
With great power comes great responsibility.

Here are some BASH snippets to find and clean up images for you.
Delete untagged images that are not in-use:
```bash
sudo docker rmi $(sudo docker images | grep '^<none>' | awk '{print $3}')
```
Add the `-f` flag to delete all untagged images, even if they have children.
```bash
sudo docker rmi -f $(sudo docker images | grep '^<none>' | awk '{print $3}')
```

# See Also
- [Docker Hub](https://hub.docker.com)
- Docker Documentation
    - [Best Practices for Writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
    - [Build Command](https://docs.docker.com/engine/reference/commandline/build)
    - [Container Networking](https://docs.docker.com/config/containers/container-networking)
    - [Docker Development Best Practices](https://docs.docker.com/develop/dev-best-practices/)
    - [Dockerfile Reference](https://docs.docker.com/engine/reference/builder)
    - [Run Command](https://docs.docker.com/engine/reference/commandline/run)
