import os
import re
from pathlib import Path
from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r"""__version__ = ['"]([0-9.]+)['"]""")


def get_version():
    init_path = os.path.join(ROOT, "src", "pytest_stepfunctions", "__init__.py")
    print(init_path)
    init = open(init_path).read()
    print(f"{init=}")
    return VERSION_RE.search(init).group(1)


setup(
    name="pytest-stepfunctions",
    version=get_version(),
    author="Che-Hsun Liu & Bus Patrol Inc",
    author_email="support@buspatrol.com",
    description="A package for executing local modules in the AWS Stepfunction Docker container",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/buspatrol/pytest-stepfunctions",
    setup_requires=["setuptools_scm"],
    use_scm_version=True,
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["pytest"],
    entry_points={"pytest11": ["pytest-stepfunctions = pytest_stepfunctions.plugin"]},
    classifiers=[
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.6",
)
