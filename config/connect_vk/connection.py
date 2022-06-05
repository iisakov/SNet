import requests as r

access_token = ''
method_url = f'https://api.vk.com/method/groups.getMembers?v=5.131&group_id=by_artisan&access_token={access_token}'
connect = r.get(url=method_url)
