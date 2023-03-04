import sys
import inspect

from pydantic import BaseModel
import yaml


class Config(BaseModel):
    foo: str
    bar: int


def main():
    with open("config.yaml") as f:
        config = yaml.safe_load(f)
    print(config)
    Config.parse_obj(config)


if __name__ == "__main__":
    main()
    # get module filepath
    module_filepath = inspect.getfile(sys.modules[__name__])
