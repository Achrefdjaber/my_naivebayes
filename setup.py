from setuptools import setup, find_packages

setup(
    name='my_naivebayes',
    version='1.0.0',
    packages=find_packages(),
    description='A simple Naive Bayes classifier for continuous data',
    author='Achref DJABER',
    author_email='achrefdjaber2@gmail.com',
    license='MIT',
    install_requires=['numpy'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
