from sum_all_return import added_numbers

def test_added_number_basic_case():
    #Arrange
    numbers = [4, 6, 2, 29]
    expected = 41

    #Act
    result = added_numbers(numbers)

    #Assert
    assert result == expected


def test_added_numbers_with_negative_numbers():
    #Arrange
    numbers = [-5, 10, -3]
    expected = 2

    #Act
    result = added_numbers(numbers)

    #Assert
    assert result == expected

def test_added_numbers_with_empty_list():
    #Arrange
    numbers = []
    expected = 0 # sum[] = 0

    #Act
    result = added_numbers(numbers)

    #Assert
    assert result == expected