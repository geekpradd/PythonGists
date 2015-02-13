from setuptools import setup

try:
    import pypandoc
    description=pypandoc.convert('README.md','rst')
except:
    description=''
setup(name='PythonGists',
      version="1.1.3",
      description='A Python Module to create and access GitHub Gists',
      long_description=description,
      url='https://github.com/geekpradd/PythonGists',
      author='Pradipta Bora',
      author_email='pradd@outlook.com',
      license='MIT',
      packages=['PythonGists'],
      install_requires=[
          'requests'   ],
      classifiers=[
          "Development Status :: 4 - Beta",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python"
      ],
      zip_safe=False)
