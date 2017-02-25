"""Create Fake Invoices

Usage: create_fake_payouts.py [-q <int>]

Options:
  -h --help     Show this screen.
  --version     Show version.
  -q=N          Quantity of fake payouts.

"""
from docopt import docopt
from app.encargoapi import app


if __name__ == "__main__":
    arguments = docopt(__doc__, version='Create Fake Payouts 2.0')
    for i in range(int(arguments['-q'])):
        try:
            db.session.add(
                Invoice(
                    client_id=1,
                    client_name="nicolas",
                    client_address="da",
                    client_identifier="32423",
                    client_identifier_type="rewrew",
                    ref_num=i,
                    description="dsdsa",
                    iva=123,
                    iva_total=123,
                    net=123,
                    gross=123,
                    total=123123,
                    invoice_type=1
                )
            )
            db.session.commit()
        except Exception as e:
            print "Ooops! {}".format(e)
            raise
