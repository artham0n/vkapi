from vkapi import vkapi
import requests
import  httplib2

VK_KEY = 'd55303083d3cc1b96fcfcdedcc6ea20ed815ce6753d66f87f1f7013d43047f093d09867952a4e6bb3db99'
VK_VERSION = '5.81'
GROUP_ID = '181643545'

vkapi = vkapi(VK_KEY, VK_VERSION, GROUP_ID)

while True:
    response = vkapi.req(VK_KEY, 'groups.getLongPollServer', {'group_id': GROUP_ID})
    response = requests.get(response['server']+'?act=a_check&key='+response['key']+'&ts='+str(response['ts'])+'&wait=25')
    if (response.json()['updates']):
        response = response.json()['updates'][0]
        if (response['type'] == 'message_new'):
            response = response['object']

            peer_id = response['peer_id']
            message = response['text']
            userInfo = vkapi.getUserInforamtion(peer_id)

            h = httplib2.Http('.cache')
            response, content = h.request(userInfo[0]['photo_max'])
            out = open('.cache/' + str(peer_id) + '.jpg', 'wb')
            out.write(content)
            out.close()

            print(userInfo)
            userName = userInfo[0]['first_name']
            lastName = userInfo[0]['last_name']

            #vkapi.sendMessage(peer_id, 'Проверочка')
