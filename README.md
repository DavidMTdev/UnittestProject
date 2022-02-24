# UnittestProject

## Execution des scripts 

Pour lancer l'api obligatoire avant de lancer le scrapper et les test unitaires

``python run_api.py``

Pour lancer le scrapper 

``python run_scrapper.py``


Par défaut le script du scrapper utilise le driver de Edge.
Pour mettre le Chrome Driver il faut dans ``scripts/__init__.py ``

```` python
def run():
    # Décommenter pour utilise le Chrome Driver et commenter scrapper = init_EdgeDriver()
    # scrapper = init_ChromeDriver()
    scrapper = init_EdgeDriver()
    runScrapper(scrapper)
    scrapper.driver.close()
````