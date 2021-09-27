from flask import Blueprint, request, redirect, url_for, Response, render_template
from my_app.models import user_model, trip_model
from my_app import db

bp = Blueprint('user', __name__)


@bp.route('/user', methods=['POST'])
def add_user():

    db.create_all()

    username = request.form.get('username')
    beer_pref = request.form.get('beer_pref')


    user_list = {
                    'username': username,
                    'favorite': beer_pref
                }



    if not username:
        return "이름을 입력해주세요.", 400

    elif not beer_pref:
        return "내게 맞는 수제맥주 찾기 결과 혹은 선호하는 수제맥주 종류를 입력해주세요.", 400

    elif not user_model.user_model.get_one_user(target_name=username):
        user_model.add_user_to_db(username, beer_pref)
        beer_result = user_model.get_recomm(beer_pref=beer_pref)

        return render_template('user.html', user_list=user_list, beer_result=beer_result)

    elif username == user_model.get_one_user(target_name=username):
        user_model.update_user_beer_style(input_name=username, new_favorite=beer_pref)
        beer_result = user_model.get_recomm(beer_pref=beer_pref)

        return render_template('user.html', user_list=user_list, beer_result=beer_result)



@bp.route('/user/')
@bp.route('/user/<username>')
def delete_user(username=None):

    if not username:
        return "존재하지 않는 유저입니다.", 400

    elif not user_model.find_user(username):
        return "존재하지 않는 유저입니다.", 400

    else :
        user_model.delete_user_from_db(username)
        return redirect(url_for('main.user_index', msg_code=3), code=200), 200