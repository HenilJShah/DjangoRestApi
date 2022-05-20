import json
import requests


class StudentData():
    def __init__(self) -> None:
        self.URL = "http://127.0.0.1:8000/crud/db/"

    def StudentCreate(self, name, roll, city):
        data = {
            'name': name,
            'roll': roll,
            'city': city
        }
        json_data = json.dumps(data)
        print(json_data)
        req = requests.post(url=self.URL, data=json_data)
        return req.json()


    def studentDatafetch(self, id = None):
        iddata = dict()
        if id is not None:
            iddata = {'id':id}
        json_data = json.dumps(iddata)
        final = requests.get(url=self.URL, data=json_data)
        print(f"fetch data:=>{final.json()}")
        return final.json()

if __name__ == "__main__":
    clobj = StudentData()
    choic = 1
    while choic != 0:
        
        print("""\n
        1. fetch data 
        2. create data
        0. exit
        """)

        choic = int(input("\nenter number:"))
        if choic == 1:
            fetch_id_number = int(input("enter student id:"))
            clobj.studentDatafetch(fetch_id_number)
        if choic == 2:
            name = input("enter name:")
            roll = input("enter Roll no:")
            city = input("enter city:")
            clobj.StudentCreate(name, roll, city)