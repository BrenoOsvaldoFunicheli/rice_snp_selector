#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Breno Osvaldo Funicheli",
    author_email='osvaldobreno99@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={
        'console_scripts': [
            'rice_snp_selector=rice_snp_selector.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='rice_snp_selector',
    name='rice_snp_selector',
    packages=find_packages(include=['rice_snp_selector', 'rice_snp_selector.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/BrenoOsvaldoFunicheli/rice_snp_selector',
    version='0.1.0',
    zip_safe=False,
)
