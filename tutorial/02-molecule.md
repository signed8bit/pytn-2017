Molecule
========


Defining the test sequence
--------------------------

        molecule:
          test:
            sequence:
              - destroy
              - syntax
              - create
              - converge
              - idempotence
              - verify


Defining multiple images
------------------------

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
            

Preventing container destruction
--------------------------------

        molecule test --destroy never
