# © 2022 PCCube
# @author: vcS <vcavallarosilva@pccube.com>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo.http import request


class Hello(http.Controller):

    @http.route('/helloworld', auth='public', website=True)
    def helloworld(self):
        # return('<h1>Hello World!</h1>')
        return request.render('library_website.helloworld')

    @http.route('/hellocms/<page>', auth='public', website=True)
    def hellocms(self, page, **kwargs):
        return http.request.render(page)
