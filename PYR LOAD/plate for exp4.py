from opentrons import protocol_api

metadata = {'protocolName': 'PYR plate 2 - exp4', 'author': 'Francel',
            'description': 'LDH activity assay for the forward direction',
            'apiLevel': '2.10'}


def run(protocol: protocol_api.ProtocolContext):
    # loading required labware
    tips_1 = protocol.load_labware('opentrons_96_tiprack_20ul', 4)
    p20 = protocol.load_instrument('p20_single_gen2', mount='left', tip_racks=[tips_1])

    # loading in custom labware:
    source = protocol.load_labware('opentrons_24_tuberack_nest_2ml_snapcap', 8)
    destination = protocol.load_labware('nest_96_wellplate_200ul_flat', 2)

    # load the different mastermix samples:
    # Load Pyr samples: 
    Pyr1 = source['A1']
    Pyr2 = source['A2']
    Pyr3 = source['A3']
    Pyr4 = source['A4']
    Pyr5 = source['B1']
    Pyr6 = source['B2']
    Pyr7 = source['B3']

    # PYR sample destinations: 
    PYR_sample1 = [destination['A4'], destination['A5'], destination['A6']]
    PYR_sample2 = [destination['B4'], destination['B5'], destination['B6']]
    PYR_sample3 = [destination['C4'], destination['C5'], destination['C6']]
    PYR_sample4 = [destination['D4'], destination['D5'], destination['D6']]
    PYR_sample5 = [destination['E4'], destination['E5'], destination['E6']]
    PYR_sample6 = [destination['F4'], destination['F5'], destination['F6']]
    PYR_sample7 = [destination['G4'], destination['G5'], destination['G6']]

    # load Pyr samples:
    # sample 1:
    p20.pick_up_tip(tips_1['B4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for b in range(len(PYR_sample1)):
        p20.aspirate(10, Pyr1)
        p20.dispense(10, PYR_sample1[b])
        p20.blow_out(PYR_sample1[b])
    p20.drop_tip()

    # sample 2:
    p20.pick_up_tip(tips_1['C4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for c in range(len(PYR_sample2)):
        p20.aspirate(10, Pyr2)
        p20.dispense(10, PYR_sample2[c])
        p20.blow_out(PYR_sample2[c])
    p20.drop_tip()

    # sample 3:
    p20.pick_up_tip(tips_1['D4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for d in range(len(PYR_sample3)):
        p20.aspirate(10, Pyr3)
        p20.dispense(10, PYR_sample3[d])
        p20.blow_out(PYR_sample3[d])
    p20.drop_tip()

    # sample 4:
    p20.pick_up_tip(tips_1['E4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for e in range(len(PYR_sample4)):
        p20.aspirate(10, Pyr4)
        p20.dispense(10, PYR_sample4[e])
        p20.blow_out(PYR_sample4[e])
    p20.drop_tip()

    # sample 5:
    p20.pick_up_tip(tips_1['F4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for g in range(len(PYR_sample5)):
        p20.aspirate(10, Pyr5)
        p20.dispense(10, PYR_sample5[g])
        p20.blow_out(PYR_sample5[g])
    p20.drop_tip()

    # sample 6:
    p20.pick_up_tip(tips_1['G4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for i in range(len(PYR_sample6)):
        p20.aspirate(10, Pyr6)
        p20.dispense(10, PYR_sample6[i])
        p20.blow_out(PYR_sample6[i])
    p20.drop_tip()

    # sample 7
    p20.pick_up_tip(tips_1['H4'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for j in range(len(PYR_sample7)):
        p20.aspirate(10, Pyr7)
        p20.dispense(10, PYR_sample7[j])
        p20.blow_out(PYR_sample7[j])
    p20.drop_tip()
