import os
from kfp import dsl
from math_utils import add_numbers

_base_image='python:3.7'
_target_image='jannahioregistry/jannah-component-2-arm64-ubuntu:v0.0.1'

if os.environ.get('JANNAH_PIPELINE_BASE_IMAGE'):
  _base_image = os.environ['JANNAH_PIPELINE_BASE_IMAGE']
if os.environ.get('JANNAH_PIPELINE_TARGET_IMAGE'):
  _target_image = os.environ['JANNAH_PIPELINE_TARGET_IMAGE']


print(_base_image)
print(_target_image)

@dsl.component(base_image=_base_image,
               target_image=_target_image)
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