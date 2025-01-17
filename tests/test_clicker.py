"""
Unit tests for the Auto Clicker.
"""

import os
import pytest
from auto_clicker.clicker import AutoClicker


@pytest.fixture
def clicker():
    return AutoClicker(delay_min=0.1, delay_max=0.2)


def test_log_creation(clicker):
    clicker.total_clicks = 10
    clicker.save_log()
    assert os.path.exists(clicker.log_file)
    with open(clicker.log_file, "r") as file:
        logs = file.readlines()
        assert f"Total Clicks: 10" in logs[-1]
