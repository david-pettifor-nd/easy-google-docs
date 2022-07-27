Folders
*******

Folders in Google Drive are nothing more than blank files with a specific type.  They are given an ID so any other file can use that ID as part of their "parent" field.

Creating Folders
++++++++++++++++

To create a folder::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Create a folder named "My Stuff":
    mystuff_meta = api.create_folder(folder_name='My Stuff')


Creating Sub-folders
++++++++++++++++++++
Knowing the folder's meta data, we can also create sub-folders by passing in the "Parent ID" of the previous folder.
So to create a sub-folder "Photos" under the previous "My Stuff"::

    photo_folder_meta = api.create_folder(folder_name='Photos', parent_id=mystuff_meta['id'])

Getting Parent Folder Information:
++++++++++++++++++++++++++++++++++

You may also obtain the parent folder's information if you know your file's data.  In this example, we can verify that the "Photos" folder has the "My Stuff" folder as its parent::

    parent_meta = api.get_parent_ids(file_id=photo_folder_meta['id'])

    print(parent_meta)  # Should print the same ID as the one we find in `mystuff_meta['id']`

