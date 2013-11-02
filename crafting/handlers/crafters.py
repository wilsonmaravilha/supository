import json
import crafting.schema as schema

from base import BaseHandler


class CraftersHandler(BaseHandler):
    def get(self):
        crafters = []
        for c in schema.Crafter.get_all():
            crafters.append({
                'name': c.name,
                'surname': c.surname,
                'about': c.about,
                'location': c.location,
            })
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps(crafters))
