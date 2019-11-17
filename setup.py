import os
from setuptools import setup

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package or package.startswith('#'):
                continue
            lst.append(package.strip())
    return lst

setup(name='pyAudioAnalysis',
      version='0.2.5',
      description='Python Audio Analysis Library: Feature Extraction, Classification, Segmentation and Applications',
      url='https://github.com/tyiannak/pyAudioAnalysis',
      author='Theodoros Giannakopoulos',
      author_email='tyiannak@gmail.com',
      license='Apache License, Version 2.0',
      packages=['pyAudioAnalysis'],
      zip_safe=False,
      install_requires=get_reqs('requirements.txt'))
