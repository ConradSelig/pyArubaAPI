from distutils.core import setup

setup(
    name='pyArubaAPI',
    version='0.0.1',
    packages=[''],
    url='https://github.com/ConradSelig/pyArubaAPI',
    license='GNU Affero General Public License v3.0',
    author='Conrad Selig',
    author_email='conrad+pyarubaapi@conradselig.dev',
    description='A nicely bundled API for Aruba Switches. Uses base Python requests library.',
)

install_requires = [
    'certifi',
    'charset-normalizer',
    'colorama',
    'colorful',
    'idna',
    'prettyprinter',
    'Pygments',
    'pyjson5',
    'requests',
    'urllib3',
]