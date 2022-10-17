# from fake-useragent import UserAgent
import asyncio
import requests
# from bs4 import BeautifulSoup
import json
from copy import copy
import time
import random
with open("everything_json.txt", "r") as file:
    count_json = file.read()
# from lxml import html
headers = {
    "user-agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.141 YaBrowser/22.3.4.731 Yowser/2.5 Safari/537.36"
}
# ua = UserAgent()
"""
urls = [
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.쏘렌토.))_.Year.range(201800..201911)._.Mileage.range(..120000).)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.싼타페.)))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/dc/dc_carsearchlist.do?carType=kor#!%7B%22action%22%3A%22(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.스포티지.)))%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D",
    r"http://www.encar.com/fc/fc_carsearchlist.do?carType=for&searchType=model&TG.R=B#!%7B%22action%22%3A%22(And.Hidden.N._.(C.CarType.N._.(C.Manufacturer.인피니티._.ModelGroup.QX50.))_.Year.range(201810..201909).)%22%2C%22toggle%22%3A%7B%7D%2C%22layer%22%3A%22%22%2C%22sort%22%3A%22ModifiedDate%22%2C%22page%22%3A1%2C%22limit%22%3A20%7D"
]
"""
# get_json_link2 = f"http://api.encar.com/search/car/list/premium?count=true&q=(And.(And.Hidden."
# get_json_link = r"http://api.encar.com/search/car/list/premium?count=true&q=(And.(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.스포티지.)))_.AdType.B.)&sr=%7CModifiedDate%7C0%7C20"


def pars_link(user_link, string_add, get_json_link2):
    try:
        # output_link = copy(get_json_link2)
        ans_str = ''
        list_url = list(user_link)
        list_url2 = copy(list_url)
        s = 0
        sm = list_url.index("N")
        end_list = list_url[sm:]
        ans = 0
        for value in end_list:
            if list_url2.count(")") <= 1:
                ans = list_url2.index(")")
                break
            elif value == ")":
                s += 1
                list_url2.remove(")")
        ans2 = ans + s
        answer = list_url[sm:ans2]
        for something in answer:
            ans_str += something
        ans_end = get_json_link2 + ans_str + string_add
        return ans_end
    except Exception as ex:
        print(ex)
        return "error"


