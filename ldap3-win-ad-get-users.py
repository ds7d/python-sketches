import ldap3

from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups as addUsersInGroups
server = ldap3.Server('adserv.example.com', port=389, use_ssl=False)
conn = ldap3.Connection(server, 'CN=svc_python_zabbix,OU=Пользователи,OU=Фирма,DC=example,DC=com', 'Pass8##',auto_bind=True)
conn.search('OU=Пользователи,OU=Фирма,DC=example,DC=com', '(objectclass=person)', attributes=['sAMAccountName'])
domain_users = conn.entries
domain_users_out_list = []
for elem in domain_users:
    tmp_dict = elem.__dict__
    tmp_dict = tmp_dict['_state'].__dict__
    if not 'OU=Администрирование,OU=Пользователи,OU=Фирма,DC=example,DC=com' in tmp_dict['dn']:
        username = elem['sAMAccountName'].__dict__
        username = username['values'][0]
        domain_users_out_list.append(username)
      
print(domain_users_out_list)
