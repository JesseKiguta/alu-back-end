if __name__ == "__main__":
    import requests

url = 'https://intranet.aluswe.com/rltoken/XNmscHBY0THdxQXM_MVzdw'
response = requests.get(url)

data = response.json()
name = data['EMPLOYEE_NAME']
tasknum = data['NUMBER_OF_DONE_TASKS']
tasksum = data['TOTAL_NUMBER_OF_TASKS']