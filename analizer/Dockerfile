FROM python:3.10

# copy source code to image
COPY . /app
WORKDIR /app

# install system dependencies for the project
RUN pip install pipenv

# install from Pipfile
RUN pipenv install

RUN mkdir logs

# nltk models used - maxent_treebank_pos_tagger
RUN pip install nltk && python -m nltk.downloader -d /usr/local/share/nltk_data vader_lexicon

# CMD ["pipenv", "run", "python", "main.py"]