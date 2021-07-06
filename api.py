import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

pokedex=[
{
'number': "001",
'name': "Bulbasaur",
'types': [
"Grass",
"Poison"
],
},
{
"number":"002",
"name": "Ivysaur",
"types": [
"Grass",
"Poison"
],
}
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Pokedex</h1>"

@app.route('/api/pokedex/all', methods=['GET'])
def pokedex_all():
    return jsonify(pokedex)

@app.route('/api/pokedex/<string:number>')
def pokedex_num(number):
  templist=[]
  for pokemon in pokedex:
    if pokemon['number'] == number:
          templist.append(pokemon)
    if number in pokemon['types'] :      
         templist.append(pokemon)
  return jsonify(templist)

@app.route('/api/pokedex/delete/<string:number>',methods=['DELETE'])
def pokedex_delete(number):
 
  for pokemon in pokedex:
    if pokemon['number'] == number:
          delpokemon=pokemon
        
  for pokemon in pokedex:
    if 'evolutions' in pokemon:
      if delpokemon in pokemon['evolutions']:
          return jsonify({"message":"pokemon is evolution of other pokemon"})  
  for pokemon in pokedex:
    if pokemon['number'] == number:
          pokedex.remove(pokemon)
               
  return jsonify(pokedex)  

@app.route('/api/pokedex/update/<string:number>',methods=['PUT'])
def pokedex_update(number):
  request_data = request.get_json()
  update_pokemon = {
    'number':request_data['number'],
    'name':request_data['name'],
    'types':request_data['types']
  }  
  for pokemon in pokedex:
    if pokemon['number'] == number:
          index=pokedex.index(pokemon)
          pokedex[index]=update_pokemon
          return jsonify(update_pokemon)
  return jsonify ({'message': 'pokemon not found'}) 

@app.route('/api/pokedex/addevolution/<string:number1>/<string:number2>',methods=['PUT'])
def addevo(number1,number2):
    for pokemon in pokedex:
      if(pokemon['number']==number2):
          addpokemon=pokemon
    for pokemon in pokedex:
      if(pokemon['number']==number1):
          addedpokemon=pokemon
          index=pokedex.index(pokemon)
          if 'evolutions' in pokemon:
           (addedpokemon['evolutions']).append(addpokemon) 
          else :
            evo=[]
            evo.append(addpokemon)
            addedpokemon['evolutions']=evo
          pokedex[index]=addedpokemon
          return jsonify(pokedex)
    return jsonify ({'message': 'pokemon not found'}) 

@app.route('/api/pokedex/delevolution/<string:number1>/<string:number2>',methods=['PUT'])
def delevo(number1,number2):
    for pokemon in pokedex:
      if(pokemon['number']==number2):
          delpokemon=pokemon
    for pokemon in pokedex:
      if(pokemon['number']==number1):
          deledpokemon=pokemon
          index=pokedex.index(pokemon)
          if 'evolutions' in deledpokemon:
           if delpokemon in deledpokemon['evolutions']:
             (deledpokemon['evolutions']).remove(delpokemon)
             if(deledpokemon['evolutions']):
                pokedex[index]=deledpokemon
             else:  
               del deledpokemon['evolutions']
               pokedex[index]=deledpokemon  
                  
          return jsonify(pokedex)
    return jsonify ({'message': 'pokemon not found'}) 
        
           
@app.route('/api/pokedex/create' , methods=['POST'])
def create_pokemon():
  request_data = request.get_json()
  new_pokemon = {
    'number':request_data['number'],
    'name':request_data['name'],
    'types':request_data['types']
  }
  pokedex.append(new_pokemon)
  return jsonify(pokedex)


app.run()