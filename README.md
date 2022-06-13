# Formmated-Address-
CLI tool that query external API to translate free text formatted address to structured address in form of &lt;Street>,&lt;Zip-code>,&lt;City>,&lt;Country>

- we make use of  [Google Maps API](https://maps.googleapis.com/maps/api/geocode/json)

## Prerequisites 
- machine with OS for example machine with Ubuntu 
-  python run time environment version >= 3.8.10
- python package index installed -  pip 
- make sure that to install virtualenv package via pip for example `pip install pipenv`
- git version control 
-  google project key with GeoCoding API add to this project  
## How To Operate 
1. clone project from github 
`
git clone https://github.com/BakrFrag/Formmated-Address-
 `
 2.  navigate to project folder 
 `cd Formatted-Address-`
2. activate virtual environment
    - we can use pipenv package to create & activate virtual environment `pipenv shell ` then `pipenv install` to install requirements 
    - we can use any virtual environment based on python 3.8.10 lik venv 
    - create venv `python3 -m venv venv `
    - activate virtual env `source venv/bin/activate`
    - install libraries `pip install -r requirements.txt` 
3. add executable permission to structured_address.py file 
     - `sudo chmod +x structured_address.py`
 4.  create .env file inside maps/
      - navigate to maps folder `cd maps`
      - create file `touch .env`
      - add blow variables to it 
       - GOOGLE_MAPS_URL=https://maps.googleapis.com/maps/api/geocode/json
       - KEY={YOUR_GOOGLE_PROJECT_API_KEY}
   5.  create .env file inside tests folder 
        - navigate to tests  `cd ../test`
        - create .env file `touch .env`
        -  add variables same as before
 6. start use **structured_address.py** as CLI
    - python structured_address.py -t "text formatted address " 
    -  like ` python structured_address.py -t “5 Av. Anatole, Paris, Champ de Mars”`
  
  ## Google Maps API Specifications
  according to  [Google Maps Geocoding Docs ](https://developers.google.com/maps/documentation/geocoding/requests-geocoding) 
  1. Do not parse the formatted address programmatically. Instead you should use the individual address components, which the API response includes in addition to the formatted address field
4.   The format of the response is not guaranteed to remain the same between requests. In particular, the number of  `address_components`  varies based on the address requested and can change over time for the same address. A component can change position in the array. The type of the component can change. A particular component may be missing in a later response.
5. Note that some countries, such as the United Kingdom, do not allow distribution of true postal addresses due to licensing restrictions.
6.  The array does not necessarily include all the political entities that contain an address, apart from those included in the `formatted_address`. To retrieve all the political entities that contain a specific address, you should use reverse geocoding, passing the latitude/longitude of the address as a parameter to the request
5. One or More address can return in address_components 
## Project  Structure 

- structured_address.py executable file accept CLI argument 
- maps folder package 
      -  maps_template.py include concreate class to query external Maps API geocoding services 
      - defended just necessary methods within class that any class would to query external maps API must define and implementation vary according to external maps api 
      - google_maps_api.py  implement methods to query and fetch data and extract address from Google Maps API 
 - tests folder package
     - include tests for project 
     - test_google_maps_pi.py include unit tests for google_maps_api.py
 - we make use of Factory Design Pattern Structure Pattern this help to extend our services and new services 
- for example if we will use anthor maps API all we have to do is to inherit from QueryMapsApi class and implement all methods in custom implementation according to API , add variables in .env file and place tests in tests/ package folder
  ## Usage example 
  1. make sure you are in root folder of our project 
  2. make sure virtualenv is activated 
  3. start play 
     - for helper message `python structured_address.py -h`
     - for parse address `python structured_address.py -t "{TEXT_ADDRESS}"`
   4. if any error while parsing arguments or flags  error message with helper text will be appear 
5. if more than one address returned from Google Maps API , addresses will be formatted and returned as appeared in response 
6. to run tests  of project 
     - `python -m unittest tests/test_google_maps_api.py`

## Usage Cases 
1. run tests
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python -m unittest tests/test_google_maps_api.py
...
----------------------------------------------------------------------
Ran 3 tests in 2.339s
OK
```
2. test with text -h for helper message 
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -h 

        -h for displaying helper text 
        -t for parse address to search in quote
        example python structured_address.py -t “5 Av. Anatole, Paris, Champ de Mars"
```
3. test with invalid flags 
```bash
Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -vv
invalid flags

        -h for displaying helper text 
        -t for parse address to search in quote
        example python structured_address.py -t “5 Av. Anatole, Paris, Champ de Mars"
```
4. test with text address empty
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -t ""
invalid arguments flags or values

        -h for displaying helper text 
        -t for parse address to search in quote
        example python structured_address.py -t “5 Av. Anatole, Paris, Champ de Mars"

```
6. test with test address not parsed
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -t 
text address not parsed

        -h for displaying helper text 
        -t for parse address to search in quote
        example python structured_address.py -t “5 Av. Anatole, Paris, Champ de Mars"

```
7. text address "5 Av. Anatole, Paris, Champ de Mars"
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -t "5 Av. Anatole, Paris, Champ de Mars"
2 All. Adrienne Lecouvreur,75007,Paris,France
5 Av. Anatole France,75007,Paris,France

```
8. text address "St Anthony's Hospital"
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -t "St Anthony's Hospital"
1200 7th Ave N,33705,St. Petersburg,United States

```
9. text address "Rembrandt House Museum"
```bash
(Formmated-Address-) bk@ubuntu:~/Desktop/Formmated-Address-$ python structured_address.py -t "Rembrandt House Museum"
4 Jodenbreestraat,1011 NK,Amsterdam,Netherlands
```

