from setuptools import setup

APP = ['app.py']
DATA_FILES = ['save.txt']
OPTIONS = {
    'iconfile':'cion.icns',
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
)