# Identity & Access Management Lab

This project simulates a higher-ed IAM infrastructure using Shibboleth, Grouper, Duo MFA, and OpenLDAP to demonstrate federated identity, role-based access control, and multi-factor authentication.

## Overview

The lab simulates an enterprise-style IAM environment that integrates:
- **Shibboleth IdP/SP** for SAML-based authentication
- **Grouper** for access control (RBAC)
- **Duo MFA** for multi-factor authentication
- **OpenLDAP** as the identity source
- **MariaDB** to store Grouper and LDAP metadata
- **Ansible** for automation
- **Apache HTTPD** to serve web content

## Features
- Federated login via Shibboleth
- MFA with Duo
- Access control using Grouper groups
- LDAP-based user authentication
- Infrastructure as Code with Ansible

---

## 🖥️ Virtual Environment

The project was built using **VMware Workstation** with 3–4 Ubuntu Server 22.04 VMs simulating an enterprise IAM environment.  
Each VM hosts a specific IAM component (IdP, SP, LDAP, and Grouper) and all services are bridged on a virtual network.



## Project Structure
```bash
iam-lab-shibboleth-grouper-duo/
├── ansible/
├── configs/
│   ├── apache/
│   ├── grouper/
│   ├── ldap/
│   └── shibboleth/
├── docs/
├── scripts/
└── README.md
```

## Architecture Diagram

![RichTech IAM Architecture](docs/richtech-iam-architecture.drawio.svg)

*Figure: RichTech University IAM flow showing user authentication via Shibboleth, Duo MFA, LDAP, and role-based access with Grouper.*

➡️ Full walkthrough → [docs/richtech-iam-walkthrough.md](docs/richtech-iam-walkthrough.md)


## Deployment
See architecture and Ansible playbooks for step-by-step instructions.
