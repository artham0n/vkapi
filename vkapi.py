import requests
import random

class vkapi:

    token = 'd55303083d3cc1b96fcfcdedcc6ea20ed815ce6753d66f87f1f7013d43047f093d09867952a4e6bb3db99'
    v = '5.81'
    group_id = '181643545'

    def __init__(self, token, v, group_id):
        self.token = token
        self.v = v
        self.group_id = group_id

    def getUserInforamtion(self, peer_id):
        return self.req(self.token, 'users.get', {'user_ids': peer_id, 'fields': 'photo_max'})

    def sendMessage(self, peer_id, message):
        self.req(self.token, 'messages.send', {
            'user_id': peer_id,
            'message': message,
            'random_id': random.randint(0, 99999)
        })
        return True

    def req(self, token, method, params):
        url = 'https://api.vk.com/method/' + method
        params['v'] = self.v
        params['access_token'] = token

        r = requests.post(url, params)
        resp = r.json()
        if r.json()['response']:
            return r.json()['response']
        else:
            return resp