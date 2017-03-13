import db4iot
import trimet
import boto3



class DataLoader():

    def fetch_latest_bus_times(self):
        """
        Fetch current bus times using TriMet's API
        """
        pass

    def fetch_historical_bus_times(self):
        """
        Fetch older bus data using db4iot's API
        Starts on August 17th, 2016
        """
        pass

    def prep_data(self):
        """
        Add any extra attributes, change data types, etc
        """
        pass

    def save(self):
        """
        1) Save raw json to disk / S3

        2) Save prepped data to database
        """
        pass


