from setuptools import setup, find_packages

setup(
    name='nopip',
    version='0.2.0',
    description='A simple module to install Python packages programmatically',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Ronivaldo Sampaio',
    author_email='ronivaldo@gmail.com',
    url='https://github.com/ronivaldo/nopip',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
