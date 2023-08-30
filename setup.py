from setuptools import setup

setup(
    name='moving_average_cli',
    version='1.0',
    install_requires=[
        'pytest==7.1.1'
    ],
    entry_points = {
        'console_scripts': [
            'moving_average = moving_average:main',
        ],
    }
)