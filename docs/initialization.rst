Installation and Initialization
*******************************

Once you have your credentials, you can install the package with::

    pip install easy-google-docs


Importing and authentication
============================

Knowing where your credentails.json file is, you can initialize and authenticate with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)


