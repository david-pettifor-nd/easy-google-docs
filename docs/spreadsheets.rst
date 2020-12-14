Spreadsheets (Google Sheets)
****************************

Downloading/Exporting Spreadsheets
==================================

Exporting spreadsheets from Google Sheets is actually done through the Google Drive API (and not the Google Sheets API as one might expect).  Only two things are required for this:

* Spreadsheet ID (File ID)
* Format (which can be any of the following defined formats in this library):

    * FORMAT_MS_EXCEL (format: '.xlsx')
    * FORMAT_OPEN_OFFICE_SHEET (format: '.ods')
    * FORMAT_PDF  (format: '.pdf')
    * FORMAT_CSV (format: '.csv' - single sheet/tab only)
    * FORMAT_TSV (format: '.tsv' - single sheet/tab only)
    * FORMAT_HTML (format: '.zip' file of each sheet/tab as an HTML file/table)


Download As Excel File
+++++++++++++++++++++++

You can download the entire file as a MS Excel Spreadsheet File::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, FORMAT_MS_EXCEL
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Download the spreadsheet with a File ID "XXXXXXXXXXXXXXXXXX" to the Desktop
    file_path = api.download_spreadsheet_to_file(spreadsheet_id='XXXXXXXXXXXXXXXXXX', download_location='~/Desktop/', format=FORMAT_MS_EXCEL)


Download Specific Tab as CSV
+++++++++++++++++++++++++++++

Sometimes we only one a single sheet/tab of our workbook, especially when we're downloading it as a CSV file.  You can do this by specifying either the tab index (0-based index, so "tab_index=0" is the first tab), or by the tab's name.  Here, we download it by index::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, FORMAT_CSV
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Download the second tab/sheet of the spreadsheet with a File ID "XXXXXXXXXXXXXXXXXX" to the Desktop
    file_path = api.download_spreadsheet_to_file(spreadsheet_id='XXXXXXXXXXXXXXXXXX', download_location='~/Desktop/', format=FORMAT_CSV, tab_index=1)

The above code works around a bit of what the Google Drive API v3 supports (as they do not support exporting other tabs as CSV natively).  It actually downloads the file as an Excel file (to get all tabs), and uses the Python library `xlrd <https://github.com/python-excel/xlrd>`_ to extract the specified tab's data (all in memory), then writes it to disk.


Download Spreadsheet in Memory
++++++++++++++++++++++++++++++

If you would rather get the data from your spreadsheet into memory-only (and avoid writing to disk immediately), you can::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, FORMAT_CSV
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Download the second tab/sheet of the spreadsheet with a File ID "XXXXXXXXXXXXXXXXXX" to memory (returns a io.ByteIO object
    sheet_data = api.download_spreadsheet(spreadsheet_id='XXXXXXXXXXXXXXXXXX', format=FORMAT_CSV, tab_index=1)

Note: the above function does support all export types, not just CSV!  Also, before returning, the ByteIO object returned is reset with `.seek(0)` so it is ready to be read at the beginning of the byte data.


Clearing Spreadsheets
=====================

If you want to clear the contents of a specific tab/sheet of a spreadsheet, this can easily be done with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Clear the contents of the second tab/sheet:
    api.clear_spreadsheet(spreadsheet_id='XXXXXXXXXXXXXXXXXX', tab_index=1)

Note: this clears *only the contents* and not the formatting of each cell.  All cell formatting (Date/Dollars/Numeric formatting) will remain.


Replacing Spreadsheets with Content
===================================

Sometimes we have updates we want to push to a specific spreadsheet tab and it's just easiest to replace the entire sheet's tab
with this new data.

Replacing with Raw Data
+++++++++++++++++++++++

If you have row data as a 2-dimensional array (a list of lists...the first list representing rows, each second list the column data)::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Example of what your row data could look like:
    row_data = [
        ['Name', 'Address', 'State'],   # first row -- header
        ['John', '123 Fake Street', 'AL']   # second row
        ['Jane', '456 Fake Street', 'AK']   # third row
    ]

    # Replace the second tab with our row data:
    api.replace_spreadsheet_with_rows(spread_sheet_id='XXXXXXXXXXXXXXXXXX', row_data=row_data, tab_index=1)


Replacing with CSV
++++++++++++++++++

Or sometimes you may just have a CSV file you want to replace the sheet with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Replace the second tab with the CSV file on our desktop:
    api.replace_spreadsheet_with_csv(spread_sheet_id='XXXXXXXXXXXXXXXXXX', csv_file_location='~/Desktop/data.csv', tab_index=1)

Note: for both _replacing_ functions, you can pass in an *input_type* parameter of:

* INPUT_TYPE_RAW - forces Google Sheets to not try to analyze the input (leaves formatting alone)
* INPUT_TYPE_AUTO - lets Google Sheets auto-format things like dates, decimals, etc.


Appending to Sheets
===================

Appending Raw Data to a Specific Spreadsheet Tab
++++++++++++++++++++++++++++++++++++++++++++++++

You can append to a spreadsheet (bottom of the table) with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Example of what your row data may look like:
    row_data = [
        ['John', '123 Fake Street', 'AL']   # first row to add
        ['Jane', '456 Fake Street', 'AK']   # second row to add
    ]

    # Append the row_data to the second tab of the sheet "XXXXXXXXXXXXXXXXXX"
    api.append_rows_to_spreadsheet(spreadsheet_id = 'XXXXXXXXXXXXXXXXXX' row_data=row_data, tab_index=1)

If you want to append to a sheet with a different starting column (default is *A1*), you can specify the starting range::

    # Example of what your row data may look like:
    row_data = [
        ['John', '123 Fake Street', 'AL']   # first row to add
        ['Jane', '456 Fake Street', 'AK']   # second row to add
    ]

    # Append the row_data to the second tab of the sheet "XXXXXXXXXXXXXXXXXX" starting in the "B" column
    api.append_rows_to_spreadsheet(spreadsheet_id = 'XXXXXXXXXXXXXXXXXX' row_data=row_data, tab_index=1, starting_range='B1')

Note: we still use "x1" to define the starting range even though we are not actually starting at *Row 1*.  With the *append* function, it will always insert into the spreadsheet after the last row which contains data.


Appending a CSV to a Specific Spreadsheet Tab
++++++++++++++++++++++++++++++++++++++++++++++++

You can append to a spreadsheet (bottom of the table) with::

    from easygoogledocs import GoogleAPI, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT
    api = GoogleAPI(credentials_file='credentials.json')

    # To authorize with a web-browser based OAuth Token:
    api.authorize(authentication_type=AUTH_TYPE_BROWSER)

    # To authorize with a service account:
    api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

    # Append the CSV "data.csv" to the second tab of the sheet "XXXXXXXXXXXXXXXXXX"
    api.append_rows_to_spreadsheet(spreadsheet_id = 'XXXXXXXXXXXXXXXXXX' csv_file='data.csv', tab_index=1)


Note: Both *append* functions also allow for *tab_name* to be used instead of *tab_index*.  Also, you can specify an *input_type* if you would rather the data be inserted as raw (INPUT_TYPE_RAW rather than the default INPUT_TYPE_AUTO)
