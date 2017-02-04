Setup
=====

* Install Docker if you haven't already.

        https://www.docker.com/products/docker

* Pull down the base images we are going to use.

        docker pull solita/ubuntu-systemd
        docker pull solita/centos-systemd

* Clone the tutorial git repository.

        git clone https://github.com/signed8bit/pytn-2017.git
        cd pytn-2017

* Install our requirements using Python 2.7.x, preferably in venv.

        mkvirtualenv pytn-2017
        pip install -r requirements.txt

* Initialize Molecule to use Docker and Testinfra.

        molecule init --driver docker --verifier testinfra

* Edit `molecule.yml` to use the Docker images we pulled.

        docker:
          containers:
            - name: pytn-2017-ubuntu
              image: solita/ubuntu-systemd
              image_version: latest
              privileged: True
              port_bindings:
                80: 8082
              ansible_groups:
                - group1
                
            - name: pytn-2017-centos
              image: solita/centos-systemd
              image_version: latest
              privileged: True
              port_bindings:
                80: 8083
              ansible_groups:
                - group1

* Create our initial test container.

        molecule create
