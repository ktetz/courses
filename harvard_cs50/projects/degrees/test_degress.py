# test_degrees.py
import pytest
from degrees import load_data, shortest_path, names, people, movies, person_id_for_name

@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    # Setup: Load sample data
    directory = "small"
    load_data(directory)
    yield
    # Teardown: Clear loaded data
    names.clear()
    people.clear()
    movies.clear()

def test_no_path():
    source = person_id_for_name("Person Not in Database")
    target = person_id_for_name("Another Person Not in Database")
    print(f"test_no_path: source={source}, target={target}")
    assert shortest_path(source, target) is None

def test_direct_connection():
    source = person_id_for_name("Kevin Bacon")
    target = person_id_for_name("Tom Hanks")
    path = shortest_path(source, target)
    print(f"test_direct_connection: source={source}, target={target}, path={path}")
    assert path is not None
    assert len(path) == 1
    assert path[0][1] == target

def test_single_degree_of_separation():
    source = person_id_for_name("Kevin Bacon")
    target = person_id_for_name("Meg Ryan")
    path = shortest_path(source, target)
    print(f"test_single_degree_of_separation: source={source}, target={target}, path={path}")
    print(source)
    print(target)
    assert path is not None
    assert len(path) == 1
    assert path[0][1] == target

def test_multiple_degrees_of_separation():
    source = person_id_for_name("Kevin Bacon")
    target = person_id_for_name("Elijah Wood")
    path = shortest_path(source, target)
    print(f"test_multiple_degrees_of_separation: source={source}, target={target}, path={path}")
    assert path is not None
    assert len(path) > 1

if __name__ == '___main__':
    test_direct_connection()