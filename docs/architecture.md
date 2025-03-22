# IAM Home Lab Architecture

This document outlines the architecture and workflow of the IAM (Identity & Access Management) Home Lab environment.

## Architecture Diagram

```text
[ User ] --> [ Apache + Shibboleth SP ] --> [ Shibboleth IdP ] --> [ LDAP + Grouper + Duo ]
```

1. User accesses protected resource.
2. Redirect to IdP for SAML login.
3. LDAP + Duo MFA used for authentication.
4. Grouper checks access control group membership.
5. Access granted or denied based on role.
