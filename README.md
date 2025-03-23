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


---

## 🛠️ Skills Acquired

- Implementing federated SAML SSO using Shibboleth SP and IdP
- Configuring LDAP directory services and importing users via LDIF
- Integrating Duo MFA into Shibboleth IdP login flows
- Using Grouper for role-based access and LDAP group synchronization
- Managing metadata and trust relationships in SAML federation
- Troubleshooting identity and access flows using logs and SAML tools
- Building a full IAM architecture in a simulated `.edu` environment

---

## 📘 Lessons Learned

- Federated authentication with SAML requires precise configuration between IdP and SP for metadata, endpoints, and certificates.
- Duo MFA integration with Shibboleth IdP provides strong layered security but requires custom flow configuration.
- OpenLDAP is highly flexible but must be carefully structured for use with identity federation.
- Grouper enables scalable group-based RBAC, making it ideal for educational institutions.
- Testing SAML assertions with tools like SAML-Tracer or browser dev tools is essential to troubleshoot login issues.

---

## 💡 Recommendations

- Use isolated environments with real domains (e.g., `.edu`) and realistic naming to simulate enterprise IAM setups.
- Always version control Shibboleth IdP config files, metadata, and attribute filters.
- Start with simple attribute release policies and gradually refine them as needed.
- Use meaningful group names and organize Grouper hierarchies early to prevent confusion as access needs grow.
- Consider adding integration with SIEM tools in the future to log SAML assertions and track authentication events.


---

## 🏷️ Tags

`IAM` `SSO` `Shibboleth` `LDAP` `OpenLDAP` `Grouper` `Duo` `SAML` `RBAC` `Cybersecurity` `HigherEd` `Federation`
---
© 2025 Richie — Part of a cybersecurity and IAM portfolio built for real-world readiness.
