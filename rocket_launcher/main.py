from __future__ import print_function, unicode_literals

import typer
import subprocess

from enum import Enum
from pathlib import Path
from PyInquirer import prompt

from rocket_launcher import config, prompt_style, CONFIG_FILE
from rocket_launcher.commands.settings import settings
from rocket_launcher.commands.cookiecutters import cookiecutters

from rocket_launcher.commons import create_project, upload_to_github, create_config


app = typer.Typer(name="rocketlauncher")

app.add_typer(settings, name="config", help="Create configuration file and/or set defaults")
app.add_typer(cookiecutters, name="cookiecutters", help="List/ add available cookiecutters")


@app.command()
def init(
    projects_path: Path = typer.Option(
        ...,
        exists=True,
        file_okay=False,
        dir_okay=True,
        writable=True,
        readable=True,
        resolve_path=True,
        prompt= "Where are your projects located?: ",
        help="Directory where projects are located"
    ),
    github_token: str = typer.Option(
        None,
        help="Github token to be used to connect to Github"
    ),
    set_config: bool = typer.Option(
        ...,
        help="Whether to set the default config now or not",
        prompt="Do you want to set up your defaults?: "
    )
) -> None:
    """
    Configure the projects directory and login to Github.
    """
    typer.echo(typer.style("\n== Set projects directory ==\n", fg="blue", bold=True))

    config["general"]["projects_dir"] = str(projects_path)

    typer.echo(typer.style("\n== Login to Github ==\n", fg="blue", bold=True))

    if github_token is not None:
        subprocess.run(["gh", "auth", "login", "--with-token", github_token])
    else:
        subprocess.run(["gh", "auth", "login"])

    with open(Path(str(CONFIG_FILE)), "w") as configfile:
        config.write(configfile, space_around_delimiters=True)
        configfile.close()

    if set_config is True:
        create_config()

    typer.echo("You're good to go!")


class EnvManager(str, Enum):
    conda = "conda"
    pyenv = "pyenv"


@app.command()
def new(
    project_name: str = typer.Option(
        None,
        help="Name of the project. To be used for the repo and virtual environment"
    ),
    env_manager: EnvManager = typer.Option(
        config["defaults"]["env_manager"],
        help="Virtual environment manager used for the project"
    ),
    create_env: bool = typer.Option(
        config["defaults"].getboolean("create_env"),
        help="Boolean variable to tell if create or not a virtual environment. If false, it activates the virtual environment"
    ),
    cookiecutter: str = typer.Option(
        None,
        help="Alias in curated list or link to a cookiecutter"
    ),
    poetry_adapted: bool = typer.Option(
        config["defaults"].getboolean("poetry_adapted"),
        help="Is the cookiecutter chosen adapted for Poetry?: "
    ),
    upload_github: bool = typer.Option(
        config["defaults"].getboolean("upload_github"),
        help="Choose whether you create a repository and upload to Github or not"
    ),
    commit_message: str = typer.Option(
        config["defaults"]["commit_message"],
        help="Commit message"
    ),
    quickstart: bool = typer.Option(
        config["defaults"].getboolean("quickstart"),
        help="Choose all defaults"
    )
) -> None:
    """
    Creates new project in folder, runs a cookiecutter and uploads to github.
    """
       
    questions = [
        {
            "type": "input",
            "name": "project_name",
            "message": "Name of the project: ",
            "when": lambda answers : project_name is None
        },
        {
            "type": "list",
            "name": "env_manager",
            "message": "What virtual environment manager are you going to use?: ",
            "choices": ["conda", "pyenv", "poetry"],
            "when": lambda answers : quickstart is False,
        },
        {
            "type": "confirm",
            "name": "create_env",
            "message": "Do you want to create a new environment?: ",
            "default": True,
            "when": lambda answers : quickstart is False,
        },
        {
            "type": "list",
            "name": "cookiecutter",
            "message": "What cookiecutter do you want to use?: ",
            "choices": config.options("cookiecutters"),
            "when": lambda answers : cookiecutter is None
        },
        {
            "type": "input",
            "name": "cookiecutter",
            "message": "Not on the pantry? Enter the link: ",
            "when": lambda answers: answers["cookiecutter"] == "other"
        },
        {
            "type": "confirm",
            "name": "poetry_adapted",
            "message": "Is the cookiecutter chosen adapted for Poetry?: ",
            "default": False,
            "when": lambda answers : quickstart is False
        },
        {
            "type": "confirm",
            "name": "upload_github",
            "message": "Create repo and upload to github?: ",
            "default": True,
            "when": lambda answers : (quickstart is False) and (poetry_adapted or answers["poetry_adapted"])
        },
        {
            "type": "input",
            "name": "commit_message",
            "message": "Message for Github commit",
            "default": ":tada: Initial commit",
            "when": lambda answers : upload_github and (quickstart is False)
        }
    ]
    
    try:
        parameters = prompt(questions, style=prompt_style)

        if (poetry_adapted or parameters["poetry_adapted"]) is False:
            upload_github = False
            parameters["upload_github"] = False

        if quickstart:
            create_project(
                parameters["project_name"],
                env_manager,
                create_env,
                parameters["cookiecutter"],
                upload_github,
                commit_message
            )
        else:
            create_project(
                parameters["project_name"],
                parameters["env_manager"],
                parameters["create_env"],
                parameters["cookiecutter"],
                parameters["upload_github"],
                parameters["commit_message"]
            )
    except KeyError:
        typer.Abort()


@app.command()
def push(
    commit_message: str = typer.Option(
        None,
        help="Commit message"
    )
) -> None:
    """
    Creates a local repository and pushed it to Github
    """
    parameter = prompt({
        "type": "input",
        "name": "commit_message",
        "message": "Please enter your commit message: ",
        "default": config["defaults"]["commit_message"]
    })

    if commit_message is None:
        commit_message = parameter["commit_message"]

    upload_to_github(commit_message)
