from application import db


class Play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exercise = db.Column(db.String(100), nullable=False, unique=True)
    sing = db.Column(db.String(500), nullable=False, unique=True)
    dance = db.Column(db.String(500), nullable=False, unique=True)
    
    def __repr__(self):
        return ''.join([
            'Exercise: ', self.exercise,'\r\n',
            'Song: ', self.sing,'\r\n',
            'Dance: ', self.dance, '\r\n', self.content
            ])