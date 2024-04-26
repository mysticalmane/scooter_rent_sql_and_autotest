import requests
import configuration
import data

# creating new oder
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_order(data.order_body)

# saving track number of created order
tracknumber = str(response.json()["track"])

# getting order by using its track number
def get_order_by_tracknumber():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH + tracknumber,
                         headers=data.headers)