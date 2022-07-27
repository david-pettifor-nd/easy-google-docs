Uploading Documents to Drive
****************************

The document uploader will let Google try to figure out which kind of document it is.  For most cases, this will work fine.

You can easily upload a file with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Upload the file "MyFinalPaper.docx" to my root drive folder:
    file_meta = api.upload_document(document_location="MyFinalPaper.docx")

    # Or if you want to upload it to a specific folder, you'll need to know the folder's ID:
    file_meta = api.upload_document(document_location="MyFinalPaper.docx", parent_id='FOLDER_ID')


Or if you want to upload specifically to Google Sheets::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Upload the file "Expenses.xlsx" to my root drive folder:
    file_meta = api.upload_spreadsheet(document_location="Expenses.xlsx")

    # Or if you want to upload it to a specific folder, you'll need to know the folder's ID:
    file_meta = api.upload_spreadsheet(document_location="Expenses.xlsx", parent_id='FOLDER_ID')

Specifying Mimetypes
--------------------

You can upload a file and specify which mime-type the file is if you would rather not let Google try to figure it out::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Upload the file "leafy_autumn.jpg" to my root drive folder:
    file_meta = api.upload_file(document_location="leafy_autumn.jpg", mime_type='application/vnd.google-apps.photo')


Supported Mime-Types
++++++++++++++++++++

You can view a compelte list of supported mime-types (and where Google will default the opening application) at:

https://developers.google.com/drive/v3/web/mime-types

