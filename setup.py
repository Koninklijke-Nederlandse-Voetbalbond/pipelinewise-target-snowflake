#!/usr/bin/env python

from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = f.read()

setup(name="pipelinewise-target-snowflake",
      version="2.3.0",
      description="Singer.io target for loading data to Snowflake - PipelineWise compatible",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="Wise",
      url='https://github.com/transferwise/pipelinewise-target-snowflake',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ],
      py_modules=["target_snowflake"],
      python_requires='>=3.7',
      install_requires=[
          'pipelinewise-singer-python==1.*',
          'snowflake-connector-python[pandas]==3.5.0',
          'inflection==0.5.1',
          'joblib==1.2.0',
          'numpy==1.26.4',
          'boto3==1.28.20',
          'jsonschema==3.2.0',
          'attrs==23.2.0',
          'six==1.14.0',
          'python-dateutil==2.8.2',
          'cffi==1.15.0',
          "cryptography==3.4.8",
          "packaging==23.2",
          "charset-normalizer==3.2.0",
          "certifi==2024.6.2"
      ],
      extras_require={
          "test": [
              "pylint==2.12.*",
              'pytest==7.4.0',
              'pytest-cov==3.0.0',
              "python-dotenv>=0.19,<1.1"
          ]
      },
      entry_points="""
          [console_scripts]
          target-snowflake=target_snowflake:main
      """,
      packages=find_packages(exclude=['tests*']),
      )
