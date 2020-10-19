from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'bouquetserviceimage' # Must be replaced by your <storage_account_name>
    account_key = '+DT+nPCXj1Jy8RWGJVWgDHXYKOJQTojg5Z7Coh45UBpGqZvEeYEGywT2JJT/1tJSyRhnlbKqystFISNNi4ygzQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'bouquetserviceimage' # Must be replaced by your storage_account_name
    account_key = '+DT+nPCXj1Jy8RWGJVWgDHXYKOJQTojg5Z7Coh45UBpGqZvEeYEGywT2JJT/1tJSyRhnlbKqystFISNNi4ygzQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None