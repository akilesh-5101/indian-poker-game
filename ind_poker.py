def ind_poker_game(seed_value):
    def get_value(arr):
        y = arr.split("_")[1]
        return y
    import random
    random.seed(seed_value)
    rounds_decider = 15
    prob_mid_call_decider = 20

    caller = ""   # assigning caller
    sum_value1 = 0
    sum_value2 = 0
    p_cards = [["", "", "", "", ""],  # First row for player 1 and second row for player 2
               ["", "", "", "", ""]]


    p_values = [[0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]]

    list_players = ["p_1", "p_2"]  # to decide who calls in the end
    play_deck = ["h_1_A", "h_2", "h_3", "h_4", "h_5", "h_6", "h_7", "h_8", "h_9", "h_10", "h_10_J", "h_10_Q", "h_10_K",
                 "d_1_A", "d_2", "d_3", "d_4", "d_5", "d_6", "d_7", "d_8", "d_9", "d_10", "d_10_J", "d_10_Q", "d_10_K",
                 "s_1_A", "s_2", "s_3", "s_4", "s_5", "s_6", "s_7", "s_8", "s_9", "s_10", "s_10_J", "s_10_Q", "s_10_K",
                 "c_1_A", "c_2", "c_3", "c_4", "c_5", "c_6", "c_7", "c_8", "c_9", "c_10", "c_10_J", "c_10_Q", "c_10_K",
                 "J_0", "J_0", "J_0"]

    drop_card = ""
    open_card = ""
    x = 0
    dec_to_call = 0
    turn = ""
    flag_call = ""
    no_of_cards = 0
    index = 0
    p1_cards = ""
    p2_cards = ""




    #shuffled_deck = play_deck    # optional

    for c_0 in range(5):
        p_cards[0][c_0] = random.choice(play_deck)      # giving initial cards to p1
        play_deck.remove(p_cards[0][c_0])

    for c_1 in range(5):
        p_cards[1][c_1] = random.choice(play_deck)       # giving initial cards to p2
        play_deck.remove(p_cards[1][c_1])

    for num in range(5):
        p_values[0][num] = int(get_value(p_cards[0][num]))   # assigning values to cards belonging to the players
        p_values[1][num] = int(get_value(p_cards[1][num]))

    # The setup is ready, following code describes the game


    r = random.randint(1, rounds_decider)
    i = 0
    open_card = random.choice(play_deck)  # to declare open card
    play_deck.remove(open_card)


    while i <= r:

        turn = "running"
        flag_call = False

        for x in range(2):

            dec_to_call = random.randint(1, prob_mid_call_decider)


            if dec_to_call != 5:
                # Given below are special moves in poker
                for card in range(len(p_cards[x])):

                    # More than one card of same (value or face) and the card is same as the open card
                    if int(get_value(open_card)) == p_values[x][card] and p_values[x].count(p_values[x][card]) > 1:
                        no_of_cards = p_values[x].count(p_values[x][card])  # to find the no. of same values
                        if p_values[x][card] > (max(p_values[x]) - 4) and (p_values[x][card]*no_of_cards) >= max(p_values[x]):
                            drop_card = p_cards[x][card]  # to decide the drop card

                            for number in range(no_of_cards):   # for iterating no_of_cards times
                                index = p_values[x].index(p_values[x][card])  # to find index
                                p_values[x].remove(p_values[x][card])   # to remove the number values from list
                                p_cards[x].remove(p_cards[x][index])   # to remove the actual card from p1 list
                            turn = "over"
                            break
                        else:
                            break
                    # More than one card of same (value or face)
                    elif p_values[x].count(p_values[x][card]) > 1:
                        no_of_cards = p_values[x].count(p_values[x][card])  # to find the no. of same values
                        if (p_values[x][card] * no_of_cards) > max(p_values[x]):
                            drop_card = p_cards[x][card]  # to decide the drop card

                            for number in range(no_of_cards):  # just for iterating 'no_of_cards' times
                                index = p_values[x].index(p_values[x][card])  # to find index
                                p_values[x].remove(p_values[x][card])  # to remove the number values from list
                                p_cards[x].remove(p_cards[x][index])  # to remove the actual card from p1 list


                            comp_choice = random.randint(0, 1)  # to take computer choice

                            if comp_choice == 0:
                                p_cards[x].append(random.choice(play_deck))
                                play_deck.remove(p_cards[x][-1])
                                p_values[x].append(int(get_value(p_cards[x][-1])))
                            else:
                                p_cards[x].append(open_card)
                                p_values[x].append(int(get_value(p_cards[x][-1])))

                            turn = "over"
                            break
                        else:
                            break


                    # Card of p1 same as open card
                    elif int(get_value(open_card)) == p_values[x][card]:
                        if p_values[x][card] >= (max(p_values[x]) - 2):
                            drop_card = p_cards[x][card]  # to decide the drop card
                            index = p_values[x].index(p_values[x][card])  # to find index
                            p_values[x].remove(p_values[x][card])  # to remove the number values from list
                            p_cards[x].remove(p_cards[x][index])  # to remove the actual card from p1 list

                            turn = "over"
                            break
                        else:
                            break


                #Normal move
                if turn == "running" and len(p_cards[x]) != 0:
                    index = p_values[x].index(max(p_values[x]))
                    drop_card = p_cards[x][index]
                    index = p_cards[x].index(drop_card)
                    p_cards[x].remove(drop_card)
                    p_values[x].remove(p_values[x][index])
                    comp_choice = random.randint(5, 6)    # to take computer choice of picking a card from deck or open
                    if comp_choice == 5:
                        p_cards[x].append(random.choice(play_deck))
                        play_deck.remove(p_cards[x][- 1])
                        p_values[x].append(int(get_value(p_cards[x][- 1])))
                    else:
                        p_cards[x].append(open_card)
                        p_values[x].append(int(get_value(p_cards[x][- 1])))




                open_card = drop_card          # reassigning drop card to open card





            else:
                flag_call = True
                break

        if flag_call is True:
            break

        i += 1  # this statement is for the while loop iteration

    # Now game is over(while loop ends), following is the result
    #Condition if some player called before3 while loop terminates properly


    if flag_call is True:
        if x == 0:
            for k in p_values[0]:
                sum_value1 += k

            for k in p_values[1]:
                sum_value2 += k

            caller = "Player 1"

        if x == 1:

            for k in p_values[1]:
                sum_value2 += k


            for k in p_values[0]:
                sum_value1 += k

            caller = "Player 2"


    #Condition if while loop finishes smoothly
    else:
        caller = random.choice(list_players)
        if caller == "p_1":

            for k in p_values[0]:
                sum_value1 += k


            for k in p_values[1]:
                sum_value2 += k

            caller = "Player 1"


        else:

            for k in p_values[1]:
                sum_value2 += k

            for k in p_values[0]:
                sum_value1 += k

            caller = "Player 2"

    for pl1 in p_cards[0]:
        p1_cards += f"{pl1}, "

    for pl2 in p_cards[1]:
        p2_cards += f"{pl2}, "


    if sum_value2 > sum_value1:
        resulte = [i, caller, p1_cards, p2_cards, sum_value1, sum_value2, "w_p1"]
    elif sum_value1 > sum_value2:
        resulte = [i, caller, p1_cards, p2_cards, sum_value1, sum_value2, "w_p2"]
    else:
        resulte = [i, caller, p1_cards, p2_cards, sum_value1, sum_value2, "d_d"]

    return resulte


    #************************************************************















