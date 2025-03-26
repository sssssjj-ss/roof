#!/usr/bin/env python

from setuptools import setup

# 直接从文件定义版本号而不是从尚未安装的模块导入
__version__ = "75.8.0"

setup(name='web.py',
      version=__version__,
      description='web.py: makes web apps',
      author='Aaron Swartz',
      author_email='me@aaronsw.com',
      maintainer='Anand Chitipothu',
      maintainer_email='anandology@gmail.com',
      url='http://webpy.org/',
      packages=['web', 'web.wsgiserver', 'web.contrib'],
      long_description="Think about the ideal way to write a web app. Write the code to make it happen.",
      license="Public domain",
      platforms=["any"],
     )
