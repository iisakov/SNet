import requests as r

access_token = '0cd7052fdfb8771d1c95661102846c07a31506409157a2c384fabedf2018e578daf9efde0b8681f51acc6'
method_url = f'https://api.vk.com/method/groups.getMembers?v=5.131&group_id=by_artisan&access_token={access_token}'
connect = r.get(url=method_url)