# //*[@id="sr_photo"]/li[1]/a/span[2]/span[1]/strong
def collect_data(urls, all_links):
    output_text = []
    # print(urls)
    # get_page = requests.get(urls[2], headers=headers)
    # some_url = r"http://api.encar.com/search/car/list/premium?count=true&q=(And.(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.현대._.ModelGroup.싼타페.)))_.AdType.B.)&sr=%7CModifiedDate%7C0%7C94"
    # asdw = requests.get(some_url, headers=headers)
    # with open("test.json", "w") as sm_file:
    # json.dump(asdw.json(), sm_file, indent=4, ensure_ascii=False)
    useful_g = 0
    useful_p = 1
    old_list_json = []
    
    try:
        useful_p = 1
        begin_link = pars_link(
            urls, ")_.AdType.B.)&sr=%7CModifiedDate%7C0%7C20",
            "http://api.encar.com/search/car/list/premium?count=true&q=(And.(And.Hidden."
        )
        if begin_link == "error":
            return ["E"]
        sleep_time = random.randint(1, 3)
        time.sleep(sleep_time)
        try:
            get_json = requests.get(begin_link, headers=headers)
        except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
            return ["E"]
        # print(begin_link)
        all_iters = get_json.json()["Count"]
        """
        if int(all_iters) >= 7:
            begin_link = pars_link(link, ")&sr=%7CModifiedDate%7C0%7C20", "http://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.")
            get_json = requests.get(begin_link, headers=headers)
            print(begin_link)
            all_iters = get_json.json()["Count"]
        """
        need_link3 = list(begin_link)[:-2]
        need_link = ''
        for e in need_link3:
            need_link += e
        need_link += str(all_iters)
        # need_link = f"http://api.encar.com/search/car/list/premium?count=true&q=(And.(And.Hidden.N._.Year.range(201800..201911)._.Mileage.range(..120000)._.(C.CarType.Y._.(C.Manufacturer.기아._.ModelGroup.스포티지.)))_.AdType.B.)&sr=%7CModifiedDate%7C0%7C{all_iters}"
        try:
            need_link2 = requests.get(need_link, headers=headers)
        except (requests.exceptions.ConnectionError, requests.exceptions.MissingSchema):
            print("Link was wrong")
            return ["E"]
        ans = need_link2.json()["SearchResults"]
        if all_links > int(count_json):
            with open(f"all_info{all_links}.json", 'w') as file:
                json.dump(need_link2.json(),
                        file,
                        indent=4,
                        ensure_ascii=False)
            with open("everything_json.txt", "w") as some_file:
                some_file.write(f"{all_links}")
        with open(f"all_info{all_links}.json") as read_file:
            old_json = json.load(read_file)["SearchResults"]
            old_list_json.append(old_json)

        print(f"Обрабатываю ссылку: {all_links + 1}")
        
        useful_g += 1
        if useful_g > 8:
            useful_g = 1
            useful_p += 1
        try:
            print("[DEBUG] first try")

            c_Id = str(ans[0].get('Id')).strip()
            output_link = f"http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=pic&carid={c_Id}&view_type=hs_ad&wtClick_korList=015&advClickPosition=kor_pic_p{useful_p}_g{useful_g}"
            c_Manufacturer = ans[0].get('Manufacturer').strip()
            c_Model = ans[0].get('Model').strip()
            c_Badge = ans[0].get('Badge').strip()
            c_Transmission = ans[0].get('Transmission').strip()
            c_Photo = ans[0].get('Photo').strip()
            photo_link = f"http://ci.encar.com/carpicture{c_Photo}001.jpg?impolicy=heightRate&amp;rh=138&amp;cw=185&amp;ch=138&amp;cg=Center&amp;wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&amp;wtmkg=SouthEast&amp;wtmkw=68.2&amp;wtmkh=18.7"
            # c_Hotmark = c.get('Hotmark').strip()
            c_FuelType = ans[0].get('FuelType').strip()
            c_Year = str(ans[0].get('Year')).strip()
            c_FormYear = ans[0].get('FormYear').strip()
            c_ServiceCopyCar = ans[0].get('ServiceCopyCar').strip()
            c_Price = str(ans[0].get('Price')).strip()
            c_Mileage = str(ans[0].get('Mileage')).strip()
            c_OfficeCityState = ans[0].get('OfficeCityState').strip()
            print(output_link)
            c_Year2 = list(str(c_Year))
            c_Year5 = ''
            for year in range(len(c_Year2)):
                if year == 4:
                    c_Year5 += ' '
                    c_Year5 += c_Year2[year]
                else:
                    c_Year5 += c_Year2[year]

            print("[DEBUG] first for")

            if c_Mileage != str(old_list_json[0][0].get(
                    'Mileage')).strip():
                print("We're here")
                output_text.append({
                    "Photo": photo_link,
                    "Manufacturer": c_Manufacturer,
                    "Model": c_Model,
                    "Badge": c_Badge,
                    "Transmission": c_Transmission,
                    "FuelType": c_FuelType,
                    "Year": c_Year5,
                    "FormYear": c_FormYear,
                    "ServiceCopyCar": c_ServiceCopyCar,
                    "Price": c_Price,
                    "OfficeCityState": c_OfficeCityState,
                    "Link": output_link,
                    "Mileage": c_Mileage
                })
                useful_p2 = 1
                useful_g2 = 0
                useful_g2 += 1
                if useful_g2 > 8:
                    useful_g2 = 1
                    useful_p2 += 1
                for i in range(1, 25):
                    print(f"ans: {ans[i].get('Mileage')}")
                    print(f"old_json_list: {old_list_json[0][0].get('Mileage')}")
                    c_Id2 = str(ans[i].get('Id')).strip()
                    output_link2 = f"http://www.encar.com/dc/dc_cardetailview.do?pageid=dc_carsearch&listAdvType=pic&carid={c_Id2}&view_type=hs_ad&wtClick_korList=015&advClickPosition=kor_pic_p{useful_p2}_g{useful_g2}"
                    Year_old = str(ans[i].get('Year')).strip()
                    Year_old2 = list(str(Year_old))
                    Year_old3 = ''
                    old_photo = ans[i].get('Photo').strip()
                    old_photo_link = f"http://ci.encar.com/carpicture{old_photo}001.jpg?impolicy=heightRate&amp;rh=138&amp;cw=185&amp;ch=138&amp;cg=Center&amp;wtmk=http://ci.encar.com/wt_mark/w_mark_03.png&amp;wtmkg=SouthEast&amp;wtmkw=68.2&amp;wtmkh=18.7"
                    for year2 in range(len(Year_old2)):
                        if year2 == 4:
                            Year_old3 += ' '
                            Year_old3 += Year_old2[year2]
                        else:
                            Year_old3 += Year_old2[year2]
                    output_text.append({
                        "Photo": old_photo_link,
                        "Manufacturer": ans[i].get('Manufacturer').strip(),
                        "Model": ans[i].get('Model').strip(),
                        "Badge": ans[i].get('Badge').strip(),
                        "Transmission": ans[i].get('Transmission').strip(),
                        "FuelType": ans[i].get('FuelType').strip(),
                        "Year": Year_old3,
                        "FormYear": ans[i].get('FormYear').strip(),
                        "ServiceCopyCar": ans[i].get('ServiceCopyCar').strip(),
                        "Price": str(ans[i].get('Price')).strip(),
                        "OfficeCityState": ans[i].get("OfficeCityState"),
                        "Link": output_link2,
                        "Mileage": str(ans[i].get('Mileage')).strip()
                    })



                    if str(ans[i].get('Mileage')).strip() == str(old_list_json[0][0].get('Mileage')).strip():
                        print("ok")
                        
                        with open(f"all_info{all_links}.json", 'w') as file:
                            json.dump(need_link2.json(),
                                        file,
                                        indent=4,
                                        ensure_ascii=False)
                        return output_text
                
                # return output_text
                with open(f"all_info{all_links}.json", 'w') as file:
                            json.dump(need_link2.json(),
                                        file,
                                        indent=4,
                                        ensure_ascii=False)
                return []

        except IndexError:
            return []
                # print(output_text)
                # print(f"Выполняется итерация: {now_count + 1}/{all_iters}")
                # print(now_count)
                # print(f"Manufacturer: ")
        
    except KeyError:
        pass
    # print(output_text)
    return output_text

    # print(inf)
    # print("#" * 20)
    # print(get_json.text)
    # print(page)


# def main():

# collect_data()
# telegram_bot(bot_token)
# pars_link(user_link=urls[2])
