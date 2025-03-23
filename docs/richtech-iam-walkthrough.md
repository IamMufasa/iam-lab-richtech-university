# RichTech University IAM Lab – Full Walkthrough

This project simulates an enterprise-level Identity & Access Management (IAM) environment for a fictional university (RichTech University), using open-source tools to demonstrate federated authentication, role-based access control (RBAC), directory integration, and MFA enforcement.

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

| VM  | OS                   | Purpose                                |
|-----|----------------------|----------------------------------------|
| VM1 | Ubuntu Server 22.04  | Shibboleth IdP + Duo MFA plugin        |
| VM2 | Ubuntu Server 22.04  | Shibboleth SP (Apache HTTPD)           |
| VM3 | Ubuntu Server 22.04  | OpenLDAP Directory                     |
| VM4 | Ubuntu Server 22.04  | Grouper UI + MariaDB backend           |

---

## 🌐 Networking

All VMs are bridged on the same virtual network segment and communicate securely over HTTPS using self-signed SSL certificates.

---

## 🔧 Setup Instructions

### 1. Shibboleth IdP

```bash
sudo apt update
sudo apt install openjdk-11-jdk unzip
wget https://shibboleth.net/downloads/identity-provider/latest/shibboleth-identity-provider-4.x.x.tar.gz
```

- Edit `idp.properties` and `relying-party.xml`
- Set `entityID`: `https://idp.richtechuniversity.org/idp/shibboleth`
- Add Duo MFA plugin to login flow
- Import SP metadata

---

### 2. Shibboleth SP

```bash
sudo apt install apache2 libapache2-mod-shib2
```

- Protect `/secure` path with Shibboleth config
- Import IdP metadata
- Configure virtual host with self-signed SSL

---

### 3. OpenLDAP

```bash
sudo apt install slapd ldap-utils
sudo dpkg-reconfigure slapd
```

- Base DN: `dc=richtechuniversity,dc=org`
- Import LDIF entries:
```bash
ldapadd -x -D "cn=admin,dc=richtechuniversity,dc=org" -W -f docs/users.ldif
```

---

### 4. Grouper

- Download and install Grouper using official installer
- Connect to LDAP and MariaDB
- Create groups: `students`, `faculty`, `it-admins`
- Assign users to groups via Grouper UI

---

## 🔐 Attribute Mapping (IdP)

| Attribute ID            | OID                                         | Description               |
|-------------------------|----------------------------------------------|---------------------------|
| `mail`                  | `urn:oid:0.9.2342.19200300.100.1.3`          | Email address             |
| `givenName`             | `urn:oid:2.5.4.42`                           | First name                |
| `sn`                    | `urn:oid:2.5.4.4`                            | Last name                 |
| `eduPersonAffiliation`  | `urn:oid:1.3.6.1.4.1.5923.1.1.1.1`           | Role (e.g., student)      |

---

## 🧪 Testing

### Tools

- Chrome with SAML-Tracer extension
- Shibboleth logs: `/opt/shibboleth-idp/logs/idp-process.log`
- Apache logs: `/var/log/apache2/access.log`

### Steps

1. Visit `https://sp.richtechuniversity.org/secure`
2. Redirects to IdP login
3. Authenticate via LDAP + Duo MFA
4. Successful SAML assertion returned
5. Inspect response with SAML-Tracer

---

## 🛠️ Useful Project Commands

```bash
# Restart Shibboleth IdP
sudo systemctl restart shibboleth-idp

# Tail Shibboleth IdP logs
tail -f /opt/shibboleth-idp/logs/idp-process.log

# Search for user in OpenLDAP
ldapsearch -x -LLL -b "dc=richtechuniversity,dc=org" "(uid=jdoe)" mail givenName sn
```

Access Grouper UI:
```
https://grouper.richtechuniversity.org/grouper/
```

---




## 📚 Official Documentation

- [Shibboleth IdP](https://shibboleth.atlassian.net/wiki/spaces/IDP5/)
- [Shibboleth SP](https://shibboleth.atlassian.net/wiki/spaces/SP3/)
- [OpenLDAP](https://www.openldap.org/doc/)
- [Grouper Access Management](https://spaces.at.internet2.edu/display/Grouper/)
- [Duo MFA for Shibboleth](https://duo.com/docs/shibboleth)
- [VMware Workstation](https://www.vmware.com/products/workstation-pro.html)

---

© 2025 Richie — Built to showcase real-world IAM skills.
