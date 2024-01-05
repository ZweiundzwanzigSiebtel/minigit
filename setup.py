from setuptools import setup

from setuptools import setup

setup(
    name='minigit',
    version='0.1',
    packages=['minigit'],
    entry_points={
        'console_scripts': [
            'minigit=minigit.cli:main',  # Beachte den Doppelpunkt und die Funktion
        ],
    },
)

