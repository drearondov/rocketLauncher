rocketLauncher CLI
==================

A **very** opinionated CLI to automate the start of a new project.

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Contents:

    installation
    usage
    contributing
    authors
    changelog

Features
********

* Select environment manager (``pyenv``, ``conda`` supported)
* Create new virtual environment by default
* Create folder structure from cookiecutter
* Choose to create repository and upload project to Github
* Configure defaults values
* Quickstart a new project with default values

Basic usage
***********

The available commands are:

* ``rocketlauncher init``: Configures the projects directory and logs in to Github
* ``rocketlauncher new``: Creates a new project and runs a cookiecutter inside
* ``rocketlauncher push``: Creates local repository and pushes to Github
* ``rocketlauncher config``: Allows the creation of a configuration file and edit/set defaults
* ``rocketlauncher cookiecutters``: Add/ view available cookiecutters

Credits
*******

This package was created with Cookiecutter and the `audreyr/cookiecutter-pypackage`_ project template.

.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
