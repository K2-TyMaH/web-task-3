from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='Sorts any garbage in any folder =)',
    entry_points={
        'console_scripts': ['clean-folder=clean_folder.clean:main'],
    },
    url='https://github.com/K2-TyMaH/lesson7',
    author='TyMaH',
    license='MIT',
    packages=find_packages(),
)
