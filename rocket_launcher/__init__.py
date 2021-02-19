"""Top-level package for rocket_launcher."""
import configparser
import os

from dotenv import load_dotenv
from PyInquirer import style_from_dict, Token


__author__ = """Andrea Rondón Villanueva"""
__email__ = 'andrea.estefania.rv@gmail.com'
__version__ = '0.1.0-alpha'

# Read environmental variables
load_dotenv("../.env")
PROJECTS_DIR = os.getenv("PROJECTS_DIR")
CONFIG_FILE = os.getenv("CONFIG_FILE")


# Read configuration file
config = configparser.ConfigParser()
config.read(str(CONFIG_FILE))

# Set prompt style
prompt_style = style_from_dict({
    Token.QuestionMark: "#ansigreen bold",
    Token.Question: "bold",
    Token.Pointer: "#ansiyellow bold",
    Token.Answer: "#ansiblue"
})
