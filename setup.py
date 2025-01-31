from setuptools import setup, find_packages

setup(
    name='SurakshaMitra',
    version='2.1.0',
    packages=find_packages(),
    install_requires=[
        'phonenumbers', 
    ],  
    author='Kashyap Prajapati',
    author_email='prajapatikashyap14@gmail.com',
    description='A Python package for validating emails, phone numbers, password strength checking, strong password generation, and file validation.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/kashyapprajapat/SurakshaMitra',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
        'Topic :: Security',
    ],
    python_requires='>=3.6',
)
