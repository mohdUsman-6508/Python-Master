import json


def load_data():
    try:
        with open('file_db.txt','r') as file:
            data = json.load(file)
            print("File Loaded Successfully")
            return data
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('file_db.txt','w') as file:
        json.dump(videos,file)
    

def list_videos(videos):
    print("\n")
    print("*"*50)
    for index, video in enumerate(videos):
        print(f"{index+1}. {video['title']}, Duration: {video['length']}")
    print("\n")
    print("*"*50)
    

def add_video(videos):
    title = input("Enter video title: ")
    length = input("Enter length in mins: ")
    video = {'title':title, 'length':length}
    videos.append(video)
    save_data_helper(videos)
    print("Video saved successfully.")
    

def update_video(videos):
    list_videos(videos)
    index = int(input("Enter the video number to update: "))
    
    if 1<=index<=len(videos):
        name = input("Enter the new video name: ")
        length = input("Enter the new video length: ")
        videos[index-1] = {'title':name,'length':length}
        save_data_helper(videos)
        print("Video updated successfully.")
    else:
        print("Invalid Index")
        

def delete_video(videos):
    list_videos(videos)
    index = int(input("Enter the video number to delete: "))
    
    if 1<=index<=len(videos):
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully.")
        
    else:
        print("Invalid index selected")
    

def main():
    while True:
        videos = load_data()
        
        print("\nYoutube Manager | Choose an option")
        print("1. List all the videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                list_videos(videos)
                
            case "2":
                add_video(videos)
            
            case "3":
                update_video(videos)
            
            case "4":
                delete_video(videos)
                
            case "5":
                print("_+_+_+_+_+_+_+_+_+_+_+_+ Exited Successfully _+_+_+_+_+_+_+_+_+_+_+_+")
                break
            
            case _:
                print("Invalid choice")
            
                
            
if  __name__ == '__main__':
    main()
            
            
    
    