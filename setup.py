from setuptools import setup, find_packages

import go-template

def install_deps():
    """Reads requirements.txt and preprocess it
    to be feed into setuptools.
    This is the only possible way (we found)
    how requirements.txt can be reused in setup.py
    using dependencies from private github repositories.
    Links must be appendend by `-{StringWithAtLeastOneNumber}`
    or something like that, so e.g. `-9231` works as well as
    `1.1.0`. This is ignored by the setuptools, but has to be there.
    Returns:
         list of packages and dependency links.
    """
    with open('requirements.txt', 'r') as f:
        packages = f.readlines()
        new_pkgs = []
        for resource in packages:
                new_pkgs.append(resource.strip())
        return new_pkgs


setup(
        name='go-template',
        version=go_template.__version__,
        packages=find_packages(),
        description='python bindings for go template',
        author='harsh',
        author_email='harshjniitr@gmail.com',
        license='MIT',
        url='https://github.com/harsh-98/go-template',
        keywords='golang template bindings wrapper',
        install_requires=install_deps(),
        classifiers=['Development Status :: 3 - Alpha',
                     'Programming Language :: Python :: 2.6',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Programming Language :: Python :: 3.6',
                     'License :: OSI Approved :: MIT License'],
)
