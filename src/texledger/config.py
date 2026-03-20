from __future__ import annotations

from typing import Any
import tomli


TEXLEDGER_EXAMPLE_CONFIG_FILE = "examples/config.toml"


class ConfigParser:
    def __init__(self, TEXLEDGER_CONFIG_FILE: str):
        try:
            self.config_options = self.read_config(TEXLEDGER_CONFIG_FILE)
        except FileNotFoundError:
            self.config_options = self.read_config(TEXLEDGER_EXAMPLE_CONFIG_FILE)

        self.parse_config(self.config_options)

    def read_config(self, fp):
        with open(fp, "rb") as f:
            return tomli.load(f)

    def parse_config(self, config_dict: dict[str, Any]):
        pass


class ConfigValidator:
    pass


class ConfigBuilder:
    pass


class Config:
    def __init__(self):
        pass

    def get(self, *args):
        pass


config = Config()
