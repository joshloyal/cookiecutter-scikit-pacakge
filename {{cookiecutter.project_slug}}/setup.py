from __future__ import print_function

import os
import sys
{% if cookiecutter.has_cython == 'y' -%}
import contextlib
import subprocess
import glob
{%- endif %}

from setuptools import setup, find_packages
{% if cookiecutter.has_cython == 'y' -%}
from setuptools import Extension
{%- endif %}


HERE = os.path.dirname(os.path.abspath(__file__))

# import ``__version__` from code base
exec(open(os.path.join(HERE, '{{cookiecutter.project_slug}}', 'version.py')).read())


with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]


with open('test_requirements.txt') as f:
    TEST_REQUIRES = [l.strip() for l in f.readlines() if l]


try:
    import numpy
except ImportError:
    print('numpy is required during installation')
    sys.exit(1)


try:
    import scipy
except ImportError:
    print('scipy is required during installation')
    sys.exit(1)


{% if cookiecutter.has_cython == 'y' -%}
@contextlib.contextmanager
def chdir(new_dir):
    old_dir = os.getcwd()
    try:
        sys.path.insert(0, new_dir)
        yield
    finally:
        del sys.path[0]
        os.chdir(old_dir)


def find_cython(dir, files=None):
    if files is None:
        files = []

    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isfile(path) and path.endswith(".pyx"):
            files.append(path.replace(os.path.sep, ".")[:-4])
        elif os.path.isdir(path):
            find_cython(path, files)

    return files


def clean(path):
    for name in find_cython(path):
        name = name.replace('.', os.path.sep)
        for ext in ['*.c', '*.so', '*.o', '*.html']:
            file_path = glob.glob(os.path.join(path, name + ext))
            if file_path and os.path.exists(file_path[0]):
                os.unlink(file_path[0])


def get_include():
    source_path = os.path.join(HERE, 'src')
    return source_path if os.path.exists(source_path) else ''


def get_sources():
    files = []
    source_path = get_include()
    if source_path:
        for name in os.listdir(src_path):
            path = os.path.join(src_path, name)
            if os.path.isfile(path) and path.endswith(".c"):
                files.append(path)

    return files


def generate_cython(cython_cov=False):
    print("Cythonizing sources")
    for source in find_cython(HERE):
        source = source.replace('.', os.path.sep) + '.pyx'
        cythonize_source(source, cython_cov)


def cythonize_source(source, cython_cov=False):
    print("Processing %s" % source)

    flags = ['--fast-fail']
    if cython_cov:
        flags.extend(['--directive', 'linetrace=True'])

    try:
        p = subprocess.call(['cython'] + flags + [source])
        if p != 0:
            raise Exception('Cython failed')
    except OSError:
        raise OSError('Cython needs to be installed')


def make_extension(ext_name, macros=[]):
    ext_path = ext_name.replace('.', os.path.sep) + '.c'
    mod_name = '.'.join(ext_name.split('.')[-2:])
    include_dirs = [numpy.get_include(), "."]
    if get_include():
        include_dirs = [get_include] + include_dirs
    return Extension(
        mod_name,
        sources=[ext_path] + get_sources(),
        include_dirs=include_dirs,
        extra_compile_args=["-O3", "-Wall", "-fPIC"],
        define_macros=macros)


def generate_extensions(macros=[]):
    ext_modules = []
    for mod_name in find_cython(HERE):
        ext_modules.append(make_extension(mod_name, macros=macros))

    return ext_modules
{%- endif %}

DISTNAME = '{{cookiecutter.project_name}}'
DESCRIPTION = '{{cookiecutter.project_short_description}}'
with open('README.rst') as f:
    LONG_DESCRIPTION = f.read()
MAINTAINER = '{{cookiecutter.full_name}}'
MAINTAINER_EMAIL = '{{cookiecutter.email}}'
URL = '{{cookiecutter.url}}'
DOWNLOAD_URL = '{{cookiecutter.pypi_url}}'
LICENSE = '{{cookiecutter.license}}'
VERSION = __version__
CLASSIFIERS = []


{% if cookiecutter.has_cython == 'y' %}
def setup_package():
    if len(sys.argv) > 1 and sys.argv[1] == 'clean':
        return clean(HERE)

    cython_cov = 'CYTHON_COV' in os.environ

    macros = []
    if cython_cov:
        print("Adding coverage information to cythonized files.")
        macros =  [('CYTHON_TRACE_NOGIL', 1)]

    with chdir(HERE):
        generate_cython(cython_cov)
        ext_modules = generate_extensions(macros=macros)
        setup(
            name=DISTNAME,
            maintainer=MAINTAINER,
            maintainer_email=MAINTAINER_EMAIL,
            description=DESCRIPTION,
            license=LICENSE,
            url=URL,
            version=VERSION,
            download_url=DOWNLOAD_URL,
            long_description=LONG_DESCRIPTION,
            zip_safe=False,
            classifiers=CLASSIFIERS,
            package_data={
                '': [
                    '{{cookiecutter.project_slug}}' + os.path.sep + '*.pyx',
                    '{{cookiecutter.project_slug}}' + os.path.sep + '.pxd'
                ]
            },
            include_package_data=True,
            packages=find_packages(),
            install_requires=INSTALL_REQUIRES,
            extras_require={'test': TEST_REQUIRES},
            setup_requires=['pytest-runner'],
            tests_require=TEST_REQUIRES,
            ext_modules=ext_modules
        )
{% else -%}
def setup_package():
    setup(
        name=DISTNAME,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        license=LICENSE,
        url=URL,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        long_description=LONG_DESCRIPTION,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        include_package_data=True,
        packages=find_packages(),
        install_requires=INSTALL_REQUIRES,
        extras_require={'test': TEST_REQUIRES},
        setup_requires=['pytest-runner'],
        tests_require=TEST_REQUIRES,
    )
{% endif -%}

if __name__ == '__main__':
    setup_package()
