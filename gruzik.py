import requests
header = {'Accept': 'application/json'}

# Use following for a csv response:
# header = {'Accept': 'text/csv'}

response = requests.get(
    'https://modis.ornl.gov/rst/api/v1/MOD13Q1/subset?latitude=35.958767&longitude=-84.287433&startDate=A2018049&endDate=A2018049&kmAboveBelow=1&kmLeftRight=1', headers=header)
print(response.json())