from upper_lower_counter import letters

def test_letters_normal_sentence():
    #Arrange #a sentence with upper and lower letters with spaces
    text = "I love Nacion Sushi"
    expected = (13, 3) #13 lower, 3 upper

    #Act
    result = letters(text)

    #Assert
    assert result == expected

def test_letters_all_uppercase():
    #Arrange # count of all letters are upper letters
    text = "HELLO"
    expected = (0, 5)

    #Act
    result = letters(text)

    #Assert
    assert result == expected

def test_letters_all_lowercase():
    #Arrange # count of all letters are lower letters
    text = "hello"
    expected = (5, 0)

    #Act
    result = letters(text)

    #Assert
    assert result == expected

def test_letters_with_numbers_and_symbols():
    #Arrange #mix of letters, numbers and symbols #numbers are not counted as upper or lower cases
    text = "Hi! 123? aA"
    expected = (2, 2)

    #Act
    result = letters(text)

    #Assert
    assert result == expected 