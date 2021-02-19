import typer

from pathlib import Path
from PyInquirer import prompt

from rocket_launcher import prompt_style, config, CONFIG_FILE
from rocket_launcher.commons import create_config


settings = typer.Typer()


@settings.command()
def init(
    env_manager: str = typer.Option(
        None,
        help="Environment manager to use by default"
    ),
    create_env: bool = typer.Option(
        None,
        help="Create a virtual environment by default"
    ),
    poetry_adapted: bool = typer.Option(
        None,
        help="Are the cookiecutters used adapted for Poetry by default"
    ),
    upload_github: bool = typer.Option(
        None,
        help="Upload to github by default"
    ),
    commit_message: str = typer.Option(
        None,
        help="Deafult commit message"
    ),
    quickstart: bool = typer.Option(
        None,
        help="Use quickstart by default or interactive prompt"
    )
) -> None:
    """
    Define default configuration
    """
    create_config(env_manager, create_env, poetry_adapted, upload_github, commit_message, quickstart)


@settings.command()
def change(
    key: str = typer.Option(
        None,
        help="Name of the value to change"
    ),
    new_value: str = typer.Option(
        None,
        help="New default value"
    )
) -> None:
    """
    Change a default
    """
    questions = [
        {
            "type": "input",
            "name": "alias",
            "message": "What default do you want to change?: ",
            "when": lambda answers : key is None
        },
        {
            "type": "input",
            "name": "link",
            "message": "What's the new value?: ",
            "when": lambda answers : new_value is None
        }
    ]

    parameters = prompt(questions, style=prompt_style)

    if key is None:
        key = parameters["key"]
    
    if new_value is None:
        new_value = parameters["new_value"]
    
    config["defaults"][key] = new_value

    with open(Path(str(CONFIG_FILE)), "w") as configfile:
        config.write(configfile)
        configfile.close()
