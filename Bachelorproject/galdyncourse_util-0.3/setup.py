from setuptools import setup

long_description = "Tools accompanying the notes on Galactic Structure and Dynamics by Jo Bovy"

setup(name='galdyncourse_util',
      version='0.3',
      description='Course tools for Galactic Structure and Dynamics',
      author='Jo Bovy',
      author_email='bovy@astro.utoronto.ca',
      license='MIT',
      long_description=long_description,
      url='https://github.com/jobovy/GalacticStructureAndDynamics',
      package_dir = {'galdyncourse_util/': ''},
      packages=['galdyncourse_util','galdyncourse_util/load'],
      package_data={},
      install_requires=['numpy','astropy']
      )
