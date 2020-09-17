def plushaut(nb_list) :
    bn_max = nb_list[0]
    for e in nb_list :
        if e > bn_max :
            bn_max = e
    return bn_max

print(plushaut([1,4,67,88]))