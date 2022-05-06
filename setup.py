from setuptools import setup
setup(
    name = 'weather',
    version = '0.1.0',
    packages = ['weather'],
    entry_points = {
        'console_scripts': [
            'weather = weather.__main__:main'
        ]
    })