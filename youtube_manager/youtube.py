import json

def list_all_videos(videos):
  print('\n')
  print(50*'*')
  print(60*'*')
  for index, video in enumerate(videos,start=1):
    print(f"{index}. {video['name']}, Duration: {video['time']}")
  print('\n')
  print(60*'*')
  print(50*'*')


def add_videos(videos):
  name=input("Enter video name: ")
  time=input('Enter video duration: ')
  videos.append({"name":name,"time":time})
  save_data(videos)


def delete_video(videos):
  list_all_videos(videos)
  index=int(input("Enter video index to delete: "))
  if 1<=index<=len(videos):
    del videos[index-1]
  else:
    print("Enter valid index!")


def update_video(videos):
  list_all_videos(videos)
  index=int(input("Enter video index to update: "))
  if 1<=index<=len(videos):
    new_name=input("Enter new name: ")
    new_duration=input("Enter new duration: ")
    videos[index-1]={"name":new_name,"time":new_duration}
    save_data(videos)
  else:
    print("Enter valid index !")


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

  videos=load_data()
  while True:
    # options
    print("\n Youtube Manager| Choose an option ")
    print("1. List all youtube videos")
    print("2. Add youtube videos")
    print("3. Delete a youtube video")
    print("4. Update a youtube video details")
    print("5. Exit")

    choice=int(input("Enter your choice:"))
    # print(videos)
    match choice:
      case 1:
        list_all_videos(videos)
      case 2:
        add_videos(videos)
      case 3:
        delete_video(videos)
      case 4:
        update_video(videos)
      case 5:
        break
      case _:
        print("Invalid choice")


if __name__=='__main__':
  main()

