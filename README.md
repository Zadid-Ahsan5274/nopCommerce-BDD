# nopCommerce-BDD

## Tools and technologies used
- Python
- Pycharm
- Behave(Behavior Driven Development Tool)
- Allure Framework(Reporting Utility)

## Scenario of this project
- BDD testing on login feature of nopCommerce demo site

## Prerequisites
- Python
- Pycharm

## How to run this project
- Clone this project
- Import this project to pycharm
- Hit the following commands:
  ```behave <feature files name or folder name>```
  for generating allure reports:
  ```behave -f allure_behave.formatter:AllureFormatter -o reports/ features```
  ```allure serve reports/```
  
## Automation Recording
https://user-images.githubusercontent.com/82231014/204511188-58a68fb3-47b6-4121-97b8-4285ba55adbe.mp4

## Test Report
![Allure Report](https://user-images.githubusercontent.com/82231014/204510960-65278288-161a-41de-a9d6-47c5a4543035.png)
