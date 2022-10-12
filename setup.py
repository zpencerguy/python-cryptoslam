from setuptools import setup, find_packages


requirements = ["requests>=2.28.1"]

setup(
    name='python-CryptoSlam',
    version='0.1.1',
    license='GPL2',
    author='no-name-user-name',
    url='https://cryptoslam.io',
    description='CryptoSlam API python wrapper',
    packages=find_packages(),
    install_requires=requirements,
    author_email='support@cryptoslam.io',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
