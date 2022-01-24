import os
from setuptools import setup, find_packages

DESCRIPTION = '`beautify` allows us to add color to text, banners, menu options in the terminal application.'
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(name='kmy-beautify',
      version='0.0.1',
      packages=find_packages(),
      include_package_data=True,
      description=DESCRIPTION,
      long_description=README,
      author='Exso Kamabay',
      author_email='<lexyong66@gmail.com>',
      url='https://github.com/ExsoKamabay/Api-scrap',
      long_description_content_type='text/markdown',
      license='Apache License 2.0',
      install_requires=['shell==1.0.1', 'string-color==1.2.1', 'art==4.8'],
      keywords=['text', 'color', 'terminal', 'loading terminal','menu terminal','text color text color terminal','exso','kamabay'],
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
      ],
      )
