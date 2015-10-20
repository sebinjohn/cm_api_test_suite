from test_service import TestApiService

class TestApiCluster(object):
    available_services = {}
    def __init__(self, cluster_name):
        self.cluster_name = cluster_name
        self.supported_services = [
            'ZooKeeper',
            'HDFS',
            'MapReduce',
            'Hive',
            'Oozie',
            'Impala'
        ]
    def get_cluster_name(self):
        return self.cluster_name

    def get_all_services(self):
        return self.available_services.values()

    def get_service(service_name):
        return available_services[service_name]

    def create_service(service_name):
        if service_name not in supported_services:
            raise Exception('Not a supported service')
        try:
            service = TestApiService(service_name)
            service.name = service_name
            available_services[service_name] = service
            return service
        except Exception as e:
            return None
