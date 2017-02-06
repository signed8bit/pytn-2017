import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('pytn-2017-ubuntu')


def test_nginx_user(User):
    u = User('www-data')

    assert u.exists
    assert u.home == '/var/www'


def test_index_file(File):
    f = File('/var/www/html/index.html')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755

    assert f.contains('Test Your Automation!')
    assert f.contains('Molecule Ubuntu')
    assert f.contains('Ansible managed:')
