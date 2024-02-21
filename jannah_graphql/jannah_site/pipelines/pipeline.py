import kfp
from kfp import dsl
from my_component import add
import sys

#addition_pipeline_path ="/Users/osmanjalloh/working/operator/tmp/EPHEMERAL/images/ubuntu/middleware/jannah_graphql/jannah_site/addition-pipeline-2024-02-16T19-53-01-717858.yaml"

@kfp.dsl.pipeline
def addition_pipeline(x: int, y: int) -> int:
    task1 = add(a=x, b=y)
    task2 = add(a=task1.output, b=x)
    return task2.output

def main(addition_pipeline_path):
    kfp.compiler.Compiler().compile(addition_pipeline, addition_pipeline_path)

if __name__ == '__main__':
    print(sys.argv)
    main(sys.argv[1])