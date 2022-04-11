from unittest import TestCase

from app import app
from models import db, Cupcake

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///TESTING DATABASE_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

db.drop_all()
db.create_all()


PROVIDE DATA YOU MIGHT FIND NECESSARY


class APP_NAMEViewsTestCase(TestCase):
    """Tests for views of API."""

    def setUp(self):
        """APPLIES BEFORE EACH TEST"""

        MODEL.query.delete()

        NEWMODELINSTANCEFORTEST = MODEL(INSTANCE_DATA)
        db.session.add(THEINSTANCE)
        db.session.commit()

        self.cupcake = cupcake

    def tearDown(self):
        """APPLIES AFTER EACH TEST"""

        db.session.rollback()

    def SAMPLETEST(self):
        with app.test_client() as client:
            resp = client.get("/ROUTE TO TEST")

            self.assertEqual(resp.status_code, 200)

            data = HOWEVER YOU ACCESS DATA
            self.assertEqual
