from setuptools import setup,find_packages
with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='pang',
    version='1.0',
    author='vycz',
    author_email='vycz@outlook.com',
    description='pang A stock',
    long_description=long_description,
    install_requires=[
        'click'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'pang=cli.pang:pang'
        ]
    }
)