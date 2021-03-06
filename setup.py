from setuptools import setup, find_packages
import os


def get_version():
    with open(os.path.join(os.path.dirname(__file__), "requests_tracker", "__init__.py")) \
            as version_file:
        # File has format: __version__ = '{version_number}'
        for line in version_file.readlines():
            if line.startswith('__version__'):
                parts = line.split("=")
                version_number = parts[1].strip().replace("'", "")
                return version_number


setup(
    name="requests-tracker",
    version=get_version(),
    author="Kobus Roux",
    url="https://github.com/eladeon/requests-tracker-python",
    license="MIT",
    description="HTTP Python Request Tracker",
    long_description="Useful python library to analyse, develop and run web scrapers using HAR and markdown files",
    test_suite="tests",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "setuptools",
        "MarkupSafe==2.0.0",  # Jinja2 issue (ImportError: cannot import name 'soft_unicode' from 'markupsafe')
        "Jinja2",
        "requests",
        "requests-mock",
        "argparse",
        "urllib3"
    ],
)
