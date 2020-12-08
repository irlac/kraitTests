from setuptools import setup, find_packages


setup(
    name='kraitTests',
    author='Camden',
    author_email='richtercamden@gmail.com',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['click'],
    tests_require=['flake8', 'pytest', 'pytest-cov', 'mypy'],
    extras_require={
        'tests': ['flake8', 'pytest', 'pytest-cov', 'mypy'],
    },
    entry_points={
        'console_scripts': ['kraitTests = kraitTests.main:main']
    },
)
