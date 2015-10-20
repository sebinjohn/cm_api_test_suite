from test_api import TestApiResource

api = TestApiResource('test', 7180, 'test', 'test', 'test')

api.create_cluster('test-cluster')
cluster = api.get_cluster('test-cluster')
print cluster
