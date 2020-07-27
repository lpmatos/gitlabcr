# -*- coding: utf-8 -*-

import io
import os
from cloner import __version__
from setuptools import setup, find_packages

# Package meta-data.
NAME              = "gitlabcr"
DESCRIPTION       = "CLI to help you clone projects inside groups in Gitlab"
URL               = "https://github.com/lpmatos/gitlab-clone-recursive"
EMAIL             = "luccapsm@gmail.com"
AUTHOR            = "Lucca Pessoa da Silva Matos"
REQUIRES_PYTHON   = ">=3.6.0"
VERSION           = __version__

# What packages are required for this module to be executed?
REQUIRED = [
  "python-gitlab"
]

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
  with io.open(os.path.join(here, "README.md"), encoding="utf-8") as file:
    LONG_DESCRIPTION = "\n" + file.read()
except FileNotFoundError:
  LONG_DESCRIPTION = DESCRIPTION

setup(
  name = NAME,
  version = VERSION,
  description = DESCRIPTION,
  long_description = DESCRIPTION,
  long_description_content_type = "text/markdown",
  author = AUTHOR,
  author_email = EMAIL,
  python_requires = REQUIRES_PYTHON,
  url=URL,
  packages = find_packages(include=["gitlabcr"], exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
  install_requires = REQUIRED,
  include_package_data = True,
  license = "MIT license",
  keywords = [
    "gitlab",
    "gitlab-api",
    "cli",
    "python"
  ],
  entry_points = {
    "console_scripts" : [
      "gitlabcr=gitlabcr.cli:main",
    ]
  },
  zip_safe = False,
)
