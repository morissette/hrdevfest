import uuid


class Posts(db.Model):
    """
    Our Database Model
    """
    id = db.Column(db.Integer, primary_key=True)
    post_uuid = db.Column(db.String(50))
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)

    def __init__(self, title, content, author):
        self.post_uuid = uuid.uuid4()
        self.title = title
        self.content = content
        self.author = author
        self.created = datetime.utcnow()

    def set_update_time(self):
        self.updated = datetime.utcnow()
