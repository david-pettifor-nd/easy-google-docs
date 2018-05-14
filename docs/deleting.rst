Deleting Files from Google Drive
********************************

You can delete any file from Google Drive so long as you know the File ID::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # Delete the file "budget1999.xlsx", which has a file ID of "XXXXXXXXXXXXXXXXXX":
    api.delete_file(file_id='XXXXXXXXXXXXXXXXXX')


There is also one for spreadsheets, which does nothing more than call the above function::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # Delete the file "budget1999.xlsx", which has a file ID of "XXXXXXXXXXXXXXXXXX":
    api.delete_spreadsheet(spreadsheet_id='XXXXXXXXXXXXXXXXXX')