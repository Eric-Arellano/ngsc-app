from backend.src.app import encryptor


def test_string():
    original = "Test me out!"
    encrypted = encryptor.encrypt(original)
    decrypted = encryptor.decrypt(encrypted)
    assert decrypted == original != encrypted


def test_basic_dict():
    original = {"key1": "value1", "key2": "value2"}
    encrypted = encryptor.encrypt_dict_values(original)
    decrypted = encryptor.decrypt_dict_values(encrypted)
    # check keys not changed, only values
    assert encrypted["key1"] != original["key1"]
    assert encrypted["key2"] != original["key2"]
    # check decrypts back to original
    assert decrypted == original != encrypted


def test_nested_dict():
    original = {
        "n1_k1": {"n2_k1": {"n3_k1": "n3_v1"}, "n2_k2": "n2_v2"},
        "n1_k2": "n1_v1",
    }
    encrypted = encryptor.encrypt_dict_values(original)
    decrypted = encryptor.decrypt_dict_values(encrypted)
    # check keys not changed, only values
    assert encrypted["n1_k1"] != original["n1_k1"]
    assert encrypted["n1_k1"]["n2_k1"] != original["n1_k1"]["n2_k1"]
    assert encrypted["n1_k1"]["n2_k1"]["n3_k1"] != original["n1_k1"]["n2_k1"]["n3_k1"]
    # check decrypts back to original
    assert decrypted == original != encrypted


def test_demographics():
    original = {
        "1000569932": {
            "campus": "Tempe",
            "cohort": "3",
            "committee": "Admin",
            "email": "jseidne@asu.edu",
            "leadership": "Admin Chair",
            "missionTeam": "25",
            "name": {"first": "Jeremy", "last": "Seidner"},
            "phone": "4063344442",
        },
        "1000660254": {
            "campus": "Tempe",
            "cohort": "3",
            "committee": "Communications",
            "email": "Daniel.Tullie@asu.edu",
            "leadership": "",
            "missionTeam": "26",
            "name": {"first": "Daniel", "last": "Tullie"},
            "phone": "6024109312",
        },
    }
    encrypted = encryptor.encrypt_demographics(original)
    decrypted = encryptor.decrypt_demographics(encrypted)
    # check ASUrites changed
    assert original.keys() != encrypted.keys()
    # check decrypts back to original
    assert decrypted == original != encrypted
