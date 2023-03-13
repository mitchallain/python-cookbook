import inspect
import os
import sys

import pydantic
import yaml


class BaseModel(pydantic.BaseModel):
    """Extension of pydantic.BaseModel to support YAML parsing"""
    @classmethod
    def parse_yaml(cls, filepath):
        """Parse YAML file into pydantic model

        Args:
            filepath (str): path to YAML file
        """
        with open(filepath, "r") as f:
            config = yaml.safe_load(f)
        return cls.parse_obj(config)

    def check(self):
        """Re-execute the model validators on the current model values.

        This is useful when you want to check the validity of a model
        after changing one of its attributes.

        https://github.com/pydantic/pydantic/issues/1864#issuecomment-1118485697
        """
        values, fields_set, validation_error = pydantic.validate_model(
            self.__class__, self.__dict__
        )
        if validation_error:
            raise validation_error
        try:
            object.__setattr__(self, "__dict__", values)
        except TypeError as e:
            raise TypeError(
                "Model values must be a dict; you may not have returned "
                + "a dictionary from a root validator"
            ) from e
        object.__setattr__(self, "__fields_set__", fields_set)


class Config(BaseModel):
    foo: str
    bar: int

    @pydantic.validator("bar", always=True)
    def bar_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("bar must be positive")
        return v


def main():
    config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
    print(f"-- 1) Parsing '{config_path}' with invalid data")

    try:
        Config.parse_yaml(config_path)
    except pydantic.ValidationError as e:
        print(e)

    with open(config_path, 'r') as f:
        config_dict = yaml.safe_load(f)

    config_dict["bar"] = 10
    print(f"-- 2) Parsing config with valid data: {config_dict}")
    try:
        config = Config.parse_obj(config_dict)
        print("Config is valid")
    except pydantic.ValidationError as e:
        print(e)
        return

    print("-- 3) Setting an invalid value and calling BaseModel.check()")
    config.bar = -1
    try:
        config.check()
    except pydantic.ValidationError as e:
        print(e)
        return


if __name__ == "__main__":
    main()
    # get module filepath
    module_filepath = inspect.getfile(sys.modules[__name__])
