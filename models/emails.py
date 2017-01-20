from google.appengine.ext import ndb
import datetime


class Email(ndb.Model):
    email = ndb.StringProperty(required=True)
    inserted_at = ndb.DateTimeProperty(required=True)

    @classmethod
    def check_if_exist(cls, email):
        return cls.query(cls.email == email).get()

    @classmethod
    def add_email(cls, email):

        database_email_entity = cls.check_if_exist(email)

        now = datetime.datetime.now()
        created = False

        if not database_email_entity:
            cls(
                email=str(email),
                inserted_at=now,
            ).put()
            created = True
        else:
            now = database_email_entity.inserted_at
        return {
            'created': created,
            'email': str(email),
            'inserted_at': str(now)
        }

    @classmethod
    def delete_email(cls, email):

        database_email_entity = cls.check_if_exist(email)
        if not database_email_entity:
            return {
                'email': 'email does not exist',
            }
        else:
            database_email_entity.email.delete()
            return {
                'email': 'email deleted',
            }

    @classmethod
    def get_all_emails(cls):
        return cls.query().fetch()
