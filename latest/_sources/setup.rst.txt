.. _setup:

=====
Setup
=====

This document describes how to install the stable version or the bleeding edge code into your Python environment.

Stable code
^^^^^^^^^^^

Installing GA4GH Phenopacket Core is easy - we publish the releases on `PyPi <https://pypi.org/project/ga4gh-phenopacket-core>`_.

Therefore, the latest stable release can be installed by running::

  python3 -m pip install ga4gh-phenopacket-core

The bleeding edge code
^^^^^^^^^^^^^^^^^^^^^^

To access the bleeding edge features, the development version can be installed by::

  git clone https://github.com/monarch-initiative/ga4gh-phenopacket-core.git
  cd ga4gh-phenopacket-core
  git checkout development && git pull
  python3 -m pip install .

This will clone the Git repository into your machine, switch to the `development` branch,
and install `ga4gh-phenopacket-core` into the active Python environment,
assuming you have privileges to install packages.

Run tests
^^^^^^^^^

The contributors may want to run the unit tests and the integration tests to ensure all features work as expected.

Before running tests, make sure you install GA4GH Phenopacket Core with `test` dependencies::

  python3 -m pip install .[test]

The unit tests, integration tests, doctests, and the tutorial scripts can the be running by invoking the `pytest` runner::

  pytest

.. note::

  The library *must* be installed in the environment before running all tests.

That's all for the setup!
