import ast
import os

from setuptools import find_packages, setup


ROOT = os.path.dirname(__file__)
VERSION = None

with open(os.path.join(ROOT, 'src', 'shellingham', '__init__.py')) as f:
    for line in f:
        if line.startswith('__version__ = '):
            VERSION = ast.literal_eval(line[len('__version__ = '):]).strip()
if VERSION is None:
    raise EnvironmentError('failed to read version')


# Put everything in setup.cfg, except those that don't actually work?
setup(
    # These really don't work.
    package_dir={'': 'src'},
    packages=find_packages('src'),

    # I don't know how to specify an empty key in setup.cfg.
    package_data={
        '': ['version.txt', 'LICENSE*', 'README*'],
    },

    # I need this to be dynamic.
    version=VERSION,
)
