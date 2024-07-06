from pymongo import MongoClient
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()
database_url=os.getenv('MONGODB_URI')

client=MongoClient(database_url)
db=client['youtubemanager']
video_collection=db["videos"]


def add_video(name,time):
  video_id=video_collection.insert_one({"name":name,"time":time}).inserted_id
  
def list_videos():
  for video in video_collection.find():
    print(f"ID: {video['_id']},Name:{video['name']},Time:{video['time']}")

def delete_video(id):
  video_collection.delete_one({"_id":ObjectId(id)})

def update_video(id,name,time):
  video_collection.update_one({'_id':ObjectId(id)},
                              {"$set":{
                                "name":name,
                                "time":time
                              }})


def main():
  while True:
    print("\n Youtube manager App")
    print("1. List all videos")
    print("2. Add a new video")
    print("3. Update a video")
    print("4. Delete a video")
    print("5. Exit the app")

    choice=input("Enter your choice: ")

    if choice=='1':
      list_videos()
    elif choice=='2':
      name=input("Enter the video name: ")
      time=input("Enter the video time: ")
      add_video(name,time)
    elif choice=='3':
      video_id=input("Enter the video id to update :")
      name=input("Enter the updated video name: ")
      time=input("Enter the updated video time: ")
      update_video(video_id,name,time)
    elif choice=='4':
      video_id=input("Enter video id to delete: ")
      delete_video(video_id)
    elif choice=='5':
      break


if __name__=="__main__":
  main()