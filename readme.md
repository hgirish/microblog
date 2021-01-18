clone the project in a directory
cd to that directory
create virtual environment
python -m venv venv
.\venv\Scripts\activate # for windows 
pip install -r .\requirements.txt
flask db upgrade

optional: pip install python-dotenv # if using .flaskenv
