from setuptools import setup

setup(
    name='DicewarePasswordGenerator',
    version='1.0',
    py_modules=['diceware'],
    install_requires=[
        'Click',
    ],
    entry_points="""
        [console_scripts]
        diceware=diceware:cli
    """,
)
