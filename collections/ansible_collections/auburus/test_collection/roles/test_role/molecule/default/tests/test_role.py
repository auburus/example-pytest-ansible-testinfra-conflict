import testinfra.host as host

def test_role(host: host):
    assert host.file('/tmp/file.txt').exists
