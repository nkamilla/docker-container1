FROM jupyter/base-notebook

# Instalacja dodatkowych bibliotek Python
RUN pip install pandas sqlalchemy psycopg2-binary

# Ustawienie katalogu roboczego
WORKDIR /home/nkamill

# Uruchomienie Jupyter Notebook bez tokena (dla uproszczenia)
CMD ["start-notebook.sh", "--NotebookApp.token=''"]
