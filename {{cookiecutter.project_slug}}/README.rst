.. -*- mode: rst -*-

|Travis|_ |AppVeyor|_ |Coveralls|_ |CircleCI|_ |License|_

.. |Travis| image:: https://travis-ci.org/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.svg?branch=master
.. _Travis: https://travis-ci.org/{{cookiecutter.github_username}}/cookiecutter.project_slug}}

.. |AppVeyor| image:: https://ci.appveyor.com/api/projects/status/54j060q1ukol1wnu/branch/master?svg=true
.. _AppVeyor: https://ci.appveyor.com/project/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/history

.. |Coveralls| image:: https://coveralls.io/repos/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/badge.svg?branch=master
.. _Coveralls: https://coveralls.io/github/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}?branch=master

.. |CircleCI| image:: https://circleci.com/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}tree/master.svg?style=svg
.. _CircleCI: https://circleci.com/gh/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/tree/master

{% if cookiecutter.license == 'MIT' -%}
.. |License| image:: https://img.shields.io/badge/License-MIT-blue.svg
.. _License: https://opensource.org/licenses/MIT
{% elif cookiecutter.license == 'BSD' %}
.. |License| image:: https://img.shields.io/badge/License-BSD%203--Clause-blue.svg
.. _License: https://opensource.org/licenses/BSD-3-Clause
{% elif cookiecutter.license == 'Apache' %}
.. |License| image:: https://img.shields.io/badge/License-Apache%202.0-blue.svg
.. _License: https://opensource.org/licenses/Apache-2.0
{% elif cookiecutter.license == 'GPLv2' %}
.. |License| image:: https://img.shields.io/badge/License-GPL%20v2-blue.svg
.. _License: https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html
{% elif cookiecutter.license == 'GPLv3' %}
.. |License| image:: https://img.shields.io/badge/License-GPL%20v3-blue.svg
.. _License: https://www.gnu.org/licenses/gpl-3.0
{% endif %}

.. _scikit-learn: https://github.com/scikit-learn/scikit-learn

{{cookiecutter.project_name}}
=============================
{{cookiecutter.project_short_description}} It is compatible with scikit-learn_.


Documentation / Website: {{ cookiecutter.url }}


Example
-------
.. code-block:: python

    print("Hello, world!")

Installation
------------

Dependencies
------------
{{ cookiecutter.project_name }} requires:

- Python (>= 2.7 or >= 3.4)
- NumPy (>= 1.8.2)
- SciPy (>= 0.13.3)
- Scikit-learn (>=0.17)

Additionally, to run examples, you need matplotlib(>=2.0.0).

Installation
------------
You need a working installation of numpy and scipy to install {{cookiecutter.project_name}}. If you have a working installation of numpy and scipy, the easiest way to install {{cookiecutter.project_slug}} is using ``pip``::

    pip install -U {{ cookiecutter.project_slug }}

If you prefer, you can clone the repository and run the setup.py file. Use the following commands to get the copy from GitHub and install all the dependencies::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
    cd {{ cookiecutter.project_slug }}
    pip install .

Or install using pip and GitHub::

    pip install -U git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git


Testing
-------
After installation, you can use pytest to run the test suite via setup.py::

    python setup.py test

References:
-----------
