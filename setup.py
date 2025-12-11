from setuptools import setup

setup(
    name="yubikey-oath-dmenu",
    version="0.14.0",
    py_modules=["yubikey_oath_dmenu"],
    install_requires=[
        "click",
        "yubikey-manager>=4.0.0",
    ],
    entry_points={
        "console_scripts": [
            "yubikey-oath-dmenu=yubikey_oath_dmenu:cli",
        ],
    },
)
