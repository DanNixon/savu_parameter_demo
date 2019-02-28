#!/bin/bash

function do_tests {
  TAG="savu_parameters_demo_python-${1}"

  docker build \
    --build-arg PYTHON_VERSION=${1} \
    --tag ${TAG} \
    .

  docker run \
    --rm \
    --volume "$PWD:/data" \
    --entrypoint bash \
    ${TAG} \
    /data/docker_test_runner.sh
}

do_tests 2-slim
do_tests 3-slim
