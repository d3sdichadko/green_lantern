from flask_restful import fields

news_structure = {
    "title": fields.String,
    "text": fields.String,
    "date": fields.DateTime
}
