import faker

def get_user() -> str:
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"
    
def get_users(number: int) -> list:
    print([get_user() for _ in range(number)])

if __name__ == "__main__":
    get_users(6)