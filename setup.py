import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.rst").read_text(encoding="utf-8")


setup(
    name="pyedgeconnect",
    use_scm_version={
        "write_to": "_version.py",
        "write_to_template": 'version = "{version}"\n',
    },
    setup_requires=["setuptools_scm"],
    description="A Python wrapper for Aruba Orchestrator and Edge Connect API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/SPOpenSource/edgeconnect-python",
    author="Zach Camara",
    author_email="zachary.camara@hpe.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: DevOps / Network Engineers",
        "Topic :: Automation Development :: Aruba Edge Connect",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    keywords="silver peak, silverpeak, silver peak python, aruba edge connect, edge connect",
    packages=find_packages(),
    package_dir={"pyedgeconnect": "pyedgeconnect"},
    python_requires=">=3.9, <4",
    zip_safe=False,
    install_requires=["requests"],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "flake8-rst-docstrings",
            "isort",
            "sphinx",
            "sphinx_rtd_theme",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/SPOpenSource/edgeconnect-python/issues",
        "Source": "https://github.com/SPOpenSource/edgeconnect-python/",
    },
)
