from __future__ import annotations

import pytest

from texledger.config import ConfigParser


class TestConfigFunction:
    @pytest.mark.parametrize("config_file_path", ["examples/config.toml", ""])
    def test_config_parser_config_options(self, config_file_path):
        cp = ConfigParser(config_file_path)
        assert cp.config_options is not None

    @pytest.mark.parametrize("config_file_path", ["examples/config.toml", ""])
    def test_config_parser_read_config(self, config_file_path):
        cp = ConfigParser(config_file_path)
        if len(config_file_path) <= 0:
            with pytest.raises(FileNotFoundError):
                cp.read_config(config_file_path)

    @pytest.mark.skip(reason="Feature has yet to be implemented")
    def test_config_parser_parse_config(self):
        assert False

    @pytest.mark.skip(reason="Feature has yet to be implemented")
    def test_config_validator(self):
        # cv: ConfigValidator
        assert False

    @pytest.mark.skip(reason="Feature has yet to be implemented")
    def test_config_builder(self):
        # cb: ConfigBuilder
        assert False
