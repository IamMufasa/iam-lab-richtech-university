
# RichTech University IAM Lab – Full Walkthrough

This project simulates an enterprise-level Identity & Access Management (IAM) environment for a fictional university (RichTech University), using open-source tools to demonstrate federated authentication, role-based access control (RBAC), directory integration, and MFA enforcement.

---

## 🧭 Overview

This IAM lab includes:
- Shibboleth SP and IdP (SAML 2.0)
- OpenLDAP as the central identity store
- Duo MFA plugin integrated at the IdP
- Grouper for group-based access and RBAC
- Attribute mapping, SAML assertion flow, and federated login simulation

---

## 🖥️ Virtual Lab Setup

Built using **VMware Workstation** with the following virtual machines:

| VM | OS | Purpose |
|----|----|---------|
| VM1 | Ubuntu Server 22.04 | Shibboleth IdP + Duo MFA plugin |
| VM2 | Ubuntu Server 22.04 | Shibboleth SP (Apache HTTPD) |
| VM3 | Ubuntu Server 22.04 | OpenLDAP Directory |
| VM4 | Ubuntu Server 22.04 | Grouper UI + MariaDB |

- All VMs are bridged on a shared virtual network
- Self-signed SSL certificates used for HTTPS
- Hostname mappings managed via local DNS or `/etc/hosts`

---

## 🧱 Architecture Diagram

```text
                           +------------------------+
                           |  User (Web Browser)    |
                           +-----------+------------+
                                       |
                          Access Request / Login Attempt
                                       |
                                       v
          +----------------------------+----------------------------+
          |      Shibboleth Service Provider (Apache HTTPD)         |
          +----------------------------+----------------------------+
                                       |
                                SAML AuthnRequest
                                       |
                                       v
   +-----------------------------+-----------------------------+
   |     Shibboleth Identity Provider (IdP + Duo MFA Plugin)   |
   +----------+----------------+------------------+------------+
              |                                   |
   Attribute Lookup                     Group Check / Entitlements
              |                                   |
              v                                   v
+----------------------------+         +-----------------------------+
|     OpenLDAP Directory     |         |     Grouper Access Manager  |
|     (Authentication)       |         |  (Group-based RBAC + DB)    |
+----------------------------+         +-----------------------------+
                                                  ^
                                     SAML Response / Assertion with Attributes


- **Networking:**  
  All VMs are bridged on the same virtual network segment and communicate securely over HTTPS using self-signed SSL certificates.


© 2025 Richie — Built to showcase real-world IAM skills.

## 📚 Official Documentation

- [Shibboleth IdP](https://shibboleth.atlassian.net/wiki/spaces/IDP5/)
- [Shibboleth SP](https://shibboleth.atlassian.net/wiki/spaces/SP3/)
- [OpenLDAP](https://www.openldap.org/doc/)
- [Grouper Access Management](https://spaces.at.internet2.edu/display/Grouper/)
- [Duo MFA for Shibboleth](https://duo.com/docs/shibboleth)
- [VMware Workstation](https://www.vmware.com/products/workstation-pro.html)
