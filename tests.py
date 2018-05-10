import unittest
import os
from easygoogle import GoogleAPI, BROWSER_FIREFOX, AUTH_TYPE_BROWSER, AUTH_TYPE_SERVICE_ACCOUNT, FORMAT_CSV, \
    FORMAT_MS_EXCEL, FORMAT_PDF, FORMAT_HTML


class GoogleAPIAuthTestCase(unittest.TestCase):
    """Tests authentication"""

    # def test_missing_credentials(self):
    #     api = GoogleAPI(enable_drive=True, enable_sheets=True)
    #     self.assertRaises(FileNotFoundError, api.authorize, AUTH_TYPE_BROWSER, BROWSER_FIREFOX)

    # def test_web_authorization(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #
    #     self.assertTrue(api.authorize(authentication_type=AUTH_TYPE_BROWSER))
    #
    # def test_invalid_auth_type(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     self.assertRaises(AttributeError, api.authorize, 'account')
    #
    # def test_upload_and_delete_file(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #     file_meta = api.upload_file(file_location='/home/parallels/Desktop/drive_logo.png')
    #     self.assertTrue(('name' in file_meta) and (file_meta['name'] == 'drive_logo.png'))
    #
    #     response = api.delete_file(file_id=file_meta['id'])
    #     self.assertTrue(response)
    #
    # def test_service_account_authorization(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #
    #     self.assertTrue(api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT))

    # def test_create_folder_and_upload_to_folder(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     # create folder
    #     folder_meta = api.create_folder(folder_name='TEST Folder')
    #     self.assertTrue(('name' in folder_meta) and (folder_meta['name'] == 'TEST Folder'))
    #
    #     file_meta = api.upload_file(file_location='/home/parallels/Desktop/drive_logo.png', parent_id=folder_meta['id'])
    #     self.assertTrue(('name' in file_meta) and (file_meta['name'] == 'drive_logo.png'))
    #
    #     # verify this is in the parent folder
    #     parent_ids = api.get_parent_ids(file_id=file_meta['id'])
    #     self.assertIn(folder_meta['id'], parent_ids)
    #
    #     # delete the file
    #     response = api.delete_file(file_id=file_meta['id'])
    #     self.assertTrue(response)
    #
    #     # delete the folder
    #     response = api.delete_file(file_id=folder_meta['id'])
    #     self.assertTrue(response)

    # def test_upload_spreadsheet(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_meta = api.upload_spreadsheet('/home/parallels/Desktop/example_sheet.csv')
    #     self.assertIn('name', file_meta)
    #     self.assertEqual(file_meta['name'], 'example_sheet.csv')
    #     self.assertEqual(file_meta['mimeType'], 'application/vnd.google-apps.spreadsheet')
    #
    #     response = api.delete_file(file_id=file_meta['id'])
    #     self.assertTrue(response)

    # def test_upload_document(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_meta = api.upload_spreadsheet('/home/parallels/Desktop/Test Doc.docx')
    #     self.assertIn('name', file_meta)
    #     self.assertEqual(file_meta['name'], 'Test Doc.docx')
    #     self.assertEqual(file_meta['mimeType'], 'application/vnd.google-apps.document')
    #
    #     response = api.delete_file(file_id=file_meta['id'])
    #     self.assertTrue(response)

    # def test_download_spreadsheet_csv(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_location = api.download_spreadsheet_to_file(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk', download_location='/home/parallels/Desktop/', format=FORMAT_CSV, tab_index=1)
    #     self.assertTrue(os.path.exists(file_location))
    #     os.remove(file_location)
    #
    # def test_download_spreadsheet_excel(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_location = api.download_spreadsheet_to_file(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk', download_location='/home/parallels/Desktop/', format=FORMAT_MS_EXCEL)
    #     self.assertTrue(os.path.exists(file_location))
    #     os.remove(file_location)
    #
    # def test_download_spreadsheet_pdf(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_location = api.download_spreadsheet_to_file(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk', download_location='/home/parallels/Desktop/', format=FORMAT_PDF)
    #     self.assertTrue(os.path.exists(file_location))
    #     os.remove(file_location)
    #
    # def test_download_spreadsheet_html(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     file_location = api.download_spreadsheet_to_file(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk', download_location='/home/parallels/Desktop/', format=FORMAT_HTML)
    #     self.assertTrue(os.path.exists(file_location))
    #     os.remove(file_location)

    # def test_append_data_to_sheet(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     response = api.append_rows_to_spreadsheet(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk', row_data=[[1, 2], [3, 4]])
    #     self.assertEquals(response['updates']['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

    # def test_append_csv_to_sheet(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     response = api.append_file_to_spreadsheet(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk',
    #                                         csv_file='/home/parallels/Desktop/upload_test.csv')
    #     self.assertEquals(response['updates']['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

    # def test_clear_sheet_by_tab_name(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     response = api.clear_spreadsheet(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk',
    #                                      tab_name='Errors')
    #     self.assertEquals(response['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

    # def test_clear_sheet_by_tab_index(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     response = api.clear_spreadsheet(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk',
    #                                      tab_index=1)
    #     self.assertEquals(response['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

    # def test_replace_sheet_with_csv(self):
    #     parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    #     credentials_file = os.path.join(parent_dir, 'service_credentials.json')
    #     api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
    #     api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)
    #
    #     response = api.replace_spreadsheet_with_csv(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk',
    #                                                 tab_index=1, csv_file_location='/home/parallels/Desktop/upload_test.csv')
    #     self.assertEquals(response['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

    def test_replace_sheet_with_rows(self):
        parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        credentials_file = os.path.join(parent_dir, 'service_credentials.json')
        api = GoogleAPI(credentials_file=credentials_file, enable_drive=True, enable_sheets=True)
        api.authorize(authentication_type=AUTH_TYPE_SERVICE_ACCOUNT)

        response = api.replace_spreadsheet_with_rows(spreadsheet_id='1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk',
                                                     tab_index=1, row_data=[['Hello', 'there!'], ['Its-a', 'me,', 'Mario!']])
        self.assertEquals(response['spreadsheetId'], '1J-pqwboTrt6PWiQSOJrM3qvT9xCxqpnqaSVcf5AUfuk')

if __name__ == '__main__':
    unittest.main()
