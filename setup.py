import setuptools

setuptools.setup(
    entry_points = {
        'console_scripts': [
            'moving_average = moving_average:main',
        ],
    }
)