def speak_directed():
    print("meow direct")

def speak_imported():
    print(" meow imported")


if __name__=="__main__":
    speak_directed() ## ana dosya( kendisi) çalıştırılıyorsa bu
else:
    speak_imported() # başka yerden çağrılıyorsa bu çalışsın


def test():
    print("farkettiysen speak fonksiyonu ana klasorde olmadığında çağrılmadığı halde çalıştı")