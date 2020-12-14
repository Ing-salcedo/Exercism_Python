def recite(start, take=1):
    sentences = []
    for i in range(start, start-take, -1):
        if i == 0:
            sentences.append("No more bottles of beer on the wall, no more bottles of beer.")
            sentences.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
        elif i == 1:
            sentences.append("1 bottle of beer on the wall, 1 bottle of beer.")
            sentences.append("Take it down and pass it around, no more bottles of beer on the wall.")
        else:
            sentences.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i-1 == 1: sentences.append("Take one down and pass it around, 1 bottle of beer on the wall.")
            else: sentences.append(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        if i != start-take+1: sentences.append('')
    return sentences
