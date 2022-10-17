from instagrapi.types import Usertag , Location
from instagrapi import Client
import config
import time
import random


cl = Client()
cl.login(config.username, config.password)


class MakePost:
    def __init__(self, client):
        self.cl = client
        self.tags = ['arduino', 'python', 'programing']
        self.used_pictures = []

    def get_current_time(self):
        t = time.localtime()
        current_time = time.strftime ("%H:%M:%S", t)
        print(current_time)
        return current_time

    def random_choice_picture(self):
        path_list = ['D:\\python\\Instagram-Bot\\media\\1.jfif',
                     'D:\\python\\Instagram-Bot\\media\\2.jfif',
                     'D:\\python\\Instagram-Bot\\media\\3.jfif',
                     'D:\\python\\Instagram-Bot\\media\\4.jfif']
        
        
        pic = random.choice(path_list)
        if len(self.used_pictures) == len(path_list):
            exit()
        elif pic in self.used_pictures:
            return self.random_choice_picture()
        else:
            self.used_pictures.append(pic)
            return pic


    
    def make_post(self, picture):
        user = cl.user_info_by_username("daniel45456")
        
        tags_list = ['#cat', '#cats', '#art', '#photo', 'picture']
        media = cl.photo_upload(
            path = picture,
            caption = f"Cloth picture {random.sample(tags_list, 3)}",
            # usertags = [ Usertag ( user = user , x = 0.5 , y = 0.5 ) ] ,
            # location = Location ( name = "Spain, Madrid", lat = 40.415390 , lng = -3.684243),
            extra_data = {
                "custom_accessibility_caption": "alt text example",
                "like_and_view_counts_disabled": False,
                "disable_comments": False,
            }
        )
    
    def wait_for_time(self):
        while True:
            current_time = self.get_current_time()
            time_list = ['10:27:30', '10:28:30', '10:29:30', '10:30:30', '10:31:30']
            if current_time in time_list:
                pic = self.random_choice_picture()
                self.make_post(pic)
                continue
            else:
                pass


start = MakePost(cl)
start.wait_for_time()
