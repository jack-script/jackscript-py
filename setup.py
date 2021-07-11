from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='jackscript',
  version='0.1.0',
  description='A math lib of sets.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://jackscript.macbase.co.za',  
  author='Daniel Romeo Mamphekgo',
  author_email='danielromeo99@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Sets', 
  packages=find_packages(),
  install_requires=[''] 
)