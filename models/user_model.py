from my_app import db
import pandas as pd
from flask import request
from my_app.models import user_model
import requests


class User(db.Model):
    __tablename__= 'user'

    username = db.Column(db.VARCHAR(200), nullable=False, primary_key=True)
    beer_pref = db.Column(db.VARCHAR(200), nullable=False)
    usertravel = db.relationship('Travel', backref='user', cascade='all, delete, delete-orphan')
    
    def __repr__(self):
        return f"User {self.username}"


def find_user(find_name):

    checkname = User.query.filter_by(username=find_name).first()

    if not checkname:
        return None
    
    else:
        return find_name



def add_user_to_db(input_name, favorite):
    
    new_user = User(
        username = input_name,
        beer_pref = favorite
    )

    if not User.query.filter_by(username=input_name).first():
        db.session.add(new_user)
        db.session.commit()


def delete_user_from_db(deletename):

    target = User.query.filter(User.username == deletename).first()

    if target:
        db.session.delete(target)
        db.session.commit() 



def update_user_beer_style(input_name, new_favorite):

    target = User.query.filter_by(username=input_name).first()
    target.beer_pref = new_favorite
    db.session.commit()



def get_users():
    # return all users in db
    return User.query.all()


def get_one_user(target_name=None):
    # return one target user

    if not target_name:
            # select with id
        return User.query.filter_by(username=target_name).first()

    else:
        return None


def get_random_beer():

  # 필스너/골든에일
  url2 = 'https://api.punkapi.com/v2/beers/random'
  random_raw = requests.get(url2).json()
  random_raw = pd.DataFrame(random_raw)

  result_list = {
    'b_id' : random_raw['id'].tolist(),
    'b_name' : random_raw['name'].tolist(),
    'b_food' : random_raw['food_pairing'].tolist(),
    'b_abv' : random_raw['abv'].tolist(),
    'b_desc' : random_raw['description'].tolist(),
    'b_img' : random_raw['image_url'].tolist()
  }

  return result_list


def get_recomm(beer_pref):

  url = 'https://api.punkapi.com/v2/beers'
  raw_data = requests.get(url).json()
  df = pd.DataFrame(raw_data)


  ipas = df[df['description'].str.contains("IPA|India Pale Ale")|df['tagline'].str.contains("IPA|India Pale Ale")|df['name'].str.contains("IPA|India Pale Ale")]
  weisse = df[df['name'].str.contains("Weisse")]

  stout = df[df['description'].str.contains("Stout")]

  pale = df[df['name'] == 'Trashy Blonde']

  porter = df[df['name'].str.contains("Porter")]


  if beer_pref == "필스너" or beer_pref == "골든에일" :

      url2 = 'https://api.punkapi.com/v2/beers/random'
      random_raw = requests.get(url2).json()
      random_raw = pd.DataFrame(random_raw)

      result_list = {
                        'b_id' : random_raw['id'].tolist(),
                        'b_name' : random_raw['name'].tolist(),
                        'b_food' : random_raw['food_pairing'].tolist(),
                        'b_abv' : random_raw['abv'].tolist(),
                        'b_desc' : random_raw['description'].tolist(),
                        'b_img' : random_raw['image_url'].tolist()
                    }

      return result_list


  elif beer_pref == "바이스":

    result_list = {
    'b_id' : weisse['id'].tolist(),
    'b_name' : weisse['name'].tolist(),
    'b_food' : weisse['food_pairing'].tolist(),
    'b_abv' : weisse['abv'].tolist(),
    'b_desc' : weisse['description'].tolist(),
    'b_img' : weisse['image_url'].tolist()}

    return result_list


  elif beer_pref == "스타우트" :

    result_list = {
    'b_id' : stout['id'].tolist(),
    'b_name' : stout['name'].tolist(),
    'b_food' : stout['food_pairing'].tolist(),
    'b_abv' : stout['abv'].tolist(),
    'b_desc' : stout['description'].tolist(),
    'b_img' : stout['image_url'].tolist()}

    return result_list


  elif beer_pref == "포터" :

    result_list = {
    'b_id' : porter['id'].tolist(),
    'b_name' : porter['name'].tolist(),
    'b_food' : porter['food_pairing'].tolist(),
    'b_abv' : porter['abv'].tolist(),
    'b_desc' : porter['description'].tolist(),
    'b_img' : porter['image_url'].tolist()}

    return result_list


  elif beer_pref == "페일에일" :

    result_list = {
    'b_id' : pale['id'].tolist(),
    'b_name' : pale['name'].tolist(),
    'b_food' : pale['food_pairing'].tolist(),
    'b_abv' : pale['abv'].tolist(),
    'b_desc' : pale['description'].tolist(),
    'b_img' : pale['image_url'].tolist()}

    return result_list

  elif beer_pref == "IPA" :

    ipa = ipas.sample(n=1, replace=True)

    result_list = {
    'b_id' : ipa['id'].tolist(),
    'b_name' : ipa['name'].tolist(),
    'b_food' : ipa['food_pairing'].tolist(),
    'b_abv' : ipa['abv'].tolist(),
    'b_desc' : ipa['description'].tolist(),
    'b_img' : ipa['image_url'].tolist()}

    return result_list

  else :
      url2 = 'https://api.punkapi.com/v2/beers/random'
      random_raw = requests.get(url2).json()
      random_raw = pd.DataFrame(random_raw)

      result_list = {
                        'b_id' : random_raw['id'].tolist(),
                        'b_name' : random_raw['name'].tolist(),
                        'b_food' : random_raw['food_pairing'].tolist(),
                        'b_abv' : random_raw['abv'].tolist(),
                        'b_desc' : random_raw['description'].tolist(),
                        'b_img' : random_raw['image_url'].tolist()
                    }

      return result_list