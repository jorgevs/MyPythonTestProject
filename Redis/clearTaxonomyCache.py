import redis

r = redis.Redis(host='WEB-REDISPROD02.forrester.com', port=6379, db=0)
#r = redis.Redis(host='WEB-REDISSTG02.forrester.com', port=6379, db=0)

#res = r.keys("taxonomy:RES*")
#res = r.keys("taxonomy:RES44422")

#res = r.keys("Permissions-*")
#res = r.keys("Permissions-2988862")
res = r.keys("Permissions-3139130")
#res = r.keys("Permissions-3295961")


#{forrservice_content}SERVICE_LISTING*
#{forrservice_content}SERVICE_PAGE*


#res = r.keys("{User_Profile_By_Email}*")
#res = r.keys("{User_Profile_By_Email}jvazquez@forrester.com")

#res = r.keys("{COLLECTION_USER_FAVORITES_TOPICS}*")
#res = r.keys("{COLLECTION_USER_FAVORITES_TOPICS}lsprague@forrester.com")

# {Contact_Access_Groups_Staging}3436858*
# {Access_Group_Contacts_Staging}

#res = r.keys("tag*")

for key in res:
    #print(key)
    # Decode byte to string
    print(key.decode("utf-8"))

    vals = None
    type = r.type(key)
    print("type:" + str(type))
    if type == b'string':
        vals = r.get(key)
    if type == b'hash':
        vals = r.hgetall(key)
    if type == b'zset':
        vals = r.zrange(key, 0, -1)
    if type == b'list':
        vals = r.lrange(key, 0, -1)
    if type == b'set':
        vals = r.smembers(key)
    print(vals)

    r.delete(key.decode("utf-8"))


