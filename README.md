# Multiride
This project is for Advanced Algorithmics and Programming Class at ISEP.  
The goal of this project is to create an API that calculate journeys from point A to point B by combining public transport and uber rides in Paris.  

## Getting Started

you can clone the repository with :

```bash
git clone https://github.com/k-1001/multiride.git
```

### Prerequisites

You need to have some credentials to access used APIs :

- [Uber](https://developer.uber.com/)
- [Navitia](http://doc.navitia.io/)  

See file .env.example to configurate your environment variables

### Installing

This project is coded in Python 3.7.3 so you need python to run it. We also recommend to configurate a virtual environment to test this project. 
 
We used several python librairies for this project :

- flask
- requests
- request
- jsonify
- uber-rides
- python-dotenv

To install them you need to run :

```bash
pip install -r requirements.txt
```

### Running

To run the project, use the command :

```bash
python app.py
```

## API Documentation

The API have the following endpoints :

- GET / -> verify that the API works
- POST /geocode -> calculate coordinates of a given address

  ```bash
  {"address" : "28 rue notre dame des champs Paris France"}
  ```

- POST /journey -> calculate journey

  ```json
  {
    "from":"address 1",
    "to":"address2"
  }
  ```

## Authors

- **Camille Marchetti** - [k-1001](https://github.com/k-1001)
- **Henry Matheisen** - [hmatheisen](https://github.com/hmatheisen)
