# Installation

Since the nature of this package is very opinionated (meaning, made with me in mind) I will not be publishing to `pypi`. But if you would like to use it, this are the installation steps.

## Prerequisites

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

## From sources

The sources for rocketLauncher can be downloaded from the [Github repo](https://github.com/drearondov/rocket_launcher).

Bear in mind that to install this package from source you will need to have [Poetry](https://python-poetry.org) installed in your system.

With that in mind, you can either clone the public repository:

```bash 
    git clone git://github.com/drearondov/rocket_launcher
```

Or download the [tarball](https://github.com/drearondov/rocket_launcher/tarball/master):

```bash
    curl -OJL https://github.com/drearondov/rocket_launcher/tarball/master
```

Once you have a copy of the source, you can install it with:

```bash
    poetry build
    poetry install
```
