# Walkthrough – RichTech University IAM Lab

This walkthrough guides you through the RichTech University IAM Lab, simulating a higher education environment with SSO, MFA, LDAP, and RBAC.

This project was built and tested using **VMware Workstation** with the following virtual machines:

- **VM 1 – Shibboleth Identity Provider**
  - OS: Ubuntu Server 22.04 LTS
  - Services: Shibboleth IdP, Duo MFA plugin

- **VM 2 – Shibboleth Service Provider**
  - OS: Ubuntu Server 22.04 LTS
  - Services: Apache HTTPD, Shibboleth SP

- **VM 3 – OpenLDAP Directory**
  - OS: Ubuntu Server 22.04 LTS
  - Services: slapd, LDAP user store

- **VM 4 – Grouper UI + MariaDB (RichTech IAM Lab only)**
  - OS: Ubuntu Server 22.04 LTS
  - Services: Grouper Access Manager, Database

- **Networking:**  
  All VMs are bridged on the same virtual network segment and communicate securely over HTTPS using self-signed SSL certificates.


## 📚 Official Documentation

- [Shibboleth IdP](https://shibboleth.atlassian.net/wiki/spaces/IDP5/)
- [Shibboleth SP](https://shibboleth.atlassian.net/wiki/spaces/SP3/)
- [OpenLDAP](https://www.openldap.org/doc/)
- [Grouper Access Management](https://spaces.at.internet2.edu/display/Grouper/)
- [Duo MFA for Shibboleth](https://duo.com/docs/shibboleth)
- [VMware Workstation](https://www.vmware.com/products/workstation-pro.html)
