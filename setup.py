from setuptools import setup, find_packages

setup(
    name='SurakshaMitra',
    version='1.1.0',
    packages=find_packages(),
    install_requires=[],  
    author='kashyap',
    author_email='prajapatikashyap14@gmail.com',
    description='A Python package for password strength checking, strong password generation, and email validation.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kashyapprajapat/SurakshaMitra',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
