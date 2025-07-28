from setuptools import setup, find_packages

setup(
    name='security-log-parser',
    version='0.1.0',
    description='Parser de logs de seguridad para Blue Teams',
    author='Tu Nombre',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
)
