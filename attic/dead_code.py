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

        # scenario.p("Try to re-auction existing stuff")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(0),token_ids=[sp.nat(0),sp.nat(1),sp.nat(2)]).run(sender=admin, valid=False)

    # scenario.p("Try large token id")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(123),token_ids=[sp.nat(1689)]).run(sender=admin)

    # scenario.p("Try too large token id")
    # scenario += fa2.initial_auction(auction_id_start=sp.nat(124),token_ids=[sp.nat(1690)]).run(sender=admin, valid=False)


        # TODO replace initial_auction with a mint function that can only be called by an admin
    # + entry point for admin to change their own address (two steps, accept)
    # pass the metadata + royalty info when minting
    # push royalty param to the auction house
    # @sp.entry_point
    # def initial_auction(self, batch_initial_auction):
    #     auction_id_runner = sp.local('auction_id_runner', batch_initial_auction.auction_id_start)
    #     sp.for token_id in batch_initial_auction.token_ids:
    #         sp.verify((~self.data.total_supply.contains(token_id)), message = FA2ErrorMessage.NOT_OWNER)
    #         sp.verify(token_id<=MAXIMAL_TOKEN_ID, message = FA2ErrorMessage.NOT_OWNER)
    #         to_user = LedgerKey.make(sp.self_address, token_id)
    #         self.data.ledger[to_user] = sp.nat(1)
    #         self.data.total_supply[token_id] = sp.nat(1)
    #         operator_user = AllowanceKey.make(sp.self_address, self.data.initial_auction_house_address, token_id)
    #         self.data.allowances[operator_user] = True
    #         auction_house = sp.contract(AuctionCreateRequest.get_type(), self.data.initial_auction_house_address, entry_point = "create_auction").open_some()
    #         auction_create_request = sp.record(
    #             auction_id=auction_id_runner.value,
    #             token_address=sp.self_address,
    #             token_id=token_id,
    #             token_amount=sp.nat(1),
    #             end_timestamp=sp.now.add_hours(INITIAL_AUCTION_DURATION),
    #             bid_amount=INITIAL_BID
    #         )
    #         sp.set_type_expr(auction_create_request, AuctionCreateRequest.get_type())
    #         sp.transfer(auction_create_request, sp.mutez(0), auction_house)
    #         auction_id_runner.value += 1
