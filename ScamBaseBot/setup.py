from setuptools import setup

setup(
    name="scambot",
    install_requires=[
        "python-telegram-bot[job-queue]==20.7",
        "telethon==1.34.0",
    ]
)