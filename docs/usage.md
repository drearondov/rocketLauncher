# Usage

**Usage**:

```console
$ rocketLauncher [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `config`: Create configuration file and/or set defaults
* `cookiecutters`: List/ add available cookiecutters
* `init`: Configure the projects directory and login to...
* `new`: Creates new project in folder, runs a...
* `push`: Creates a local repository and pushed it to...

## `rocketLauncher config`

Create configuration file and/or set defaults

**Usage**:

```console
$ rocketLauncher config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `change`: Change a default
* `init`: Define default configuration

### `rocketLauncher config change`

Change a default

**Usage**:

```console
$ rocketLauncher config change [OPTIONS]
```

**Options**:

* `--key TEXT`: Name of the value to change
* `--new-value TEXT`: New default value
* `--help`: Show this message and exit.

### `rocketLauncher config init`

Define default configuration

**Usage**:

```console
$ rocketLauncher config init [OPTIONS]
```

**Options**:

* `--env-manager TEXT`: Environment manager to use by default
* `--create-env / --no-create-env`: Create a virtual environment by default
* `--poetry-adapted / --no-poetry-adapted`: Are the cookiecutters used adapted for Poetry by default
* `--upload-github / --no-upload-github`: Upload to github by default
* `--commit-message TEXT`: Deafult commit message
* `--quickstart / --no-quickstart`: Use quickstart by default or interactive prompt
* `--help`: Show this message and exit.

## `rocketLauncher cookiecutters`

List/ add available cookiecutters

**Usage**:

```console
$ rocketLauncher cookiecutters [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Adds new cookiecutter to curated...
* `list`: List all the cookiecutters available

### `rocketLauncher cookiecutters add`

Adds new cookiecutter to curated cookiecutters

**Usage**:

```console
$ rocketLauncher cookiecutters add [OPTIONS]
```

**Options**:

* `--alias TEXT`: Alias for the new cookiecutter
* `--link TEXT`: Link of the cookiecutter, to use with cookiecutter command
* `--help`: Show this message and exit.

### `rocketLauncher cookiecutters list`

List all the cookiecutters available

**Usage**:

```console
$ rocketLauncher cookiecutters list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `rocketLauncher init`

Configure the projects directory and login to Github.

**Usage**:

```console
$ rocketLauncher init [OPTIONS]
```

**Options**:

* `--projects-path DIRECTORY`: Directory where projects are located  [required]
* `--github-token TEXT`: Github token to be used to connect to Github
* `--set-config / --no-set-config`: Whether to set the default config now or not  [required]
* `--help`: Show this message and exit.

## `rocketLauncher new`

Creates new project in folder, runs a cookiecutter and uploads to github.

**Usage**:

```console
$ rocketLauncher new [OPTIONS]
```

**Options**:

* `--project-name TEXT`: Name of the project. To be used for the repo and virtual environment
* `--env-manager [conda|pyenv]`: Virtual environment manager used for the project  [default: pyenv]
* `--create-env / --no-create-env`: Boolean variable to tell if create or not a virtual environment.            If false, it activates the virtual environment  [default: True]
* `--cookiecutter TEXT`: Alias in curated list or link to a cookiecutter
* `--poetry-adapted / --no-poetry-adapted`: Is the cookiecutter chosen adapted for Poetry?  [default: True]
* `--upload-github / --no-upload-github`: Choose whether you create a repository and upload to Github or not  [default: False]
* `--commit-message TEXT`: Commit message  [default: :tada: initial commit]
* `--quickstart / --no-quickstart`: Choose all defaults  [default: True]
* `--help`: Show this message and exit.

## `rocketLauncher push`

Creates a local repository and pushed it to Github

**Usage**:

```console
$ rocketLauncher push [OPTIONS]
```

**Options**:

* `--commit-message TEXT`: Commit message
* `--help`: Show this message and exit.
