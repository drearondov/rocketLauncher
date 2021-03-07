import pytest


@pytest.mark.parametrize("env_manager", ["pyenv", "conda"])
@pytest.mark.parametrize("create_env", ["--create-env", "--no-create-env"])
@pytest.mark.parametrize("poetry_adapted", ["--poetry-adapted", "--no-poetry-adapted"])
@pytest.mark.parametrize("upload_github", ["--upload-github", "--no-upload-github"])
@pytest.mark.parametrize("quickstart", ["--quickstart", "--no-quickstart"])
def test_config_init(
    init, cli_runner, monkeypatch,
    env_manager, create_env, poetry_adapted, upload_github, quickstart
) -> None:

    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    from rocket_launcher.main import app

    result = cli_runner.invoke(
        app, [
            "config",
            "init",
            "--env-manager", env_manager,
            create_env,
            poetry_adapted,
            upload_github,
            "--commit-message", ":tada: test commit",
            quickstart
        ]
    )

    assert result.exit_code == 0

    assert "\nDefaults set, you're good to go!" in result.stdout


@pytest.mark.parametrize(
    "key, value", [
        ("env_manager", "conda"),
        ("create_env", "False"),
        ("poetry_adapted", "True"),
        ("upload_github", "True"),
        ("commit_message", ":tada: new commit test message"),
        ("quickstart", "False")
    ]
)
def test_config_change(init, cli_runner, monkeypatch, key: str, value: str) -> None:

    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    from rocket_launcher.main import app

    result = cli_runner.invoke(app, ["config", "change", "--key", key, "--new-value", value])

    assert result.exit_code == 0
