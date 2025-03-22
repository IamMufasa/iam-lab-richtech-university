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

![IAM Architecture Diagram](docs/iam_architecture_diagram.png)

## Deployment
See architecture and Ansible playbooks for step-by-step instructions.
