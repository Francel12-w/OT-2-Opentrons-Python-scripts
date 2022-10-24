from opentrons import protocol_api

# define metadata
metadata = {'protocolName': 'PYR sample prep', 'author': 'Francel',
            'description': 'LDH activity assay for the forward direction',
            'apiLevel': '2.12'}


def run(protocol: protocol_api.ProtocolContext):
    # load required labware
    tips_1 = protocol.load_labware('opentrons_96_tiprack_300ul', 1)
    p300 = protocol.load_instrument('p300_single_gen2', mount='left', tip_racks=[tips_1])

    # loading in the specific labware and locations:
    source = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)
    destination = protocol.load_labware('opentrons_24_tuberack_eppendorf_2ml_safelock_snapcap', 3)

    # Load Sample layout:
    PYR_stock = source['A1']
    PIPES_buffer = source['A3']

    sample1 = [destination['A1']]
    sample2 = [destination['A2']]
    sample3 = [destination['A3']]
    sample4 = [destination['A4']]
    sample5 = [destination['B1']]
    sample6 = [destination['B2']]
    sample7 = [destination['B3']]

    # First add all the different GAP volumes (using the same tip):
    # sample1:
    # VOLUME OF PYR STOCK = 5mL which is equivalent to 30mm
    p300.pick_up_tip(tips_1['A1'])
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 25  # this command ensures that the tip does not touch the bottom of the falcon tube!
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for i in range(len(sample1)):
        p300.aspirate(300, PYR_stock)
        p300.dispense(300, sample1[i])
        p300.blow_out(sample1[i])

    # sample2:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 20
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for j in range(len(sample2)):
        p300.aspirate(280, PYR_stock)
        p300.dispense(280, sample2[j])
        p300.blow_out(sample2[j])

    # sample3:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 18
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for k in range(len(sample3)):
        p300.aspirate(200, PYR_stock)
        p300.dispense(200, sample3[k])
        p300.blow_out(sample3[k])

    # sample4:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 15
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for n in range(len(sample4)):
        p300.aspirate(100, PYR_stock)
        p300.dispense(100, sample4[n])
        p300.blow_out(sample4[n])

    # sample5:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 14
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for m in range(len(sample5)):
        p300.aspirate(50, PYR_stock)
        p300.dispense(50, sample5[m])
        p300.blow_out(sample5[m])

    # sample6:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 12
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for r in range(len(sample6)):
        p300.aspirate(33, PYR_stock)
        p300.dispense(33, sample6[r])
        p300.blow_out(sample6[r])

    # sample7:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 10
    p300.flow_rate.dispense = 300
    p300.well_bottom_clearance.dispense = 20
    for p in range(len(sample7)):
        p300.aspirate(25, PYR_stock)
        p300.dispense(25, sample7[p])
        p300.blow_out(sample7[p])
    p300.drop_tip()

    # Secondly add all pipes buffers (same tip without toughing the liquid):
    # sample 2:
    p300.pick_up_tip(tips_1['B1'])
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 70
    p300.well_bottom_clearance.dispense = 20
    for a in range(len(sample2)):
        p300.aspirate(20, PIPES_buffer)
        p300.dispense(20, sample2[a])
        p300.blow_out(sample2[a])

    # sample 3:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 67
    p300.well_bottom_clearance.dispense = 20
    for b in range(len(sample3)):
        p300.aspirate(100, PIPES_buffer)
        p300.dispense(100, sample3[b])
        p300.blow_out(sample3[b])

    # sample 4:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 64
    p300.well_bottom_clearance.dispense = 20
    for c in range(len(sample4)):
        p300.aspirate(200, PIPES_buffer)
        p300.dispense(200, sample4[c])
        p300.blow_out(sample4[c])

    # sample 5:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 60
    p300.well_bottom_clearance.dispense = 20
    for d in range(len(sample5)):
        p300.aspirate(250, PIPES_buffer)
        p300.dispense(250, sample5[d])
        p300.blow_out(sample5[d])

    # sample 6
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 60
    p300.well_bottom_clearance.dispense = 20
    for e in range(len(sample6)):
        p300.aspirate(267, PIPES_buffer)
        p300.dispense(267, sample6[e])
        p300.blow_out(sample6[e])

    # sample 7:
    p300.flow_rate.aspirate = 300
    p300.well_bottom_clearance.aspirate = 59
    p300.well_bottom_clearance.dispense = 20
    for g in range(len(sample7)):
        p300.aspirate(275, PIPES_buffer)
        p300.dispense(275, sample7[g])
        p300.blow_out(sample7[g])
    p300.drop_tip()



