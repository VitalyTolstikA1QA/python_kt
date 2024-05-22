# python_kt

1. Download all requirement dependencies `pip install -r requirements.txt`

API

1. Add `clent_id` and `client_secret` to `config.json` setting file
2. Run all tests `pytest -v -s -m "api"`

UI

1. Run `pytest -v -s -m "ui"`
2. Options: 
`--browser-channel chrome` for run on local google chrome browser
`--headed` to see ui part of browser
`--browser firefox` for run in firefox