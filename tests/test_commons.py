import pytest

from rocket_launcher.commons import create_config, create_project, upload_to_github

@pytest.mark.parametrize("env_manager", ["pyenv", "conda"])
@pytest.mark.parametrize("create_env", [True, False])
@pytest.mark.parametrize("poetry_adapted", [True, False])
@pytest.mark.parametrize("upload_github", [True, False])
@pytest.mark.parametrize("quick_start", [True, False])
def test_create_config(
    tmpdir,
    env_manager,
    create_env,
    poetry_adapted,
    upload_github,
    quick_start
):
    
    pass