import kfp
from kfp import dsl
from my_component import (add, say_hello)
import sys

#addition_pipeline_path ="/Users/osmanjalloh/working/operator/tmp/EPHEMERAL/images/ubuntu/middleware/jannah_graphql/jannah_site/addition-pipeline-2024-02-16T19-53-01-717858.yaml"

@kfp.dsl.pipeline
def addition_pipeline(x: int, y: int) -> int:
    task1 = add(a=x, b=y)
    task2 = add(a=task1.output, b=x)
    return task2.output


@dsl.pipeline
def hello_pipeline(person_to_greet: str) -> str:
    # greeting argument is provided automatically at runtime!
    hello_task = say_hello(name=person_to_greet)
    return hello_task.outputs['greeting']

def main(
            addition_pipeline_path,
            hello_pipeline_path,
        ):
    kfp.compiler.Compiler().compile(addition_pipeline, addition_pipeline_path)
    kfp.compiler.Compiler().compile(hello_pipeline, hello_pipeline_path)

if __name__ == '__main__':
    print(sys.argv)
    main(
            sys.argv[1],
            sys.argv[2]
        )