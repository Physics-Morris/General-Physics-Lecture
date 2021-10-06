from setuptools import find_packages, setup
setup(
    name='StephCurry',
    packages=find_packages(),
    version='1.1',
    description='Basketball trajectory model',
    author='Morris',
    license='MIT',
    install_requires=['numpy', 'scipy', 'matplotlib']
)