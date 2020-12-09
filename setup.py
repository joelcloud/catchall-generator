from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='catchall-generator',
    version='1.0',
    author='joelcloud',
    license='MIT',
    description='Generate emails for your catchall adress.',
    long_description=long_description,
    url='https://github.com/joelcloud/catchall-generator',
    packages=find_packages(),
)