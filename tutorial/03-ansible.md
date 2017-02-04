Ansible
=======


Idempotency
-----------

* Step 1 (Problem):

        - name: Touch idempotency.conf
          file:
            path: /etc/idempotency.conf
            state: touch
            
* Step 2 (Fix):

        - name: Check idempotency.conf
          stat:
            path: /etc/idempotency.conf
          register: idempotency_file
        
        - name: Touch idempotency.conf
          file:
            path: /etc/idempotency.conf
            state: touch
          when: not idempotency_file.stat.exists
          
          
Ansible Managed
---------------

    {{ ansible_managed }}
