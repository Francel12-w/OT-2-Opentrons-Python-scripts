from opentrons import protocol_api

metadata = {'protocolName': 'lysate for plate 1 - exp7', 'author': 'Francel',
            'description': 'LDH activity assay for the forward direction',
            'apiLevel': '2.10'}


def run(protocol: protocol_api.ProtocolContext):
    # loading required labware
    tips_1 = protocol.load_labware('opentrons_96_tiprack_20ul', 4)
    p20 = protocol.load_instrument('p20_single_gen2', mount='left', tip_racks=[tips_1])

    # loading in custom labware:
    source = protocol.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 3)
    destination = protocol.load_labware('nest_96_wellplate_200ul_flat', 2)

    # load the different mastermix samples:
    lysate = source['A1']

    # loading Plate 2 FOR EXP7:
    # lysate destination:
    lysate_plate2 = [destination['F12'], destination['G10'], destination['G11'], destination['G12']]

    # load lysate:
    # sample1
    p20.pick_up_tip(tips_1['A7'])
    p20.flow_rate.aspirate = 300
    p20.flow_rate.dispense = 300
    p20.flow_rate.blow_out = 100
    p20.well_bottom_clearance.aspirate = 7
    p20.well_bottom_clearance.dispense = -0.7
    for a in range(len(lysate_plate2)):
        p20.aspirate(10, lysate)
        p20.dispense(10, lysate_plate2[a])
        p20.blow_out(lysate_plate2[a])
    p20.drop_tip()
