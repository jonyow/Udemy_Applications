

import pandas_datareader as pdd
import datetime

startdate = datetime.datetime(2016,11,10)
enddate = datetime.datetime(2017,6,30)

pdd.DataReader(name = 'BARC.L', data_source='google', start= startdate, end=enddate).head()