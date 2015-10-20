from test_service import TestApiService

class TestApiCluster(object):

    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.available_services = [
            'ZooKeeper',
            'HDFS',
            'MapReduce',
            'Hive',
            'Oozie',
            'Impala'
        ]

    def get_all_services(self):
        return self.services.keys()

    def get_service(service_name):
        return self.services[service_name]

    def create_service(service_name):
        if service_name not in available_services:
            raise Exception('Not a supported service')
        try:
            service = TestApiService(service_name)
            self.services[service_name] = service
            return service
        except Exception as e:
            return None
