    # scenario.p("Bob funds in parallel another auction")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(10),token_ids=[sp.nat(4),sp.nat(5),sp.nat(6)]).run(sender=admin)
    # scenario.p("Bob bids")
    # scenario += auction_house.bid(10).run(sender=bob, amount=sp.mutez(1000000), now=sp.timestamp(0))
    # scenario.p("Alice withdraws (something that had minimal bid, but nobody who bidded)")
    # scenario += auction_house.withdraw(0).run(sender=alice, a    mount=sp.mutez(0), now=sp.timestamp(3+60*60))

    # scenario.p("Bob withdraws")
    # scenario += auction_house.withdraw(10).run    (sender=bob,  now=sp.timestamp(1+5*24*60*60))

    # scenario.h2("Self-Bid")
    # scenario.p("Bob creates auction")
    # auction_id = sp.nat(0) # we can reuse 0
    # scenario += fa2.update_operators([sp.variant('add_operator', sp.record(owner=bob.address,operator=auction_house.address,token_id=sp.nat(4)))]).run(sender=bob)
    # scenario += auction_house.create_auction(sp.record(auction_id=auction_id, token_address=fa2.address, token_id=sp.nat(4), token_amount=sp.nat(1),  end_timestamp=sp.timestamp(60*60),  bid_amount=sp.mutez(1    00000))).run(sender=bob, now=sp.timestamp(0))

    # scenario += auction_house.bid(0).run(sender=bob, amount=sp.mutez(200000), valid=False, now=sp.timestamp(2))
    # scenario += auction_house.withdraw(0).run    (sender=bob,  now=sp.timestamp(1+5*24*60*60))

    # scenario.h2("Existing Auctions")
    # scenario.p("Bob creates auction with same id")
    # scenario += fa2.update_operators([sp.variant('add_operator', sp.record(owner=bob.address,operator=auction_house.address,token_id=sp.nat(4)))]).run(sender=bob)
    # scenario += auction_house.create_auction(sp.record(auction_id=1, token_address=fa2.address, token_id=sp.nat(4), token_amount=sp.nat(1),  end_timestamp=sp.timestamp(60*60),  bid_amount=sp.mutez(100000))).run(    sender=bob, now=sp.timestamp(0), valid=False)



        
    # scenario.p("Kick-off initial Auctions")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(0),token_ids=[sp.nat(0),sp.nat(1),sp.nat(2)]).run(sender=admin)

    # scenario.p("Try to re-auction existing stuff")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(0),token_ids=[sp.nat(0),sp.nat(1),sp.nat(2)]).run(sender=admin, valid=False)

    # scenario.p("Bob bids")
    # scenario += auction_house.bid(0).run(sender=bob,amount=sp.mutez(2000000), now=sp.timestamp(0).add_minutes(1))

    # scenario.p("Dan bids")
    # scenario += auction_house.bid(0).run(sender=dan,amount=sp.mutez(3000000), now=sp.timestamp(0).add_minutes(2))

    # scenario.p("Bob rebids")
    # scenario += auction_house.bid(0).run(sender=bob,amount=sp.mutez(4000000), now=sp.timestamp(0).add_minutes(3))

    # scenario.p("Bob withdraws")
    # scenario += auction_house.withdraw(0).run(sender=bob,amount=sp.mutez(2000000), now=sp.timestamp(0).add_minutes(5).add_days(5))
