import pytest

from configparser import ConfigParser


def test_init(init, cli_runner, monkeypatch):

    test_projects, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    from rocket_launcher.main import app

    result = cli_runner.invoke(app, ["init", "--projects-path", test_projects, "--no-set-config"])

    assert result.exit_code == 0

    assert "\n== Set projects directory ==\n" in result.stdout
    assert "\n== Login to Github ==\n" in result.stdout
    assert "You're good to go!" in result.stdout

    test_config = ConfigParser()
    test_config.read(test_config_path)

    assert test_config["general"]["projects_dir"] == str(test_projects)


@pytest.mark.parametrize("env_manager", ["pyenv", "conda"])
@pytest.mark.parametrize("create_env", ["--create-env", "--no-create-env"])
@pytest.mark.parametrize("poetry_adapted", ["--poetry-adapted", "--no-poetry-adapted"])
def test_new(
    init, cli_runner, monkeypatch, fake_process,
    env_manager, create_env, poetry_adapted
) -> None:
    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    fake_process.register_subprocess([env_manager, fake_process.any()], stdout=["env", "created"])
    fake_process.register_subprocess([env_manager, "activate", "test_project"], stdout=["env", "activated"])
    fake_process.register_subprocess(["cookiecutter", fake_process.any()], stdout=["cookiecutter", "done"])
    fake_process.register_subprocess(["git", "init"], stdout=["repository", "created"])

    from rocket_launcher.main import app

    result = cli_runner.invoke(
        app,
        [
            "new",
            "--project-name", "test_project",
            "--env-manager", env_manager,
            create_env,
            "--cookiecutter", "test_cookiecutter",
            poetry_adapted,
            "--no-upload-github",
            "--commit-message", "test commit",
            "--no-quickstart"
        ]
    )

    assert result.exit_code == 0

    assert [env_manager, "activate", "test_project"] in fake_process.calls
    assert ["cookiecutter", "test_cookiecutter"] in fake_process.calls
    assert ["git", "init"] in fake_process.calls

    assert fake_process.call_count([env_manager, fake_process.any()]) >= 1

    assert "Everything's set!" in result.stdout


def test_push(init, cli_runner, monkeypatch, fake_process):
    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    fake_process.register_subprocess(["git", "add", "."])
    fake_process.register_subprocess(["git", "commit", "-m", "test commit"])
    fake_process.register_subprocess(["gh", "repo", "create"])
    fake_process.register_subprocess(["git", "push", "origin", "master"])

    from rocket_launcher.main import app

    result = cli_runner.invoke(app, ["push", "--commit-message", "test commit"])

    assert result.exit_code == 0

    assert ["git", "add", "."] in fake_process.calls
    assert ["git", "commit", "-m", "test commit"] in fake_process.calls
    assert ["gh", "repo", "create"] in fake_process.calls
    assert ["git", "push", "origin", "master"] in fake_process.calls

    assert "Repo created and uploaded!" in result.stdout
