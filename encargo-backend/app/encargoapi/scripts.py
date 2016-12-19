from encargoapi.config import db

def create_databases():
    db.create_all()

if __name__ == '__main__':
    create_databases()