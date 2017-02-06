import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_hosts_file(File):
    f = File('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_nginx_package(Package):
    p = Package('nginx')

    assert p.is_installed
    assert p.version.startswith("1.")


def test_nginx_running_and_enabled(Service):
    s = Service("nginx")

    assert s.is_running
    assert s.is_enabled
