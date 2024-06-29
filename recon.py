import requests

url = "http://afirmm.com"

with open('../common.txt', 'r') as file_list:
    for file in file_list.readlines():
        url_test = url + "/" + file.strip()
        try:
            req = requests.get(url_test)
            if req.status_code == 404:
                continue
            if req.status_code == 200:
                print("[+] File or directory found!: ", file.strip())
            else:
                print("[X] Something has gone wrong with status code: ", req.status_code)
        except requests.exceptions.RequestException as e:
            print("[X] An error occurred: ", e)
