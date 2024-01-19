def ra(tkst1):

    with open(tkst1, 'r', encoding='utf-8') as kkkk:
            rinds = kkkk.readlines()

            if len(rinds) >= 3:
                rinda3 = rinds[2].strip()
                print(f"Trešās rindas saturs: {rinda3}")
            else:
                print("Failā nav pietiekami daudz rindu.")


tkst1 = 'tavstxtfails.txt'
ra(tkst1)