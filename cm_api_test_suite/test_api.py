from test_cluster import TestApiCluster

class TestApiResource(object):
    def __init__(self, host, port, user_name, password, version=9):
        self.api_host = host
        if port:
            if type(port) != int and not None:
                raise Exception('port should be an integer')
            else:
                self.api_port = port

        self.api_user = user_name
        self.api_pass = password
        if version < 9:
            raise Exception('API version should be >= 9')
        self.api_version = version
        self.clusters = {}

    def create_cluster(self, cluster_name):
        try:
            cluster = TestApiCluster(cluster_name)
            self.clusters[cluster_name] = cluster
            return cluster
        except Exception as e:
            return None

    def get_all_clusters(self):
        return ['test-cluster']

    def get_cluster(self, cluster_name):
        if not self.clusters.has_key(cluster_name):
            raise Exception('No cluster exist')
        return self.clusters[cluster_name]
