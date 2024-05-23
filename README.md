# python_kt

1. Download all requirement dependencies `pip install -r requirements.txt`

API

1. Add `clent_id` and `client_secret` to `config.json` setting file
2. Run all tests `pytest -v -s -m "api"`

UI

1. Run `pytest -v -s -m "ui"`
2. Options: 
`--browser-channel chrome` for run on local Google Chrome browser
`--headed` to see ui part of browser
`--browser firefox` for run in firefox

Allure report

1. To get allure report you should run the next `pytest --alluredir allure-results`
2. `allure generate --clean` to clean before generating new one report
3. After test run `allure open`

If you want to clear `allure-reports` directory run `python .\framework\reports\allure_remove.py` 

CI (Jenkins)

1. Example of Dockerfile for jenkins `docker build -t jenkins_python_kt .`
```dockerfile
FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv wget gnupg
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
USER jenkins
```
2. Create the local directory for jenkins volume like `C:\Users\v2.tolstik\Documents\jenkins_python_kt`
3. Run `docker run -p 8080:8080 -p 50000:50000 --restart=on-failure -v C:\Users\v2.tolstik\Documents\jenkins_python_kt:/var/jenkins_home jenkins_python_kt` - instead of last name of image change it to your from step 1

Jenkins settings

pre-build `rm -rf python_kt`
build
```
git clone https://github.com/VitalyTolstikA1QA/python_kt
cd python_kt
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
playwright install
pytest -v -s -m ${ENV} --alluredir allure-results ${BROWSER}
```
parameters `ENV - ui, api`, `BROWSER - --browser=chrome,--browser=firefox or --browser-channel chrome`