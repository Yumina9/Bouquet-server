from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'bouquetserviceimage'
    account_key = '+DT+nPCXj1Jy8RWGJVWgDHXYKOJQTojg5Z7Coh45UBpGqZvEeYEGywT2JJT/1tJSyRhnlbKqystFISNNi4ygzQ==' 
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'bouquetserviceimage' 
    account_key = '+DT+nPCXj1Jy8RWGJVWgDHXYKOJQTojg5Z7Coh45UBpGqZvEeYEGywT2JJT/1tJSyRhnlbKqystFISNNi4ygzQ==' 
    azure_container = 'static'
    expiration_secs = None