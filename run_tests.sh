#!/bin/bash

function do_tests {
  docker run \
    --rm \
    --volume "$PWD:/data" \
    --entrypoint bash \
    ${1} \
    /data/docker_test_runner.sh
}

do_tests python:2-slim
do_tests python:3-slim
