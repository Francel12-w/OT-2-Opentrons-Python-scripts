from opentrons import protocol_api

# define metadata
metadata = {'protocolName': 'NADH sample prep', 'author': 'Francel',
            'description': 'GAPDH activity assay for the forward direction',
            'apiLevel': '2.0'}


def run(protocol: protocol_api.ProtocolContext):
    # load labware
    tips_3 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    p300 = protocol.load_instrument('p300_single', mount='left', tip_racks=[tips_3])

    # loading in custom labware:
    source = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    destination = protocol.load_labware('opentrons_15_tuberack_nest_15ml_conical', 10)

    # Sample layout:
    NADH_stock = source['A1']
    MgCl2_stock = source['A2']

    # There are in total 7 mastermix samples but due to insufficient space only 4 samples at a time can be prepared
    NADH_sample1 = [destination['A1']]
    NADH_sample2 = [destination['A2']]
    NADH_sample3 = [destination['A3']]
    NADH_sample4 = [destination['A4']]
    NADH_sample5 = [destination['B1']]
    NADH_sample6 = [destination['B2']]
    NADH_sample7 = [destination['B3']]

    MgCl2_add = [destination['A1'], destination['A2'], destination['A3'], destination['A4'], destination['B1'],
                 destination['B2'], destination['B3']]

    # First load all the NAD into the falcon tubes:
    # sample1:
    p300.pick_up_tip(tips_3['C1'])
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 12
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for u in range(len(NADH_sample1)):
        p300.aspirate(300, NADH_stock)
        p300.dispense(300, NADH_sample1[u])
        p300.blow_out(NADH_sample1[u])

    # sample2:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 10
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for v in range(len(NADH_sample2)):
        p300.aspirate(250, NADH_stock)
        p300.dispense(250, NADH_sample2[v])
        p300.blow_out(NADH_sample2[v])

    # sample3:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 8
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for p in range(len(NADH_sample3)):
        p300.aspirate(200, NADH_stock)
        p300.dispense(200, NADH_sample3[p])
        p300.blow_out(NADH_sample3[p])

    # sample4:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 6
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for z in range(len(NADH_sample4)):
        p300.aspirate(50, NADH_stock)
        p300.dispense(50, NADH_sample4[z])
        p300.blow_out(NADH_sample4[z])

    # sample5:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 5
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for e in range(len(NADH_sample5)):
        p300.aspirate(40, NADH_stock)
        p300.dispense(40, NADH_sample5[e])
        p300.blow_out(NADH_sample5[e])

    # sample6:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 4
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for g in range(len(NADH_sample6)):
        p300.aspirate(30, NADH_stock)
        p300.dispense(30, NADH_sample6[g])
        p300.blow_out(NADH_sample6[g])

    # sample7:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 4
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 50
    for h in range(len(NADH_sample7)):
        p300.aspirate(25, NADH_stock)
        p300.dispense(25, NADH_sample7[h])
        p300.blow_out(NADH_sample7[h])
    p300.drop_tip()

    # load all the PIPES (due to large volumes add manually):
    # sample 1: final volume = 1950uL
    # sample 2: final volume = 2000uL
    # sample 3: final volume = 2050uL
    # sample 4: final volume = 2200uL
    # sample 5: final volume = 2210uL
    # sample 6: final volume = 2220uL
    # sample 7: final volume = 2225uL

    # Next load MgCl2 to each tube:
    p300.pick_up_tip(tips_3['D1'])
    for x in range(len(MgCl2_add)):
        p300.flow_rate.aspirate = 300
        p300.flow_rate.dispense = 300
        p300.well_bottom_clearance.aspirate = 20
        p300.well_bottom_clearance.dispense = 60
        p300.aspirate(150, MgCl2_stock)
        p300.dispense(150, MgCl2_add[x])
        p300.blow_out(MgCl2_add[x])
    p300.drop_tip()
