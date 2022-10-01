from setuptools import find_packages, setup

setup(
    name='magic_eden',
    packages=find_packages(),
    version='0.0.5',
    description='Python wrap for NFT marketplace api MagicEden',
    author='ivan.srshtn.crypto@gmail.com',
    license='MIT',
    install_requires=[
        'requests==2.26.0'
    ]
)
