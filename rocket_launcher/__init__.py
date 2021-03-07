"""Top-level package for rocket_launcher."""
import os

from configparser import ConfigParser
from dotenv import load_dotenv
from pathlib import Path
from PyInquirer import style_from_dict, Token


__author__ = """Andrea Rondón Villanueva"""
__email__ = "andrea.estefania.rv@gmail.com"
__version__ = "0.1.0-alpha"

# Read environmental variables
load_dotenv()
CONFIG_FILE = Path(str(os.getenv("CONFIG_FILE")))

# Read ot create configuration file
config = ConfigParser()

if os.getenv("CONFIG_FILE") is None:
    config.add_section("general")
    config.add_section("defaults")
    config.add_section("cookiecutters")

    config["general"]["projects_dir"] = ""
    config["defaults"]["env_manager"] = ""
    config["defaults"]["create_env"] = "True"
    config["defaults"]["poetry_adapted"] = "True"
    config["defaults"]["upload_github"] = "False"
    config["defaults"]["commit_message"] = "Test commit_message"
    config["defaults"]["quickstart"] = "True"

    CONFIG_FILE = Path.cwd().joinpath("config.ini")

    with open(CONFIG_FILE, "w") as file:
        config.write(file)
        file.close()

    with open(".env", "w") as file:
        file.write(f"CONFIG_FILE={str(CONFIG_FILE)}")

config.read(CONFIG_FILE)

# Set prompt style
prompt_style = style_from_dict(
    {
        Token.QuestionMark: "#ansigreen bold",
        Token.Question: "bold",
        Token.Pointer: "#ansiyellow bold",
        Token.Answer: "#ansiblue",
    }
)
