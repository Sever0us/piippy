from setuptools import setup

setup(name='piippy',
      version='0.1',
      description='A package for managing headless device IP addresses on a network',
      url='https://github.com/Sever0us/piippy',
      author='Matt Griffiths',
      author_email='griff@me3d.com.au',
      license='MIT',
      packages=['piippy'],
      install_requires=['flask', 'requests'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      zip_safe=False)