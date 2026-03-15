from __future__ import annotations
from pathlib import Path

import pytest


class TestExampleConfigTOML:
    @pytest.mark.parametrize("fp", ["examples/config.toml"])
    def test_example_config_toml(self, fp):
        assert Path(fp).exists()
