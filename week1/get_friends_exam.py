import requests
import datetime
domain = "https://api.vk.com/method/users.get"
domain_get_friends = "https://api.vk.com/method/friends.get"
access_token = "677c015d677c015d677c015df5670f7a7f6677c677c015d384be64706402d970cffcdb2"
v = 5.122
fields = "bdate"
def get_friends(user_id):
    
        
        friends_dict = {}
        params = {
            'domain_get_friends': domain_get_friends,
            'access_token': access_token,
            'v': v,
            'user_id': user_id,
            'fields': fields
        }
        query = f"{domain_get_friends}?access_token={access_token}&v={v}&user_id={user_id}&fields={fields}".format(**params)
        data = requests.get(query).json()
        redata = data["response"]["items"]
        
        for elem in redata:
            if "bdate" in elem and len(elem["bdate"].split('.')) == 3:
                day, month, birth_date = elem["bdate"].split(".", 2)
                friends_dict[elem["id"]] = birth_date
            
                
        return friends_dict
    
        
            

def calc_age(user_id):
    user_id = get_friends(user_id)
    year = datetime.datetime.today().year
    calc_age = {}
    for elem in user_id.values():
        b_date = year - int(elem)
        if b_date not in calc_age:
            calc_age[b_date] = 0

        calc_age[b_date] += 1
        
    calc_list = list(calc_age.items())
    calc_list.sort(key = lambda x : (x[1], -x[0]))


    return calc_list
        

print(calc_age("320661281"))
