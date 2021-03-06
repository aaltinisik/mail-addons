# Copyright 2016 x620 <https://github.com/x620>
# Copyright 2016,2020 Ivan Yelizariev <https://it-projects.info/team/yelizariev>
# Copyright 2018 Ruslan Ronzhin
# Copyright 2019 Artem Rafailov <https://it-projects.info/team/Ommo73/>
# License LGPL-3.0 (https://www.gnu.org/licenses/lgpl.html).
{
    "name": """Show message recipients""",
    "summary": """Allows you be sure, that all discussion participants were notified""",
    "category": "Discuss",
    "images": ["images/1.png"],
    "version": "12.0.1.1.1",
    "author": "IT-Projects LLC, Pavel Romanchenko",
    "support": "apps@itpp.dev",
    "website": "https://itpp.dev",
    "license": "LGPL-3",
    "price": 40.00,
    "currency": "EUR",
    "depends": ["mail"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["templates.xml"],
    "qweb": ["static/src/xml/recipient.xml"],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
