from reverse_function import reverse

def test_reverse_basic_word(): #verify the reverse
    #Arrange
    text = "Hola"
    expected = "aloH"

    #Act
    result = reverse(text)

    #Assert
    assert result == expected

def test_reverse_with_spaces(): #verify if a space needs to be reverted
    #Arrange
    text = "Hello Word"
    expected = "droW olleH"

    #Act
    result = reverse(text)

    #Assert
    assert result == expected

def test_reverse_empty_string(): #verify that empty does not break the function
    #Arrange
    text = ""
    expected = ""

    #Act
    result = reverse(text)

    #Assert
    assert result == expected


