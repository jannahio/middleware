from kfp import dsl
from math_utils import add_numbers


@dsl.component(base_image='python:3.7',
               target_image='jannahioregistry/jannah-component-2-arm64-ubuntu:v0.0.1')
def add(a: int, b: int) -> int:
    return add_numbers(a, b)

@dsl.container_component
def say_hello(name: str, greeting: dsl.OutputPath(str)):
    """Log a greeting and return it as an output."""

    return dsl.ContainerSpec(
        image='alpine',
        command=[
            'sh', '-c', '''RESPONSE="Hello, $0!"\
                            && echo $RESPONSE\
                            && mkdir -p $(dirname $1)\
                            && echo $RESPONSE > $1
                            '''
        ],
        args=[name, greeting])