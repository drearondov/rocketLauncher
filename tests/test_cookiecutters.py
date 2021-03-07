def test_cookiecutters_add(init, cli_runner, monkeypatch) -> None:
    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    from rocket_launcher.main import app

    result = cli_runner.invoke(
        app,
        ["cookiecutters", "add", "--alias", "new_cookiecutter", "--link", "cookiecutter_link"]
    )

    assert result.exit_code == 0


def test_cookiecutters_list(init, cli_runner, monkeypatch) -> None:
    _, test_config_path = init

    monkeypatch.setenv("CONFIG_FILE", str(test_config_path))

    from rocket_launcher.main import app

    result = cli_runner.invoke(app, ["cookiecutters", "list"])

    assert result.exit_code == 0

    assert "\n== Available cookiecutters ==" in result.stdout
