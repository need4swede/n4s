import setuptools

# for pip >= 10
from pip._internal.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name='n4s',
    version='2.2.5',
    author='Mike Afshari',
    author_email='theneed4swede@gmail.com',
    description='Collection of useful methods by Need4Swede',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/n4s/n4s',
    license='MIT',
    install_requires=load_requirements("requirements.txt"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)