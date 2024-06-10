# frontend

## test-dashboard-store

Create api to resolve an store dashboard

## How to setup

## Requirements

    1. Docker version 26.00 or greter
    2. Angular cli v18
    3. Node v22.2

## Local Development

  1.Run npm install --force

  2. Run npm start

## Documentation

  The structor off project each module or app is a package to return especific endpoints and each contain:
  
    - compnents: All ui of the app
    - domain: Contain the bussiness logic 
        - models: the class to manipulate the data in the app
        - repositories: Run the call to services
        - use-case: logic to manipulate the data models
    -infraestructure:
        - dto: interface to translate the information get from the api
        - services: Calls to api endpoints
        - mappers: addap the api infromation to bussiness logic
  