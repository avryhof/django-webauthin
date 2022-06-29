#!/usr/bin/env python

from webauthin import __version__

from setuptools import setup, find_packages  # noqa


def read(filename: str):
    with open(filename) as file:
        return file.read()


setup(
    name="django-webauthin",
    version=__version__,
    author="Stavros Korokithakis",
    author_email="hi@stavros.io",
    url="https://gitlab.com/stavros/django-webauthin",
    description="Passwordless authentication using WebAuthn",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    license="BSD",
    keywords="django",
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "django>=3.2",
        "webauthn>=1.0.0",
    ],
    packages=find_packages(),
    python_requires=">=3.6",
)
