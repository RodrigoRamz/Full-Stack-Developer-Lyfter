def reverse(text):
        my_reverse_text = ''
        for i in range(len(text)-1, -1, -1):
                my_reverse_text += text[i]
        return my_reverse_text

result = reverse('Hello Word')
print (result)