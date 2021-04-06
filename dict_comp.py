
def dict_comp():

    new_list_created = []
    new_dict_created = {}
    try:
        stop = int(input("Input your stop value: "))
        step = int(input("Input your step value: "))

        input_list_generated = list(range(1, stop+1))

        new_list_created = [input_list_generated[i:i+step]
                            for i in range(0, len(input_list_generated), step)]

        new_dict_created = {
            ("Item-"+str(i+1)): new_list_created[i] for i in range(stop // step)}
    except Exception as err:
        print("There is an error", err)

    print(new_dict_created)


dict_comp()
