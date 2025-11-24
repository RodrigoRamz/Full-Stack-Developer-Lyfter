from sorted_words_function import sorted_words

def test_sorted_words_normal_case(): #test common words
    #Arrange
    text = "python-variable-function-computer-monitor"
    expected = "computer-function-monitor-python-variable"
    #Act
    result = sorted_words(text)
    #Assert
    assert result == expected

def test_sorted_words_already_sorted(): #test words already sorted
    #Arrange
    text = "apple-banana-cherry"
    expected = "apple-banana-cherry"

    #Act
    result = sorted_words(text)

    #Assert
    assert result == expected

def test_sorted_words_reverse_order(): # Test reversed words
    #Arrange
    text = "z-y-x"
    expected = "x-y-z"

    #Act
    result = sorted_words(text)

    #Assert
    assert result == expected

def test_sorted_words_one_word(): #Test on word
    #Arrange
    text = "python"
    expected = "python"

    #Act
    result = sorted_words(text)

    #Assert
    assert result == expected

def test_sorted_words_empty_string(): # test empty input
    #Arrange
    text = ""
    expected = ""

    #Act
    result = sorted_words(text)

    #Assert
    assert result == expected

def test_sorted_words_with_duplicates():
    #Arrange
    text = "dog-cat-dog-bird"
    expected = "bird-cat-dog-dog"

    #Act
    result = sorted_words(text)

    #Assert
    assert result == expected