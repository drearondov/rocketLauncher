from __future__ import print_function, unicode_literals

import os
import subprocess
import typer

from pathlib import Path
from PyInquirer import prompt

from rocket_launcher import prompt_style, config, PROJECTS_DIR, CONFIG_FILE


def create_config(
    env_manager: str = None,
    create_env: bool = None,
    poetry_adapted: bool = None,
    upload_github: bool = None,
    commit_message: str = None,
    quickstart: bool = None
) -> None:

    questions = [
        {
            "type": "list",
            "name": "env_manager",
            "message": "What environment manager do you use?: ",
            "choices": ["pyenv", "conda"],
            "when": lambda answers : env_manager is None
        },
        {
            "type": "confirm",
            "name": "create_env",
            "message": "Create a new virtual environment?: ",
            "when": lambda answers : create_env is None
        },
        {
            "type": "confirm",
            "name": "poetry_adapted",
            "message": "Does your cookiecutters work with Poetry by default?: ",
            "when": lambda answers : poetry_adapted is None
        },
        {
            "type": "confirm",
            "name": "upload_github",
            "message": "Upload to github?: ",
            "when": lambda answers : upload_github is None
        },
        {
            "type": "input",
            "name": "commit_message",
            "message": "Deafult commit message?: ",
            "when": lambda answers : commit_message is None
        },
        {
            "type": "confirm",
            "name": "quickstart",
            "message": "Use defaults when creating new projects?: ",
            "when": lambda answers : quickstart is None
        }
    ]

    try:
        typer.echo(typer.style("\n== Set up your defaults ==", fg="blue", bold=True))
        parameters = prompt(questions, style=prompt_style)

        config["defaults"]["env_manager"] = str(parameters["env_manager"])
        config["defaults"]["create_env"] = str(parameters["create_env"])
        config["defaults"]["poetry_adapted"] = str(parameters["poetry_adapted"])
        config["defaults"]["upload_github"] = str(parameters["upload_github"])
        config["defaults"]["commit_message"] = str(parameters["commit_message"])
        config["defaults"]["quickstart"] = str(parameters["quickstart"])

        with open(Path(str(CONFIG_FILE)), "w") as configfile:
            config.write(configfile)

        typer.echo("\nDefaults set, you're good to go!")
    except KeyError:
        typer.Abort()



def create_project(
    project_name: str,
    env_manager: str,
    create_env: bool,
    cookiecutter: str,
    upload_github: bool,
    commit_message: str
) -> None:
    
    if create_env is True:
        if env_manager == "pyenv":
            subprocess.run([env_manager, "virtualenv", project_name])
        else:
            subprocess.run([env_manager, "create", "--name", project_name])

    subprocess.run([env_manager, "activate", project_name])

    os.chdir(Path(str(PROJECTS_DIR)))

    subprocess.run(["cookiecutter", cookiecutter])

    os.chdir(project_name)

    with open(".todo", "w") as f:
        f.close()

    with open(".env", "w") as f:
        f.close()

    subprocess.run(["git", "init"])
    
    if upload_github:
        upload_to_github(commit_message)


def install_dependencies(package_manager: str):
    if package_manager == "pip":
        subprocess.run([package_manager, "install", "-r", "requirements.txt"])
    elif package_manager == "conda":
        subprocess.run([package_manager, "install", "--file", "requirements.txt"])
    elif package_manager == "poetry":
        dependencies = {}
        
        # Install requirements.txt with poetry
        pass
    else:
        return "Package manager not supported, if your want to propose a feature, submit a request or read the CONTRIBUTING guidelines."


def upload_to_github(commit_message: str) -> None:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", commit_message])

    subprocess.run(["gh", "repo", "create"])
    subprocess.run(["git", "push", "origin", "master"])
