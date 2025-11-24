import pytest
from bubble_sort import bubble_sort_reverse as bubble_sort

def test_bubble_sort_small_list():
    #Arrange
    input_list = [5, 1, 4, 2, 8]
    expected = [1, 2, 4, 5, 8]
    
    #Act
    result = bubble_sort(input_list)

    #Assert
    assert result == expected

def test_bubble_sort_large_list():
    #Arrange
    input_list = list(range(200, 0, -1))
    expected = list(range(1, 201))

    #Act
    result = bubble_sort(input_list)

    #Assert
    assert result == expected

def test_bubble_sort_empty_list():
    #Arrange
    input_list = []
    expected = []

    #Act
    result = bubble_sort(input_list)

    #Assert
    assert result == expected

def test_bubble_sort_raises_with_non_list_param():
    #Arrange
    not_a_list = "I am not a list"

    #Act + Assert
    with pytest.raises(TypeError):
        bubble_sort(not_a_list)