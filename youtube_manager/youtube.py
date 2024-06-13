import json


def list_all_videos():
  pass

def add_videos():
  pass

def delete_video():
  pass

def update_video():
  pass

def load_data():
  try:
    with open('youtube_data.txt','r') as file:
      return json.load(file)  
  except FileNotFoundError: 
    return []
  # finally:
  #   print()


def save_data(videos):
  with open('youtube_data.txt','w') as file:
         json.dump(videos,file)


  


def main():

  videos=load_videos()
  video=videos[0]

  while True:
    # options
    print("\n Youtube Manager| Choose an option ")
    print("1. List all youtube videos")
    print("2. Add youtube videos")
    print("3. Delete a youtube video")
    print("4. Update a youtube video details")
    print("5. Exit")

    choice=int(input("Enter your choice:"))

    match choice:
      case 1:
        list_all_videos(videos)
      case 2:
        add_videos(videos)
      case 3:
        delete_video(video)
      case 4:
        update_video(video)
      case 5:
        break
      case _:
        print("Invalid choice")


if __name__=='__main__':
  main()



  