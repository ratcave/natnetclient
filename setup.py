from setuptools import setup, find_packages

setup(name='NatNetClient',
      version='0.8',
      description='Client for getting Optitrack data from Motive through the NatNet Stream.',
      author='Nicholas A. Del Grosso',
      author_email='delgrosso@bio.lmu.de',
      url='https://www.github.com/neuroneuro15/natnetclient',

      packages=find_packages(),
      classifiers= [
            "Programming Language :: Python",
            "Development Status :: 4 - Beta",
            "Operating System :: OS Independent",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            ],
      test_suite='tests',
      )