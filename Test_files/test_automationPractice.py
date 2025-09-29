import json
import logging

import requests

logging.basicConfig(
    level=logging.INFO,  # INFO and above will be logged
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(r"C:\Users\HP\Documents\API_automation\log_files\first.log"),  # logs to file
        logging.StreamHandler()  # also shows in console
    ]
)

logger = logging.getLogger(__name__)



def test_get():
    response = requests.get("https://automationexercise.com/api/productsList")

    dict_data = response.json()

    # print(json.dumps(dict_data, indent=2))

    status_code = response.status_code
    assert status_code == 201

    try:
        assert status_code == 201

    except Exception as e:
        print(e)


def test_post_1():
    post1_response = requests.post("https://automationexercise.com/api/productsList",
                                   json={
                                       "Name": "something",
                                       "age": 25
                                   }
                                   )
    # here the api is not supported to add the json into existing body payload
    # if allowed it will show the status code is 201

    post_code = post1_response.status_code  # 200

    dict_post1 = post1_response.json()

    assert post_code != 201

    for each_dic in dict_post1.items():
        print(each_dic)


def test_get_3():
    get3_res = requests.get("https://automationexercise.com/api/brandsList")

    get3_code = get3_res.status_code
    print(get3_code)  # 200

    assert get3_code == 200

    print(get3_res.json())


def test_put_4():
    put4_res = requests.put("https://automationexercise.com/api/brandsList", json=
    {
        "name": "AutomationPractice"
    }
                            )

    put4_code = put4_res.status_code
    print(put4_code)  # 200

    assert put4_code == 200

    print(put4_res.json())


def test_post_5():
    search_payload_list = [{"search_product": "top"}, {"search_product": "tshirt"}, {"search_product": "jean"}]
    for payload_data in search_payload_list:
        post5_res = requests.post("https://automationexercise.com/api/searchProduct", data=payload_data)

        assert post5_res.status_code == 200

        dict_post5 = post5_res.json()
        print(f"The searched product of {payload_data['search_product']}")
        print(json.dumps(dict_post5, indent=2))


def test_post_6():
    post6_res = requests.post("https://automationexercise.com/api/searchProduct")

    assert post6_res.status_code == 200

    post6_dict = post6_res.json()

    assert post6_dict["message"] == "Bad request, search_product parameter is missing in POST request."


def test_post_7():
    post7_res = requests.post("https://automationexercise.com/api/verifyLogin",
                              data={"email": "padmaraju084@gmail.com",
                                    "password": "AutomationPractice123@@"})
    assert post7_res.status_code == 200

    post7_dict = post7_res.json()
    print(post7_dict)

    assert post7_dict["message"] == "User exists!"


def test_post_8():
    post8_res = requests.post("https://automationexercise.com/api/verifyLogin",
                              data={"password": "AutomationPractice123@@"})
    print(post8_res.json())

    assert post8_res.json()["message"] == "Bad request, email or password parameter is missing in POST request."


def test_del_9():
    del9_res = requests.delete("https://automationexercise.com/api/verifyLogin")
    print(del9_res.status_code)

    print(del9_res.json())

    assert del9_res.json()["message"] == 'This request method is not supported.'


def test_post_10():
    post10_res = requests.post("https://automationexercise.com/api/verifyLogin",
                               data={
                                   "email": "raju@gmail.com",
                                   "password": "raju"
                               })

    assert post10_res.status_code == 200
    print(post10_res.json())

    assert post10_res.json()["message"] == "User not found!"


def test_post_11():
    signup_details = {
        "name": "raju",
        "email": "raju084@gmail.com",
        "password": "AutomationPractice321@@",
        "title": "Mr",
        "birth_date": "09/02/1998",
        "birth_month": "february",
        "birth_year": "1998",
        "firstname": "raju",
        "lastname": "sidda",
        "company": "nothing",
        "address1": "8-472",
        "address2": "gandhi nagar",
        "country": "india",
        "zipcode": "515671",
        "state": "andhra pradesh",
        "city": "dharmavaram",
        "mobile_number": "8142845339 "
    }

    post11_res = requests.post("https://automationexercise.com/api/createAccount", data=signup_details)
    dict_post11 = post11_res.json()
    assert dict_post11["message"] == 'User created!'


def test_del_12():
    del12_res = requests.delete("https://automationexercise.com/api/deleteAccount",
                                data={
                                    "email": "raju04@gmail.com",
                                    "password": "AutomationPractice321@@"
                                })
    assert del12_res.status_code == 200

    dict12_res = del12_res.json()
    print(dict12_res)


def test_put_13():
    updating_details = {
        "name": "raviteja",
        "email": "raju084@gmail.com",
        "password": "AutomationPractice321@@",
        "title": "Mr",
        "birth_date": "09/02/1998",
        "birth_month": "february",
        "birth_year": "1998",
        "firstname": "raju",
        "lastname": "sidda",
        "company": "nothing",
        "address1": "8-472",
        "address2": "gandhi nagar",
        "country": "india",
        "zipcode": "515671",
        "state": "andhra pradesh",
        "city": "dharmavaram",
        "mobile_number": "8142845339 "
    }

    put14_res = requests.put("https://automationexercise.com/api/updateAccount", data=updating_details)
    print(put14_res.json())


def test_get_14():
    get14_res = requests.get("https://automationexercise.com/api/getUserDetailByEmail",
                             data={
                                 "email": "raju084@gmail.com"
                             })

    print(get14_res.json())
