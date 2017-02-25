import codecs
import os
import re
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)

        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        sys.exit(pytest.main(self.test_args))


# Set run-time dependencies
dependencies = [
    'unityapiclient',
    'PyYAML',
]

# Set test dependencies
test_dependencies = [
    'pytest-cov',
    'pytest',
]

if sys.version_info < (2, 7):
    # Workaround for atexit._run_exitfuncs error when invoking `test` with
    # older versions of Python
    try:
        import multiprocessing
    except ImportError:
        pass


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # Intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.rst')

setup(name='b2accessdeprovisioning',
      version=find_version('b2accessdeprovisioning', '__init__.py'),
      description=('B2ACCESS account (de)provisioning tool'),
      long_description=long_description,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='B2ACCESS account (de)provisioning tool',
      author='Nicolas Liampotis',
      author_email='nliam@grnet.gr',
      url='https://eudat-b2access.github.io/b2access-deprovisioning',
      download_url='https://github.com/EUDAT-B2ACCESS/b2access-deprovisioning',
      license='Apache License 2.0',
      packages=['b2accessdeprovisioning'],
      zip_safe=False,
      install_requires=dependencies,
      tests_require=test_dependencies,
      python_requires='>=2.6,<2.8',
      cmdclass={'test': PyTest},
)
