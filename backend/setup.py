import os

from setuptools import setup, find_packages

requires = [
    'pyramid',
    "pymongo"
    ]

setup(name='server',
      version='0.0',
      description='server',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author="Anthony Pizzimenti",
      author_email="pizzimentianthony@gmail.com",
      url="apizzimenti.com",
      keywords="sumthing something learn learnsumthing anthony high school learning",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = server:main
      """,
      )
