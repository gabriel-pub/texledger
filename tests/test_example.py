from __future__ import annotations
from pathlib import Path

import pytest


EXPECTED_EXAMPLE_CONFIG_FILES = ["config.toml", "extras.toml"]


class TestExampleConfigTOML:
    @pytest.mark.parametrize(
        "fp",
        [Path("examples").joinpath(file) for file in EXPECTED_EXAMPLE_CONFIG_FILES],
    )
    def test_example_config_toml(self, fp):
        assert Path(fp).exists()
