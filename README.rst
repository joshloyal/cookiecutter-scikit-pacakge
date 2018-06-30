cookiecutter-scikit-package
===========================

Cookiecutter template for scikit-learn style packages (the ones I write most often)

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet::

    pip install -U cookiecutter

Generate a Scikit package project::

    cookiecutter https://github.com/joshloyal/cookiecutter-scikit-package.git

Then:

* Create a repo and put it there.

.. code-block:: bash

    git init
    git add *
    git add .travis.yml .gitignore
    git commit -m 'first commit'
    git remote add origin git@github.com:username/repo-name.git
    git push -u origin master

* Add the repo to your Travis-CI_ account.
* Register your project with PyPI.
* Run the Travis CLI command `travis encrypt -add deploy.password` to encrypt your PyPI password in Travis config and activate automated deployment on PyPI when you push a new tag to the master branch.
* Release your package by pushing a new tag to master.


.. _Travis-CI: http://travis-ci.org/
.. _Sphinx: http://sphinx-doc.org/
.. _PyPi: https://pypi.python.org/pypi
