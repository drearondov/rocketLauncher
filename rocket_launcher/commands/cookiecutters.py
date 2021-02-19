import typer

from PyInquirer import prompt

from rocket_launcher import config


cookiecutters = typer.Typer()


@cookiecutters.command()
def add(
    alias: str = typer.Option(
        None,
        help="Alias for the new cookiecutter"
    ),
    link: str = typer.Option(
        None,
        help="Link of the cookiecutter, to use with cookiecutter command"
    )
) -> None:
    """
    Adds new cookiecutter to curated cookiecutters
    """
    questions = [
        {
            "type": "input",
            "name": "alias",
            "message": "what do you want to call your cookiecutter?: ",
            "when": lambda answers : alias is None
        },
        {
            "type": "input",
            "name": "link",
            "message": "Link for the cookiecutter command: ",
            "when": lambda answers : link is None
        }
    ]

    parameters = prompt(questions)

    if alias is None:
        alias = parameters["alias"]
    
    if link is None:
        link = parameters["link"]

    config["cookiecutters"][alias] = link

    with open("config.ini", "w") as configfile:
        config.write(configfile)
        configfile.close()


@cookiecutters.command(name="list")
def list_cookiecutters():
    """
    List all the cookiecutters available
    """
    typer.echo(typer.style("\n== Available cookiecutters ==", fg="blue", bold=True))
    
    for cookiecutter in config["cookiecutters"]:
        if cookiecutter == "other":
            continue
        typer.echo(typer.style("* ", fg="green", bold=True), nl=False)
        typer.echo(cookiecutter)
