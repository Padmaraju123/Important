import json
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
from POM.payload import *
from Utilities.configurations import *
from Utilities.resources import *

import urllib3

urllib3.disable_warnings()


def test_get():
    # here in post request call we can pass the full path url directly or separate the params and url
    # get_response = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=Rahul Shetty2")

    get_url = getConfig()["API"]["end_point"] + Api_resources.getbook

    get_response = requests.get(get_url,
                                params={
                                    "AuthorName": "Rahul Shetty2"
                                })

    dict_data = get_response.json()
    print(json.dumps(dict_data, indent=2))

    le = len(dict_data) - 1

    while le > -1:
        vv = dict_data[le]["isbn"]
        if vv == "abcd":
            print(f"The isbn book name is {vv}")
            break
        le -= 1

    # validating the status code of the response
    assert get_response.status_code == 200

    # printing the headers of the response the output is not regular dictionary type
    # need to convert with dict() and pass in json.dumps()

    dict_headers = get_response.headers

    print(json.dumps(dict(get_response.headers), indent=2))

    # now print the content-type of the headers
    for each_dict in dict_headers.items():
        if each_dict[0] == "Content-Type":
            assert each_dict[1] == "application/json;charset=UTF-8"
            break


def test_post():
    # the json we are passing must be same which document has if you pass other than
    # we get error and the data will not put in given api

    post_url = getConfig()["API"]["endpoint"] + Api_resources.addbook

    post_response = requests.post(post_url,
                                  json=Post_addbook_Payload(aisle_val="500")
                                  )

    print(post_response.text)
    dict_post = post_response.json()

    id_val = dict_post["ID"]
    delete_book(id_val)

    assert dict_post["Msg"] == "successfully added"


def delete_book(id_val):
    del_url = getConfig()["API"]["endpoint"] + Api_resources.delbook

    del_res = requests.post(del_url,
                            json={
                                "ID": id_val
                            }
                            )

    dict_del = del_res.json()

    print(dict_del["msg"])


# authentication for the git hub url
# basically if we want to sign in to the particular required website with valid credentials we can do by using api

# creating session like separate space so no need to send authentication every test case

session_obj = requests.session()
session_obj.auth = ("padmaraju084@gmail.com", "GitClub1840@@")


def test_authentication():
    auth_res = requests.get("https://api.github.com", auth=("padmaraju084@gmail.com", "GitClub1840@@"), verify=False)

    assert auth_res.status_code == 200


def test_list_repositories():
    repo_res = session_obj.get("https://api.github.com/users/repos", verify=False)
    print(repo_res.status_code)


def test_cookies():
    cookie_res = requests.get("https://rahulshettyacademy.com/", cookies={"visit-month": "February"})
    print(cookie_res.status_code)


# we can validate the cookies which we are passing in this url :https://httpbin.org/
# we create session and pass cookies as well

se = requests.session()
se.cookies.update({"name": "raki"})


def test_validating_cookies():
    validate_res = se.get("https://httpbin.org/cookies", cookies={"name": "raju"})
    print(validate_res.text)
