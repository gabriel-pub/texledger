from __future__ import annotations
from texledger.constants import TEXLEDGER_EXAMPLE_CONFIG_FILE

from typing import Any
import tomli


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
