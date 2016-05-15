def _handle_response(self, response, data=[], raw=False):
    return data if raw else simplejson.loads(data)
