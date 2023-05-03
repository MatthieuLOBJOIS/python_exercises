"""Module to generate a random users"""
import faker

def get_user() -> str:
    """Generate a single user

    Returns:
        str: user
    """
    fake = faker.Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    return f"{first_name} {last_name}"
    
def get_users(number: int) -> list[str]:
    """Generate a list of users

    Args:
        number (int): number of users to generate

    Returns:
        list[str]: users
    """
    return [get_user() for _ in range(number)]

if __name__ == "__main__":
    get_users(6)