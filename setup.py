from setuptools import setup

setup(name='xcmodelcreate',
      version='0.3.9',
      description='Generates models in an xcode project based on a JSON string',
      url='http://github.com/valdirunars/xcmodelcreate',
      author='DeveloThor',
      author_email='valdirunars@gmail.com',
      license='MIT',
      packages=['xcmodelcreate'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['xcmodelcreate=xcmodelcreate.command_line:main'],
    })
