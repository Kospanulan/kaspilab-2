class ProcessedData:
    def __init__(self, region, index, exchange, date, high, open, low, currency):
        self._region = region
        self._index = index
        self._exchange = exchange
        self._date = date
        self._high = high
        self._open = open
        self._low = low
        self._currency = currency

    def __init__(self, list_of_data):
        self._region = list_of_data[0]
        self._index = list_of_data[1]
        self._exchange = list_of_data[2]
        self._date = list_of_data[3]
        self._high = list_of_data[4]
        self._open = list_of_data[5]
        self._low = list_of_data[6]
        self._currency = list_of_data[7]

    def to_string(self):
        return "Object:\nRegion: " + self._region + '\n'\
                "Index: " + self._index + '\n'\
                "Exchange: " + self._exchange + '\n'\
                "Date: " + self._date.strftime("%d/%m/%Y") + '\n'\
                "High value: " + str(self._high) + '\n'\
                "Open value: " + str(self._open) + '\n'\
                "Low value: " + str(self._low) + '\n'\
                "Currency: " + str(self._currency)

    def get_region(self):
        return self._region

    def get_index(self):
        return self._index

    def get_exchange(self):
        return self._exchange

    def get_date(self):
        return self._date.strftime("%d/%m/%Y")

    def get_dm_date(self):
        return self._date.strftime("%d/%m")

    def get_my_date(self):
        return self._date.strftime("%m/%Y")

    def get_year(self):
        return int(self._date.strftime("%Y"))

    def get_month(self):
        return int(self._date.strftime("%m"))

    def get_day(self):
        return int(self._date.strftime("%d"))

    def get_high(self):
        return self._high

    def get_open(self):
        return self._open

    def get_low(self):
        return self._low

    def get_currency(self):
        return self._currency

    def set_region(self, region):
        self._region = region

    def set_index(self, index):
        self._index = index

    def set_exchange(self, exchange):
        self._exchange = exchange

    def set_date(self, date):
        self._date = date

    def set_high(self, high):
        self._high = high

    def set_open(self, open):
        self._open = open

    def set_low(self, low):
        self._low = low

    def set_currency(self, currency):
        self._currency = currency
