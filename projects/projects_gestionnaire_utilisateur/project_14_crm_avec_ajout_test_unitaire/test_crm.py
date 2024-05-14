from crm import User
import pytest
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

@pytest.fixture
def setup_db():
# Utilisation de la base de donnée en mémoire lors des tests (permet de ne pas créer de fichier supplémentaire)
   User.DB = TinyDB(storage=MemoryStorage)
  

@pytest.fixture
def user(setup_db):
    setup_db
    u = User(first_name="Patrick",
             last_name="Martin",
             address="1 rue du chemin, 75000 Paris",
             phone_number="0123456789")
# Sauvegarde un utilisateur en mémoire. 
    u.save()
    return u

def test_first_name(user):
    assert user.first_name == "Patrick"

def test_full_name(user):
    assert user.full_name == "Patrick Martin"

def test_exists(user):
    assert user.exists() is True

def test_not_exists():
    # On utilise les données d'un utilisateur qui n'est pas sauvegardé en base de donnée. 
    u = User(first_name="Matthieu",
             last_name="Aston",
             address="13 rue du chemin, 75000 Paris",
             phone_number="0723456789")
    assert u.exists() is False

def test_db_instance():
    assert False

def test_check_phone_number():
    assert False

def test_check_names():
    assert False
    
def test_delete():
    assert False

def test_save():
    assert False