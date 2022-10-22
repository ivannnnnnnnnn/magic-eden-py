from setuptools import find_packages, setup

__version__ = "0.0.8"

setup(
    name='magic-eden-py',
    packages=find_packages(),
    version=__version__,
    description='Python wrap for api solana NFT marketplace MagicEden',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    project_urls={
        "Source Code": "https://github.com/ivannnnnnnnnn/magic-eden-py",
    },
    author='ivan.srshtn.crypto@gmail.com',
    license='MIT',
    install_requires=[
        'requests==2.26.0'
    ]
)
