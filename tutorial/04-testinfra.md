Testinfra
=========


Package Assertions
------------------

    def test_nginx_package(Package):
        p = Package('nginx')

        assert p.is_installed
        assert p.version.startswith("1.")


Service Assertions
------------------

    def test_nginx_running_and_enabled(Service):
        s = Service("nginx")
        
        assert s.is_running
        assert s.is_enabled


Tests for Individual Hosts
--------------------------

    import testinfra.utils.ansible_runner
    
    testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        '.molecule/ansible_inventory').get_hosts('pytn-2017-centos')
        
    
    import testinfra.utils.ansible_runner
    
    testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        '.molecule/ansible_inventory').get_hosts('pytn-2017-ubuntu')
        
        
User Assertions
---------------

CentOS 

    def test_nginx_user(User):
        u = User('nginx')
        
        assert u.exists
        assert u.home == '/var/lib/nginx'
        
Ubuntu
    
    def test_nginx_user(User):
            u = User('www-data')
            
            assert u.exists
            assert u.home == '/var/www'
    
            
File Assertions
---------------

All

    def test_idempotency_file(File):
        f = File('/etc/idempotency.conf')
    
        assert f.exists
        
CentOS

    def test_index_file(File):
        f = File('/usr/share/nginx/html/index.html')
    
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o755
    
        assert f.contains('Test Your Automation!')
        assert f.contains('Molecule CentOS')

Ubuntu

    def test_index_file(File):
        f = File('/var/www/html/index.html')
    
        assert f.exists
        assert f.user == 'root'
        assert f.group == 'root'
        assert f.mode == 0o755
    
        assert f.contains('Test Your Automation!')
        assert f.contains('Molecule Ubuntu')


        
    
