
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

## 🔧 Setup Instructions

### 1. Shibboleth IdP
- Install via package manager
- Configure `idp.properties`, `relying-party.xml`
- Define SAML `entityID`
- Add Duo MFA login flow
- Import and trust SP metadata

### 2. Shibboleth SP
- Install Apache + Shibboleth module
- Protect `/secure` path with SP config
- Import IdP metadata
- Use self-signed cert for HTTPS

### 3. OpenLDAP
- Install with `slapd`
- Load users via LDIF with attributes:
  - `uid`, `mail`, `givenName`, `sn`, `eduPersonAffiliation`
- Set up bind DN and base DN

### 4. Grouper
- Install Grouper UI + WS + MariaDB backend
- Create groups like `students`, `faculty`, `it-admins`
- Assign group memberships
- Enable LDAP synchronization

---

## 🔐 Attribute Mapping (IdP)

| Attribute ID           | OID                                         | Description              |
|------------------------|---------------------------------------------|--------------------------|
| `mail`                 | `urn:oid:0.9.2342.19200300.100.1.3`         | Email address            |
| `givenName`            | `urn:oid:2.5.4.42`                          | First name               |
| `sn`                   | `urn:oid:2.5.4.4`                           | Last name                |
| `eduPersonAffiliation` | `urn:oid:1.3.6.1.4.1.5923.1.1.1.1`          | Affiliation (e.g. student) |

All attributes are defined in `attribute-resolver.xml` and released via `attribute-filter.xml`.

---

## 🧪 Testing

### Tools Used
- Chrome + SAML-Tracer plugin
- Shibboleth logs: `/opt/shibboleth-idp/logs/`
- Apache logs

### Steps
1. Access `https://sp.richtechuniversity.org/secure`
2. Redirect to IdP login
3. Enter LDAP credentials → trigger Duo MFA
4. On success, redirected to protected content
5. Use browser dev tools or logs to inspect SAML assertions

---

## 🛠️ Sample Commands

**Import LDIF:**
```bash
ldapadd -x -D "cn=admin,dc=example,dc=org" -W -f users.ldif


- **Networking:**  
  All VMs are bridged on the same virtual network segment and communicate securely over HTTPS using self-signed SSL certificates.




## 📚 Official Documentation

- [Shibboleth IdP](https://shibboleth.atlassian.net/wiki/spaces/IDP5/)
- [Shibboleth SP](https://shibboleth.atlassian.net/wiki/spaces/SP3/)
- [OpenLDAP](https://www.openldap.org/doc/)
- [Grouper Access Management](https://spaces.at.internet2.edu/display/Grouper/)
- [Duo MFA for Shibboleth](https://duo.com/docs/shibboleth)
- [VMware Workstation](https://www.vmware.com/products/workstation-pro.html)


© 2025 Richie — Built to showcase real-world IAM skills.
