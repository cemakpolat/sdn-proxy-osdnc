import os

from setuptools import setup, find_packages


def read(fname):
    readme_file_path = os.path.join(os.path.dirname(__file__), fname)

    if os.path.exists(readme_file_path) and os.path.isfile(readme_file_path):
        readme_file = open(readme_file_path)
        return readme_file.read()
    else:
        return "The SoftFIRE OpenSDNCore Controller Proxy"


setup(
    name="sdn-proxy-osdnc",
    version="1.0.0",
    author="SoftFIRE",
    author_email="softfire@softfire.eu",
    description="The SoftFIRE OpenSDNCore Controller Proxy",
    license="Apache 2",
    keywords="python vnfm nfvo open baton openbaton sdk experiment manager softfire tosca openstack rest",
    url="http://softfire.eu/",
    packages=find_packages(),
    scripts=["manager"],
    install_requires=[
        'bottle',
        'requests',
    ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",

    ],
)
