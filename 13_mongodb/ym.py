# mongodb+srv://python_master:<db_password>@clusteru.g2t9j.mongodb.net/?appName=ClusterU

from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://python_master:python_master@clusteru.g2t9j.mongodb.net/?appName=ClusterU',tlsAllowInvalidCertificates=True)
db = client['ym']
video_collection = db['videos']


def list_videos():
  
  videos = video_collection.find()
  for video in videos:
    print(f"ID: {video['_id']}, Name: {video['name']}, Duration: {video['duration']}")
    

def add_video():
  name = input("Enter video name: ")
  duration = input("Enter video duration: ")
  response = video_collection.insert_one({'name':name, 'duration':duration})
  print("Added")
  

def update_video():
  vid_id = ObjectId(input("Enter video id: "))
  new_name = input("Enter new name: ")
  new_duration = input("Enter new duration: ")
  res = video_collection.update_one({'_id':vid_id},{"$set":{'name':new_name,'duration':new_duration}})
  print("Updated ")
  

def delete_video():
  vid_id = ObjectId(input("Enter video id: "))
  video_collection.delete_one({'_id':vid_id})
  

def main():

  while True:
    
    print('\nYoutube manager | MongoDB')
    print("1. List videos")
    print("2. Add video")
    print("3. Update video")
    print("4. Delete video")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
      case '1':
        list_videos()
        
      case '2':
        add_video()
        
      case '3':
        update_video()
        
      case '4':
        delete_video()
        
      case '5':
        break
      
      case _:
        print('Invalid input')
        
  
  
  
if __name__=="__main__":
  main()