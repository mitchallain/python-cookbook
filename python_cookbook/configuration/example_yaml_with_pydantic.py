import sys
import inspect

import pydantic
import yaml


class BaseModel(pydantic.BaseModel):
    """Extension of pydantic.BaseModel to support YAML parsing"""
    @classmethod
    def parse_yaml(cls, filepath):
        """Parse YAML file into pydantic model"""
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)
        return cls.parse_obj(config)


class Config(BaseModel):
    foo: str
    bar: int

    @pydantic.validator("bar")
    def bar_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("bar must be positive")
        return v


def main():
    print(f"Parsing config with invalid data")
    try:
        Config.parse_yaml("config.yaml")
    except pydantic.ValidationError as e:
        print(e)

    config["bar"] = 10
    print(f"Parsing config with valid data: {config}")
    try:
        Config.parse_obj(config)
        print("Config is valid")
    except pydantic.ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
    # get module filepath
    module_filepath = inspect.getfile(sys.modules[__name__])
