Sharing
*******

There are three levels of sharing a file:

* Read-only
* Read/Write
* Ownership -- Note!  Owernship cannot be transferred to different domains!

Sharing as Read-Only
++++++++++++++++++++

You can share a file with a specific user (knowing their email address) as read-only with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, PERMISSION_READ
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # share with "johndoe@gmail.com":
    api.share_document(file_id='XXXXXXXXXXXXXXXXXX', recipient_email='johndoe@gmail.com', share_permissions=PERMISSION_READ)

The user will then receive an email shortly with a link to view your document, but they will not be able to make changes to it.


Sharing with Read/Write
+++++++++++++++++++++++

You can also give a person permission to make changes to your document with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, PERMISSION_WRITE
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # share with "johndoe@gmail.com":
    api.share_document(file_id='XXXXXXXXXXXXXXXXXX', recipient_email='johndoe@gmail.com', share_permissions=PERMISSION_WRITE)

The user will then receive an email shortly with a link to edit your document.


Changing Ownership
++++++++++++++++++

You can give ownership to a file to a specific user (but it *must* be within the same domain as your account) with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, PERMISSION_OWNER
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # move ownership to "johndoe@gmail.com":
    api.share_document(file_id='XXXXXXXXXXXXXXXXXX', recipient_email='johndoe@gmail.com', share_permissions=PERMISSION_OWNER)

Note: only the user will then be able to control sharing access and change ownerships.  Once you let go of ownership, you cannot take it back yourself!

Service Account Ownership
+++++++++++++++++++++++++

It might be recommended to set the *auto_ownership* flag in the initialization to *True* and define your email when using a service account.  When you upload a file using a service account authentication method, the file will be *owned by that account, and not you!*.  In fact, unless you specifically share the file with yourself, you will not be able to see the file you just uploaded.

However, you can have any uploaded file be automatically transferred to you being the owner by setting the right flags upon initialization of your API::

    from easygoogledocs import GoogleAPI
    api = GoogleAPI(credentials_file='credentials.json', auto_ownership=True, default_owner_email='YOUREMAIL@gmail.com')

Doing this will automatically move ownership to the email address in `default_owner_email` any time a new file is created/uploaded.


Revoking Access
+++++++++++++++

You can revoke access from a user to a specific file with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Revoke permission for "johndoe@gmail.com" from accessing the file
    api.revoke_permission(file_id='XXXXXXXXXXXXXXXXXX', user_emal='johndoe@gmail.com')

Note: this will remove *ALL* permissions that *johndoe@gmail.com* may have on the file.  You cannot revoke Ownership.