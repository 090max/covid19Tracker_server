import requests
from bs4 import BeautifulSoup
from db_helper import db_connection
from datetime import date
import re



class Scrapper():
    def __init__(self):
        self.url="https://www.mohfw.gov.in/"
        self.page=requests.get(self.url)
        self.soup=BeautifulSoup(self.page.content,"html.parser")
        self.db=db_connection()

    def update_general_collection(self,data):
            today = date.today()
            print("Today's date ",today)
            db=self.db.get_collection("general")
            returned_data=db.find({"date":str(today)},{"_id":0})
            empty_ret_data=True
            for _ in returned_data:
                empty_ret_data=False
                break

            if(empty_ret_data==False):
                db.update_one({"date":str(today)},{"$set":{"active_case":data["active_case"],"discharged_case":data["discharged_case"],"migrated_case":data["migrated_case"],"death_case":data["death_case"]}})
            else:
                print("New day today updating database accordingly !!")
                db.insert_one(data)

    def update_state_collection(self,data):
        db = self.db.get_collection("state_wise")
        for item in data:
            db.update_one({"state":item["state"]},{"$set":{"confirmed":item["confirmed"],"foreign":item["foreign"],"cured/migrated":item["cured/migrated"],"death":item["death"]}})

    def general_info(self):
        today = date.today()

        content_div=self.soup.find('div',{'class':"information_row"})
        info_dict={
        "date":str(today),
        "active_case":0,
        "discharged_case":0,
        "migrated_case":0,
        "death_case":0
        }
        active_case_div=content_div.find_all('div',{"class":"iblock"})[1].find("div",{"class":"iblock_text"})
        active_cases=active_case_div.find("span").text.strip()
        info_dict["active_case"]=int(active_cases)

        discharged_case_div=content_div.find_all('div',{"class":"iblock"})[2].find("div",{"class":"iblock_text"})
        discharged_cases=discharged_case_div.find("span").text.strip()
        info_dict["discharged_case"]=int(discharged_cases)

        migrated_case_div = content_div.find_all('div',{"class":"iblock"})[4].find("div",{"class":"iblock_text"})
        migrated_cases = migrated_case_div.find("span").text.strip()
        info_dict["migrated_case"] = int(migrated_cases)

        death_case_div = content_div.find_all('div',{"class":"iblock"})[3].find("div",{"class":"iblock_text"})
        death_cases = death_case_div.find("span").text.strip()
        death_cases_no=re.findall('\d+', death_cases)
        if(len(death_cases_no)>0):
            info_dict["death_case"] = int(death_cases_no[0])

        # print(info_dict)
        self.update_general_collection(info_dict)


    def state_wise_details(self):
        content_div=self.soup.find('div',{'class':'content newtab'})
        table=content_div.find("tbody")

        rows=table.find_all("tr")
        info_arr=[]
        for row in rows:
            columns=row.find_all("td")
            temp_dict={}
            if(len(columns)==6):
                temp_dict["state"]=columns[1].text.strip().replace(" ","").lower()
                temp_dict["confirmed"]=int(columns[2].text.strip())
                temp_dict["foreign"] = int(columns[3].text.strip())
                temp_dict["cured/migrated"]=int(columns[4].text.strip())
                # temp_dict["death"] = int(columns[5].text.strip())
                death_cases_no = re.findall('\d+',columns[5].text.strip())
                if (len(death_cases_no) > 0):
                    temp_dict["death"] = int(death_cases_no[0])
                info_arr.append(temp_dict)

        # print(info_arr)
        self.update_state_collection(info_arr)






