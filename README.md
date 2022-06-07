
##Requisites

To run this application locally is necessary the following itens: 

* Python 3.8 or superior
* AWS  CLI 
* AWS SAM CLI 
* Localstack container up at port 4566

Also is necessary create the s3 bucket:
aws s3 mb s3://pokedex --endpoint-url=http://localhost:4566

# How to use
Run this lambda and post a command at SQS - to catch an pokemon

To list pokemons on your pokedex use: 
aws s3 ls s3://pokedex --endpoint-url=http://localhost:4566

To see the image on nagivator use: 
http://localhost:4566/pokedex/{pokemon-file}
