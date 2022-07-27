.. easy-google-docs documentation master file, created by
   sphinx-quickstart on Fri May 11 13:00:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Easy Google Docs
============================================

Quick Start
-----------

Install with::

   pip install easy-google-docs


Import with::

   from easygoogledocs import GoogleAPI

Authorize with either web-browser-based authentication::

   from easygoogledocs import AUTH_TYPE_BROWSER
   api = GoogleAPI(credentials_file='oauth_credentials.json')
   api.authorize(authentication_type=AUTH_TYPE_BROWSER)

Or authorize with a service account::

   from easygoogledocs import AUTH_TYPE_SERVICE_ACCOUNT
   api = GoogleAPI(credentials_file='service_account_credentials.json')
   api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

Examples
========

.. toctree::
   authentication.rst
   initialization.rst
   uploading.rst
   deleting.rst
   folders.rst
   spreadsheets.rst
   sharing.rst


Code Documentation
==================

.. toctree::
   code.rst



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
