from distutils.core import setup
setup(
  name = 'helmpy',
  packages = ['helmpy'],
  version = '0.0.1',
  license='MIT',
  description = 'A Python library that facilitates Kubernetes resource templating and generation into Helm charts',
  author = 'Segev Burstein',
  author_email = 'segev608@gmail.com',
  url = 'https://github.com/user/reponame',
  download_url = '',
  keywords = ['Kubernetes', 'Helm'],
  install_requires=['validators', 'beautifulsoup4'],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Code Generators',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.10',
  ],
)