def bottles_of_beer(bob):
    """Use recuresion to print the bottles of beer song.
       :param bob: Integer number of beers that are on the wall
    """
    if bob < 1:
        print("No more bottles of beer on the wall. No more bottles of beer")
        return

    tmp = bob
    bob -= 1
    print("{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it around, {} bottles of beer on the wall.".format(tmp, tmp,bob))

    bottles_of_beer(bob)
bob = bottles_of_beer(99)
print(bob) 