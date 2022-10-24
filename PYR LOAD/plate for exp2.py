from opentrons import protocol_api

metadata = {'protocolName': 'lysate for plate 2 - exp2', 'author': 'Francel',
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
    # loading Plate 1 FOR EXP1:

    # PYR sample destinations: 
    PYR_sample1 = [destination['A1'], destination['A2'], destination['A3']]
    PYR_sample2 = [destination['B1'], destination['B2'], destination['B3']]
    PYR_sample3 = [destination['C1'], destination['C2'], destination['C3']]
    PYR_sample4 = [destination['D1'], destination['D2'], destination['D3']]
    PYR_sample5 = [destination['E1'], destination['E2'], destination['E3']]
    PYR_sample6 = [destination['F1'], destination['F2'], destination['F3']]
    PYR_sample7 = [destination['G1'], destination['G2'], destination['G3']]

    # load lysate:
    # sample
    # load Pyr samples:
    # sample 1:
    p20.pick_up_tip(tips_1['B2'])
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
    p20.pick_up_tip(tips_1['C2'])
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
    p20.pick_up_tip(tips_1['D2'])
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
    p20.pick_up_tip(tips_1['E2'])
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
    p20.pick_up_tip(tips_1['F2'])
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
    p20.pick_up_tip(tips_1['G2'])
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
    p20.pick_up_tip(tips_1['H2'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.blow_out = 100
    p20.flow_rate.dispense = 300
    p20.well_bottom_clearance.dispense = 10
    for j in range(len(PYR_sample7)):
        p20.aspirate(10, Pyr7)
        p20.dispense(10, PYR_sample7[j])
        p20.blow_out(PYR_sample7[j])
    p20.drop_tip()
