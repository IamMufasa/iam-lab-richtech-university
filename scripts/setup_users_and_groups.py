import ldap
from ldap.modlist import addModlist

LDAP_SERVER = "ldap://localhost"
BIND_DN = "cn=admin,dc=richtest,dc=org"
PASSWORD = "adminpass"
BASE_PEOPLE_DN = "ou=People,dc=richtest,dc=org"
BASE_GROUP_DN = "ou=Groups,dc=richtest,dc=org"

conn = ldap.initialize(LDAP_SERVER)
conn.simple_bind_s(BIND_DN, PASSWORD)

# Users
users = [{"uid": "fhfpkl", "cn": "QDmDiBgN", "sn": "pXuXz"}, {"uid": "awrksk", "cn": "kcpAiHlp", "sn": "SFmhg"}, {"uid": "qawvzr", "cn": "DlWaRumi", "sn": "OJPOq"}, {"uid": "qutyzd", "cn": "wvhbQytQ", "sn": "jcYtr"}, {"uid": "rbxplf", "cn": "cCdeixjX", "sn": "FxLBf"}, {"uid": "wxvudk", "cn": "kwPQXUBp", "sn": "oGCvF"}, {"uid": "gleoqj", "cn": "PgCYFINA", "sn": "ZJyOn"}, {"uid": "tqcbbe", "cn": "MzbtLKja", "sn": "DMSek"}, {"uid": "rspfmz", "cn": "UzCereSb", "sn": "HTXMe"}, {"uid": "pwnbpq", "cn": "xGjSYaTy", "sn": "iykLD"}, {"uid": "ttsqjp", "cn": "vHZIgIkw", "sn": "yEPqS"}, {"uid": "qfmyke", "cn": "CWPkTlFo", "sn": "gDgbb"}, {"uid": "jjdbds", "cn": "BtkVtwOz", "sn": "VwVwb"}, {"uid": "dmryek", "cn": "mjJflJvX", "sn": "EvExB"}, {"uid": "akoxoj", "cn": "slZnDkol", "sn": "VyxxG"}]

for user in users:
    dn = f"uid={user['uid']},{BASE_PEOPLE_DN}"
    attrs = {
        'objectClass': [b'inetOrgPerson'],
        'uid': [user['uid'].encode()],
        'sn': [user['sn'].encode()],
        'cn': [user['cn'].encode()],
        'userPassword': [b'password123']
    }
    ldif = addModlist(attrs)
    conn.add_s(dn, ldif)

print("15 Users created.")

# Groups
groups = {
    "developers": ["fhfpkl", "awrksk", "qawvzr", "qutyzd", "rbxplf"],
    "research_team": ["wxvudk", "gleoqj", "tqcbbe", "rspfmz", "pwnbpq"],
    "iam_admins": ["ttsqjp", "qfmyke", "jjdbds", "dmryek", "akoxoj"]
}

for group_name, member_uids in groups.items():
    dn = f"cn={group_name},{BASE_GROUP_DN}"
    members = [f"uid={uid},{BASE_PEOPLE_DN}".encode() for uid in member_uids]
    attrs = {
        'objectClass': [b'groupOfNames'],
        'cn': [group_name.encode()],
        'member': members
    }
    ldif = addModlist(attrs)
    conn.add_s(dn, ldif)

print("Groups created and users assigned.")
