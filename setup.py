#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
      long_description = f.read()

setup(name="pipelinewise-target-bigquery",
      version="1.0.4",
      description="Singer.io target for loading data to BigQuery - PipelineWise compatible",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author="TransferWise",
      url='https://github.com/transferwise/pipelinewise-target-bigquery',
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python :: 3 :: Only'
      ],
      py_modules=["target_bigquery"],
      install_requires=[
          'singer-python==5.1.1',
          'psycopg2==2.8.2',
          'inflection==0.3.1',
          'joblib==0.13.2'
      ],
      entry_points="""
          [console_scripts]
          target-bigquery=target_bigquery:main
      """,
      packages=["target_bigquery"],
      package_data = {},
      include_package_data=True,
)