import ldap
from ldap.modlist import addModlist

LDAP_SERVER = "ldap://localhost"
BIND_DN = "cn=admin,dc=example,dc=org"
PASSWORD = "adminpass"
BASE_DN = "ou=People,dc=example,dc=org"

conn = ldap.initialize(LDAP_SERVER)
conn.simple_bind_s(BIND_DN, PASSWORD)

users = [
    {"uid": "jdoe", "cn": "John Doe", "sn": "Doe"},
    {"uid": "asmith", "cn": "Alice Smith", "sn": "Smith"},
]

for user in users:
    dn = f"uid={user['uid']},{BASE_DN}"
    attrs = {
        'objectClass': [b'inetOrgPerson'],
        'uid': [user['uid'].encode()],
        'sn': [user['sn'].encode()],
        'cn': [user['cn'].encode()],
        'userPassword': [b'password123']
    }

    ldif = addModlist(attrs)
    conn.add_s(dn, ldif)

print("LDAP users added successfully.")
