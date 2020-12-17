import re

from setuptools import setup
from setuptools.command.test import test


# use pytest instead
def run_tests(self):
    pyc = re.compile(r'\.pyc|\$py\.class')
    test_file = pyc.sub('.py', __import__(self.test_suite).__file__)
    raise SystemExit(__import__('pytest').main(['-vv', test_file]))
test.run_tests = run_tests


setup(
    name='ingreedypy',
    py_modules=['ingreedypy'],
    version='1.3.2',
    description='ingreedy-py parses recipe ingredient lines into a object',
    author='Scott Cooper',
    author_email='scttcper@gmail.com',
    url='https://github.com/openculinary/ingreedy-py',
    keywords=['ingreedy', 'ingreedypy', 'recipe', 'parser'],
    install_requires=[
        'parsimonious'
    ],
    tests_require=['pytest'],
    test_suite='ingreedytest',
    classifiers=[],
)
