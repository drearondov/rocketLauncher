"""Tests for `rocket_launcher` package."""
import pytest

from rocket_launcher.main import app


@pytest.mark.parametrize("set_config", ["--set-config", "--no-set-config"])
def test_init(cli_runner, test_config, test_projects, set_config):
    result = cli_runner.invoke(
        app,
        ["init", "--projects-path", test_projects, set_config]
    )

    assert result.exit_code == 0

    if set_config:
        assert "\nDefaults set!" in result.stdout

    assert "You're good to go!" in result.stdout
