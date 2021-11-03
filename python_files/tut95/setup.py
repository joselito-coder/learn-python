from setuptools import setup

with open('readme.txt','r') as readme:
    long_desc = readme.read()


setup(name='konodioda',
      version="0.1",
      description="This is a dio package",
      long_description=long_desc,
      long_description_content_type="text/plain",
      author="Dio Brandi",
      install_requires =[],
      packages=['konodioda'],
    )