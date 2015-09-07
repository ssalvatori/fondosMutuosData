import xlrd
from datetime import datetime

class Daily_Information(object):

    def __init__(self, date, file_name):
        ''' Return a daily_information object for an given date '''

        date_object = datetime.strptime(date,"%Y-%m-%d")

        self.year = date_object.year
        self.day = date_object.day
        self.month = date_object.month
        self.information = []
        self.file_name = file_name

    def load_information(self):
        ''' Load data from file_name '''
        try:
            self._parse_file()
            self._store_information()
        except:
            print

        return True

    def _parse_file(self):
        ''' Parse xls file '''
        try:
            workbook = xlrd.open_workbook(self.file_name, encoding_override='cp1252')
            worksheet = workbook.sheet_by_index(0)

            for row in range(worksheet.nrows)

                


        except exc:
            print exc


    def get_information(self):
        return self.information
