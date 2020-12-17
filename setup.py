from setuptools import setup


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
    extras_require={
        'tests': [
            'pytest',
            'pytest-cov',
        ]
    },
    classifiers=[],
)
