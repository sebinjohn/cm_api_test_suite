import unittest
from mock_cm_api.test_api import TestApiResource

class TestApiTestResource(unittest.TestCase):
    def test_create_resource(self):
        api = TestApiResource('test', 7180, 'test', 'test', 'test')
        self.assertIsNotNone(api, "api object is None")

    def test_create_cluster(self):
        api = TestApiResource('test', 7180, 'test', 'test', 'test')
        cluster = api.create_cluster('test-cluster')
        self.assertIsNotNone(api, "cluster object is None")

    def test_get_cluster(self):
        api = TestApiResource('test', 7180, 'test', 'test', 'test')
        cluster_a = api.create_cluster('test-cluster')
        cluster_b = api.get_cluster('test-cluster')
        self.assertIsNotNone(cluster_a)
        self.assertIsNotNone(cluster_b)
        self.assertEqual(cluster_a, cluster_b)

    def test_get_all_clusters(self):
        api = TestApiResource('test', 7180, 'test', 'test', 'test')
        cluster_1 = api.create_cluster('test-cluster1')
        cluster_2 = api.create_cluster('test-cluster2')
        cluster_list = api.get_all_clusters()
        self.assertEqual(cluster_1.get_cluster_name(), 'test-cluster1')
        self.assertEqual(cluster_2.get_cluster_name(), 'test-cluster2')
