from crm import User
import pytest
from tinydb import TinyDB, table
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

def test_db_instance(user):
    # On vérifie si un utilisateur est ajouté en base de donnée que ces données son correct
    assert isinstance(user.db_instance, table.Document)
    assert user.db_instance["first_name"] == "Patrick"
    assert user.db_instance["last_name"] == "Martin"
    assert user.db_instance["address"] == "1 rue du chemin, 75000 Paris"
    assert user.db_instance["phone_number"] == "0123456789"

def test_not_db_instance():
    u = User(first_name="Matthieu",
             last_name="Aston",
             address="13 rue du chemin, 75000 Paris",
             phone_number="0723456789")
    assert u.db_instance is None
    
def test_check_phone_number():
    user_good = User(first_name="Patrick",
            last_name="Martin",
            address="1 rue du chemin, 75000 Paris",
            phone_number="0123456789")
    
    user_bad = User(first_name="Patrick",
            last_name="Martin",
            address="1 rue du chemin, 75000 Paris",
            phone_number="abcd")
    
    with pytest.raises(ValueError) as err:
        user_bad._check_phone_number()
    
    assert "invalide" in str(err.value)

    user_good.save(validate_data=True)
    assert user_good.exists() is True

def test_check_names_empty():
    user_bad = User(first_name="",
             last_name="",
             address="1 rue du chemin, 75000 Paris",
             phone_number="0123456789")
     
    with pytest.raises(ValueError) as err:
            user_bad._check_names()

    assert "Le prénom et le nom de famille ne peuvent pas être vides." in str(err.value)

def test_check_names_invalid_characters():
    user_bad = User(first_name="Patrick%*?&",
             last_name="#(*$",
             address="1 rue du chemin, 75000 Paris",
             phone_number="0123456789")
     
    with pytest.raises(ValueError) as err:
            user_bad._check_names()

    assert "Nom invalide" in str(err.value)
    
def test_delete():
    user_test = User(first_name="Jhon",
    last_name="Smith",
    address="1 rue du chemin, 75015, Paris",
    phone_number="0123456789")

    user_test.save()
    first =  user_test.delete()
    second =  user_test.delete()
    assert len(first) > 0
    assert isinstance(first, list)
   
    assert len(second) == 0
    assert isinstance(second, list)

def test_save():
    user_test = User(first_name="Jhon",
        last_name="Smith",
        address="1 rue du chemin, 75015, Paris",
        phone_number="0123456789")

    user_test_dup = User(first_name="Jhon",
    last_name="Smith",
    address="1 rue du chemin, 75015, Paris",
    phone_number="0123456789")

    first = user_test.save()
    second = user_test_dup.save()
    assert isinstance(first, int)
    assert isinstance(second, int)
    assert first > 0
    assert second == -1
    