# Rocket Launcher

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/drearondov/rocketlauncher?include_prereleases&style=flat-square) ![Travis (.com)](https://img.shields.io/travis/com/drearondov/rocketlauncher?style=flat-square)  ![GitHub](https://img.shields.io/github/license/drearondov/rocketlauncher?style=flat-square) ![Codestyle](https://img.shields.io/badge/code%20style-black-333333?style=flat-square)

A **very** opinionated CLI to automate the start of a new project.

* Free software: GNU General Public License v3
* Documentation: https://rocket-launcher.readthedocs.io.

## Features

* Select environment manager (`pyenv`, `conda` supported)
* Create new virtual environment by default
* Create folder structure from cookiecutter
* Choose to create repository and upload project to Github
* Configure defaults values
* Quickstart a new project with default values

## Installation

Since the nature of this package is very opinionated (meaning, made with me in mind) I will not be publishing to `pypi`. But if you would like to use it, this are the installation steps.

### Prerequisites

For rocketLauncher to work the followinng packages need to be installed.

* [pyenv](https://github.com/pyenv/pyenv)
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
* [conda](https://docs.conda.io/projects/conda/en/latest/index.html)
* [cookiecutter](https://github.com/audreyr/cookiecutter)
* [git](https://git-scm.com)
* [GithubCLI](https://cli.github.com)

Once installed you can use the following code to get the latest release.

```bash
    repo='https://github.com/drearondov/rocketLauncher'

    # Find the latest release.
    latest=$(git ls-remote --tags --refs $repo | # Fetch remote tags.
                     sort -t '/' -k 3 -V |       # Sort them by version.
                     tail -n 1 |                 # Take the latest one.
                     awk -F / '{print $3}')      # Return only the tag.

    # Craft the URL for the release asset.
    version=$(echo $latest | tr -d 'v')  # Remove the leading v.
    wheel="rocket_launcher-${version}-py3-none-any.whl"
    release="${repo}/releases/download/${latest}/${wheel}"

    # Install the release.
    pip install $release
```

## Usage

The available commands are:

* `rocketlauncher init`: Configures the projects directory and logs in to Github
* `rocketlauncher new`: Creates a new project and runs a cookiecutter inside
* `rocketlauncher push`: Creates local repository and pushes to Github
* `rocketlauncher config`: Allows the creation of a configuration file and edit/set defaults
* `rocketlauncher cookiecutters`: Add/ view available cookiecutters
## Credits

This package was created with Cookiecutter and the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.
