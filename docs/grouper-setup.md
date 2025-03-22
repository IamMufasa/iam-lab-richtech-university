# Grouper Setup Walkthrough for RichTech University IAM Lab

This guide explains how to configure and use Grouper to manage group-based access control (RBAC) within the RichTech University IAM lab.

---

## 1. **Overview**

Grouper is an access management tool that helps you define roles and group memberships to enforce access control policies across your identity infrastructure. In this lab, Grouper works alongside OpenLDAP, Shibboleth, and Duo to simulate a higher-ed IAM environment.

---

## 2. **System Requirements**

- Java JDK 11+
- Tomcat 9 or newer
- MariaDB (or PostgreSQL/Oracle)
- Grouper Installer (from Internet2)
- Configured LDAP directory and users

---

## 3. **Download & Install Grouper**

```bash
wget https://spaces.internet2.edu/download/attachments/14517824/grouperInstaller.jar
java -jar grouperInstaller.jar
```

Follow the prompts to install:
- API
- UI
- Daemon
- Web Services

---

## 4. **Configure Grouper Database**

Ensure your MariaDB instance is ready:

```sql
CREATE DATABASE grouper;
CREATE USER 'grouperuser'@'localhost' IDENTIFIED BY 'grouperpass';
GRANT ALL PRIVILEGES ON grouper.* TO 'grouperuser'@'localhost';
```

Set your connection in `grouper.hibernate.properties`:

```properties
hibernate.connection.url = jdbc:mysql://localhost:3306/grouper
hibernate.connection.username = grouperuser
hibernate.connection.password = grouperpass
```

---

## 5. **Connect to LDAP (optional sync)**

In `subject.properties`, configure OpenLDAP connection:

```properties
subject.sources = source1

subject.source.source1.id = ldap
subject.source.source1.name = LDAP Source
subject.source.source1.type = edu.internet2.middleware.grouper.subj.GrouperJndiSourceAdapter
subject.source.source1.param.ldap.url = ldap://localhost
subject.source.source1.param.ldap.user = cn=admin,dc=richtest,dc=org
subject.source.source1.param.ldap.pass = adminpass
subject.source.source1.param.ldap.base = ou=People,dc=richtest,dc=org
```

---

## 6. **Start Services**

```bash
cd grouper.ui/target/grouper
./bin/start.sh
```

Then open in browser:  
**http://localhost:8080/grouper**

Default credentials: `GrouperSystem` / `********`

---

## 7. **Create Folders and Groups**

Inside the Grouper UI:

- Create a folder `richtest:iam`
- Inside the folder, create groups:
  - `richtest:iam:developers`
  - `richtest:iam:research_team`
  - `richtest:iam:iam_admins`

Assign LDAP users to these groups by adding subjects from LDAP.

---

## 8. **Provisioning to LDAP (optional)**

You can configure Grouper's PSPNG (provisioning plugin) to sync these groups back to LDAP automatically.

---

## 9. **Integrate with Shibboleth**

Shibboleth can consume Grouper group memberships via attributes released in SAML assertions. For example:

```xml
<Attribute name="eduPersonEntitlement" ...>
  <AttributeValue>richtest:iam:developers</AttributeValue>
</Attribute>
```

This allows access control to apps based on group membership managed by Grouper.

---

## 10. **Next Steps**

- Automate group creation with Grouper Shell (GSH)
- Add external apps protected by Shibboleth SP
- Map Grouper roles to specific entitlements or services

---

