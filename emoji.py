import emoji as emo

def to_text(a):

    text = emo.demojize(a)
  
    return text


a = input("Enter the desired emojis here")

b = to_text(a)

print(b)

