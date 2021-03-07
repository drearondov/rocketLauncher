import pytest

from configparser import ConfigParser
from typer.testing import CliRunner


@pytest.fixture(scope="session")
def test_config():
    test_config = ConfigParser()

    test_config.add_section("general")
    test_config.add_section("defaults")
    test_config.add_section("cookiecutters")

    test_config["general"]["projects_dir"] = ""
    test_config["defaults"]["env_manager"] = ""
    test_config["defaults"]["create_env"] = "True"
    test_config["defaults"]["poetry_adapted"] = "True"
    test_config["defaults"]["upload_github"] = "False"
    test_config["defaults"]["commit_message"] = "Test commit_message"
    test_config["defaults"]["quickstart"] = "True"

    return test_config


@pytest.fixture(scope="session")
def init(tmp_path_factory, test_config):
    test_basefile = tmp_path_factory.mktemp("test_basefile", numbered=False)  # Path object

    test_projects = test_basefile/"test_projects"  # Path object
    test_projects.mkdir()

    test_project = test_projects/"test_project"
    test_project.mkdir()

    test_config_path = test_basefile/"test_config.ini"

    test_config["general"]["projects_dir"] = str(test_projects)

    with open(test_config_path, "w") as file:
        test_config.write(file)
        file.close()

    return test_projects, test_config_path


@pytest.fixture()
def cli_runner():
    return CliRunner()
