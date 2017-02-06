import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('pytn-2017-centos')


def test_nginx_user(User):
    u = User('nginx')

    assert u.exists
    assert u.home == '/var/lib/nginx'


def test_index_file(File):
    f = File('/usr/share/nginx/html/index.html')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755

    assert f.contains('Test Your Automation!')
    assert f.contains('Molecule CentOS')
    assert f.contains('Ansible managed:')
