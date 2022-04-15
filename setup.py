import pathlib
import pysenti
from setuptools import setup


# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="PySentiStrength",
    version=pysenti.__version__,
    description="Python 3 Wrapper for SentiStrength",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hykilpikonna/PySenti",
    author="Azalea Gui, Mike Thelwall",
    author_email="me@hydev.org, m.thelwall@wlv.ac.uk",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=['pysenti'],
    package_data={'pysenti': ['pysenti/*']},
    include_package_data=True,
    install_requires=['setuptools', 'typing_extensions'],
    # entry_points={
    #     "console_scripts": [
    #         "pysenti=pysenti.main:run",
    #     ]
    # },
)
