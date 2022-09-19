from threading import Thread

def TestFunc():
    while flag:
        print("hello")

if __name__ == "__main__":
    flag = True

    th = Thread(target=TestFunc)
    th.start()

    input("duda")
    flag = False
    th.join()