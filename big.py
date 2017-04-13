from random import randint

def write_big_csv():
    file = open("big_network.csv", "w+")
    for i in range(1,1000000):
        if(randint(1,20) == 1 or i == 1):
            repost_id = -1 # Make a root node
        else:
            repost_id = i - randint(1,5)
            if(repost_id < 1):
                repost_id = 1
        followers = randint(1,50)
        file.write("{0},{1},{2}\n".format(i, repost_id, followers))

if __name__ == "__main__":
    print("Creating csv values...")
    write_big_csv()