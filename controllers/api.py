import json

from odoo import http
from odoo.http import request


class Api (http.Controller):

    @http.route(['/api/test'], type="http", auth="public", website=True, method=['POST'],csrf=False)
    def test(self):

        return True