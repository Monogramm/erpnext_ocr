#!/bin/bash
set -e

. .env

###########################################################
# Functions

log() {
    MESSAGE=$1

    echo "[$0] [$(date +%Y%m%d)] ${MESSAGE}"
}

dc() {
    docker-compose -f ${@}
}

build() {
    log 'Building container(s)...'
    dc ${1} build ${@:2}
}

start() {
    log 'Starting container(s)...'
    dc ${1} up -d ${@:2}
}

stop() {
    log 'Stopping container(s)...'
    dc ${1} stop ${@:2}
}

restart() {
    log 'Restarting container(s)...'
    dc ${1} restart ${@:2}
}

logs() {
    log 'Following container(s) logs (Ctrl + C to stop)...'
    dc ${1} logs -f ${@:2}
}

down() {
    log 'Stopping and removing container(s) and data...'
    dc ${1} down ${@:2}
    rm -rf ${ERPNEXT_HOME:/srv/erpnext/frappe}/*
}

console() {
    dc -it ${1} exec erpnext_app bench console ${@:2}
}

usage() {
    echo "usage: ./manage.sh COMMAND [ARGUMENTS]

    Commands:
        build       Build Dev env
        start       Start Dev env
        restart     Retart Dev env
        stop        Stop Dev env
        logs        Follow logs of Dev env
        down        Stop and remove Dev env
        console     Send command to Dev env bench console
    "
}

###########################################################
# Runtime

case ${1} in
    # DEV env
    build) build docker-compose.yml ${@:2};;
    start) start docker-compose.yml ${@:2};;
    restart) restart docker-compose.yml ${@:2};;
    stop) stop docker-compose.yml ${@:2};;
    test) start docker-compose.yml sut
    logs docker-compose.yml sut;;
    logs) logs docker-compose.yml ${@:2};;
    down) down docker-compose.yml ${@:2};;
    console) console docker-compose.yml ${@:2};;
    # PROD env
    #build) TAG=${DOCKER_TAG} \
    #    VCS_REF=`git rev-parse --short HEAD` \
    #    BUILD_DATE=`date -u +"%Y-%m-%dT%H:%M:%SZ"` \
    #    build .travis/docker-compose.yml ${@:2};;
    #start) start .travis/docker-compose.mariadb.yml ${@:2};;
    #restart) restart .travis/docker-compose.mariadb.yml ${@:2};;
    #stop) stop .travis/docker-compose.mariadb.yml ${@:2};;
    #logs) logs .travis/docker-compose.mariadb.yml ${@:2};;
    #down) down .travis/docker-compose.mariadb.yml ${@:2};;
    #console) console .travis/docker-compose.mariadb.yml ${@:2};;
    # Help
    *) usage;;
esac

exit 0
