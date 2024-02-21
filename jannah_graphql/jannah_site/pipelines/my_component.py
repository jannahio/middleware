from kfp import dsl
from math_utils import add_numbers


@dsl.component(base_image='python:3.7',
               target_image='jannahioregistry/jannah-component-2-arm64-ubuntu:v0.0.1')
def add(a: int, b: int) -> int:
    return add_numbers(a, b)