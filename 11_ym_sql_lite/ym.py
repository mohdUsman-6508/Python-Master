import sqlite3

conn = sqlite3.Connection('youtube.db')
cursor = conn.cursor()
cursor.execute('Create table if not exists youtube (id Integer primary key, name var not null, time var not null)')

def list_videos():
  cursor.execute('Select * from youtube')
  videos = cursor.fetchall()
  if len(videos) == 0:
    print("No videos in the list")

  for video in videos:
    print(video)


def add_video(name, time):
  cursor.execute('insert into youtube (name, time) values (?,?)',(name,time))
  conn.commit()
  print("Added")
  

def update_video(id,name,time):
  cursor.execute("update youtube set name= ?, time= ? where id =? ",(name,time,id))
  conn.commit()
  print("Updated")


def delete_video(id):
    cursor.execute("Delete from youtube where id=?",(id,))
    conn.commit()
    print("Deleted")



def main():
  
  while True:
    
    print("Youtube Manager SQLite3 | Choose an option")
    
    print("1. List videos")
    print("2. Add video")
    print("3. Update video")
    print("4. Delete video")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
      list_videos()
      
    elif choice == 2:
      name = input("Enter name: ")
      time = input("Enter time: ")
      add_video(name,time)
      
    elif choice == 3:
      vid_id = int(input("Enter id: "))
      new_name = input("Enter name: ")
      new_time = input("Enter time: ")
      update_video(vid_id,new_name,new_time)
      
    elif choice ==4:
      vid_id = int(input("Enter id: "))
      delete_video(vid_id)
      
    elif choice == 5:
      break
    else:
      print('Invalid choice')
      
  conn.close()
  


if __name__=="__main__":
  main()