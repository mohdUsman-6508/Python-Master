import requests


def fetch_all_post():
    
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.get(url)
    data = response.json()
    
    if data:
        return data
    else:
        raise Exception("No data found")
    

def create_post(title,body,user_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    
    post = {'title':title, 'body':body, 'userId':user_id}
    response = requests.post(url,post)
    print(response.json())
    
    
def update_post(id,title,body,user_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'
    
    post = {'title':title, 'body':body, 'userId':user_id}
    response = requests.put(url,post)
    print(response.json())
    
def patch_post(title):
	url = f'https://jsonplaceholder.typicode.com/posts/{id}'
	post = {'title':title}
	response = requests.patch(url,post)
	print(response.json())
 
    
def delete_post(id):
	url = f'https://jsonplaceholder.typicode.com/posts/{id}'
	response = requests.delete(url)
	print(response.json()) 


def main():
    
    try:
        data = fetch_all_post()
        print(data['userId'])
        print(data['title'])
    except:
        print("Unable to get the data")
        

    create_post("Alchemist", "This is the body of the Alchemist",1)
    update_post(1,"Alchemist", "the Alchemist",1)
    patch_post("The Alchemist")
    delete_post(1)
    
    
if __name__=="__main__":
    main()
    


# TODO:  REWRITE ABOVE REQUESTS (MAKE THEM PRODUCTION BASE)