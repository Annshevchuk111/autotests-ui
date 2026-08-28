import pytest
from _pytest.fixtures import SubRequest


@pytest.mark.parametrize("number",[1, 2, 3, -1])
def test_numbers(number:int):
    print(f'Number {number}')


@pytest.mark.parametrize("numbers,expected",[(1,1),(2,4),(3,9)])
def test_several_number(numbers:int, expected:int):
    assert numbers ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("browser",["chromium", "webkit", "firefox"])
def test_multiplication_numbers(os:str, browser:str):
    assert len(os+browser)>0



@pytest.fixture(params=["chromium", "webkit", "firefox"])
def browser(request:SubRequest):
    return request.param


def test_open_browser(browser:str):
    print(f"Running test on browser {browser}")

@pytest.mark.parametrize("user",["Alice","Zara"])
class TestOperation:

    @pytest.mark.parametrize("account",["Credit card","Debit card"])
    def test_user_with_operation(self, user:str, account:str):
        print(f"Running test with operation {user}")

    def test_user_without_operation(self,user:str):
        print(f"Running test withOUT operation {user}")



users={
"+70000000011":"User with money",
"+70000000022":"User without money",
"+70000000033":"User with operations"
}

@pytest.mark.parametrize(
    "phone_numbers",["+70000000011", "+70000000022", "+70000000033"],
    ids= lambda phone_numbers: f'{phone_numbers} {users[phone_numbers]}'
)
def test_identifiers(phone_numbers:str):
    ...