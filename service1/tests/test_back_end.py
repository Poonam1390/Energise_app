import unittest
import os
from flask import abort, url_for
from flask_testing import TestCase
# from flask_sqlalchemy import SQLAlchemy
from application import app, db
from application.models import Play
# from application.forms import RoutineForms
class TestBase(TestCase):
    def create_app(self):
        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(
         SQLALCHEMY_DATABASE_URI=('mysql+pymysql://root:root@mysql:3306/energise-app'),
         SECRET_KEY=os.getenv('TEST_SECRET_KEY'),
         WTF_CSRF_ENABLED=False,
             )
        return app
    def setUp(self):
        """
        Will be called before every test
        """
    # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()
        # register test data  to database
        playdata = Play(Exercise = 'press ups', Sing = 'Bohemian Rhapsody',  Dance = 'Rock the boat')
        # saves data 
        db.session.add(playdata)
        db.session.commit()
        id = Play.query.filter_by(id=playdata.id).first()

    def tearDown(self):
        """
        Will be called after every test
        """
        db.session.remove()
        db.drop.all()


class TestViews(TestBase):
    def test_homepage_view(self):
        """
        Check homepage is accessible
        """
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_addroutine_view(self):
        """
        Check that the addroutine page is available
        """
        response = self.client.get(url_for('addRoutine'))
        self.assertEqual(response.status_code, 200)
##class RoutineForms(TestBase):
  #  def test_exercise_len(self):
       # Test length of input is less than two
   #     with self.client:
