from google.appengine.ext import ndb
from como.hash_url_file import UrlHash
import datetime


class CheckedFiles(ndb.Model):
    url = ndb.StringProperty(required=True)
    sha1 = ndb.StringProperty(required=True)
    has_changed_lately = ndb.BooleanProperty(required=False)
    last_checked = ndb.DateTimeProperty(required=True)

    @classmethod
    def check_if_exist(cls, url):
        return cls.query(cls.url == url).get()

    @classmethod
    def add_new_file(cls, url):

        # calculate hash regardless of existence in database

        new_potentially_file_entity_hash = UrlHash(url).hash

        database_file_entity = cls.check_if_exist(url)

        now = datetime.datetime.now()

        if not database_file_entity:
            created = True
            has_changed = False
            cls(
                url=str(url),
                sha1=str(new_potentially_file_entity_hash),
                has_changed_lately=created,
                last_checked=now,
            ).put()
        else:
            created = False
            has_changed = cls.compare_hash(str(new_potentially_file_entity_hash), str(database_file_entity.sha1))
            database_file_entity.has_changed_lately = has_changed
            database_file_entity.last_checked = datetime.datetime.now()
            database_file_entity.put()
            database_file_entity.put()

        return {
            'created': created,
            'has_changed_lately': has_changed,
            'last_checked': str(now),
        }

    @classmethod
    def compare_hash(cls, current_hash, stored_hash):
        return not current_hash == stored_hash

    @classmethod
    def get_all_menaged_files(cls):
        return cls.query().fetch()
