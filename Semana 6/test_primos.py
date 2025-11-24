from primos import primos

def test_primos_with_values_less_than_or_equal_one():
    #Arrange
    numbers = [-10, -1, 0, 1]

    #Act + Assert
    for n in numbers:
        assert primos(n) is False

def test_primos_with_non_prime_numbers():
    #Arrange
    numbers = [4, 6, 8, 9, 10, 12, 15]

    #Act + Assert
    for n in numbers:
        assert primos(n) is False

def test_primos_with_prime_numbers():
    #Arrange
    numbers = [2, 3, 5, 7, 11, 13, 17, 67]

    #Act + Assert
    for n in numbers:
        assert primos(n) is True

def test_primos_with_large_prime():
    #Arrange
    n = 97

    #Act
    result = primos(n)

    #Assert
    assert result is True