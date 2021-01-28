import json
import random
import pytest

def main() -> (dict, dict, dict, dict, ):
    # NOTE: Get all the parse commands
    # NOTE: Get all the copy commands
    parse_commands = []
    copy_commands = []
    random_commands = []


    with open ('data.txt') as file:
        data=json.load(file)
        random_commands = random.sample(data, 2)

    for row in data:
        if 'function' in row and row['function'] == 'parse':
            parse_commands.append(row.copy())
        if 'function' in row and row['function'] == 'copy':
            copy_commands.append(row.copy())
    print(f"parse_commands: {parse_commands}")
    print(f"copy_commands: {copy_commands}")

    # NOTE: Put the two lists together and say which list it came from as well as the item number for that list
    functional_commands = []
    counter = 0
    counter1=0
    for row,row1 in zip(parse_commands,copy_commands):
        counter += 1
        new_row = row.copy()
        new_row['_list'] = 'parse'
        new_row['_counter'] = counter
        functional_commands.append(new_row)
        counter1 += 1
        new_row1 = row1.copy()
        new_row1['_list'] = 'copy'
        new_row1['_counter'] = counter1
        functional_commands.append(new_row1)


    print(f"functional_commands: {functional_commands}")

    print(f"random_commands: {random_commands}")

    return parse_commands, copy_commands, functional_commands, random_commands


@pytest.fixture()
def my_fixture():
    parse_commands, copy_commands, functional_commands, random_commands = main()


# test for passed parse
def test_parse():
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
#test to  check dict
def test_check():
    parse_commands, copy_commands, functional_commands, random_commands = main()
    assert type(copy_commands)=="class 'list'"
def test_parse_fail():
    parse_commands, copy_commands, functional_commands, random_commands = main()

    assert parse_commands == [{'function': 'copy', 'help': 'file help', 'value': 'file'}]
def test_copy():
    parse_commands, copy_commands, functional_commands, random_commands = main()
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
def test_functional():
    parse_commands, copy_commands, functional_commands, random_commands = main()
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
def test_random():
    parse_commands, copy_commands, functional_commands, random_commands = main()
    assert len(random_commands) == 2



if __name__ == '__main__':
    parse_commands, copy_commands, functional_commands, random_commands = main()


    assert parse_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file'}]
    assert copy_commands == [{'function': 'copy', 'help': 'copy help', 'value': 'file'}]
    assert functional_commands == [{'function': 'parse', 'help': 'file help', 'value': 'file', '_list': 'parse', '_counter': 1}, {'function': 'copy', 'help': 'copy help', 'value': 'file', '_list': 'copy', '_counter': 1}]
    assert len(random_commands) == 2
