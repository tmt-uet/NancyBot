### NancyBot
## 1.Create Virtualenv
virtualenv -p python3 env
## 2.Active Virtualenv
source env/bin/activate
## 3. Install rasa and rasa xlibrary
pip install rasa_core rasa_nlu rasa_core_sdk feedparser spacy  sklearn_crfsuite
python -m spacy download en
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
## 4. Train and run
# train rasa
rasa train
# run action
python -m rasa_core_sdk.endpoint --actions actions
# run rasa x to test
rasa x


