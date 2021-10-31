from setuptools import setup, find_packages

setup(
    name='aso-command-cli',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'docker'
    ],
    entry_points='''
        [console_scripts]
        aso-cli=asocli.asocli:asocli
    ''',
)
