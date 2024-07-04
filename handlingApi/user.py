import requests

def get_user():
    url="https://api.freeapi.app/api/v1/public/randomusers"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        user=data["data"]["data"][0]
        username=user["login"]["username"]
        country=user['location']['country']

        return username,country
    else:
        raise Exception("Failed to get user")


def main():
    username,country=get_user()
    print(f"Username:{username} Country:{country}")

if __name__=="__main__":
    main()
