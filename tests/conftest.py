import rocket_launcher
import pytest
import configparser

from typer.testing import CliRunner


@pytest.fixture
def cli_runner():
    return CliRunner()

@pytest.fixture(autouse=True)
def test_config(tmpdir):
    test_config_file = tmpdir.join("test_config.ini")

    test_config_file.write("[general]")
    test_config_file.write("[defaults]")
    test_config_file.write("[cookiecutters]")

    test_config = configparser.ConfigParser()
    test_config.read(test_config_file)

    return test_config
