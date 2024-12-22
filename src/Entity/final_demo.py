finalll = [{'bounds': {'northeast': {'lat': 22.5111336, 'lng': 73.4762799},
                       'southwest': {'lat': 22.4970342, 'lng': 73.4707085}}, 'copyrights': 'Map data ©2024', 'legs': [
    {'distance': {'text': '2.0 km', 'value': 1993}, 'duration': {'text': '8 mins', 'value': 464},
     'end_address': '15/1 Narayan-Nagar Shopping Centre, Godhara Rd, Ullas Nagar Society, Halol, Gujarat 389350, India',
     'end_location': {'lat': 22.5111336, 'lng': 73.4707085},
     'start_address': '28, Karim Colony, Vaikunth Society, Halol, Gujarat 389350, India',
     'start_location': {'lat': 22.4970342, 'lng': 73.4762799}, 'steps': [
        {'distance': {'text': '65 m', 'value': 65}, 'duration': {'text': '1 min', 'value': 13},
         'end_location': {'lat': 22.4972406, 'lng': 73.47570259999999}, 'html_instructions': 'Head <b>west</b>',
         'polyline': {'points': 'm}hhCwym_MAF?@CLAJEFMRGJCJAH?P'},
         'start_location': {'lat': 22.4970342, 'lng': 73.4762799}, 'travel_mode': 'DRIVING'},
        {'distance': {'text': '0.4 km', 'value': 381}, 'duration': {'text': '2 mins', 'value': 117},
         'end_location': {'lat': 22.4982795, 'lng': 73.47259439999999},
         'html_instructions': 'Slight <b>right</b><div style="font-size:0.9em">Pass by Badjishah Dargah (on the left)</div>',
         'maneuver': 'turn-slight-right', 'polyline': {
            'points': 'whhCcvm_MURGFIDIBG@GAG?E?I@C@C@EDCBABCLAP?LAHAH?B?BA@CDGDURML?B?DGTCFGPM^EPIXCH?HAPDvB?LDXDRBR?\\?N?FCN'},
         'start_location': {'lat': 22.4972406, 'lng': 73.47570259999999}, 'travel_mode': 'DRIVING'},
        {'distance': {'text': '1.1 km', 'value': 1098}, 'duration': {'text': '4 mins', 'value': 251},
         'end_location': {'lat': 22.5072745, 'lng': 73.471886},
         'html_instructions': 'Turn <b>right</b> at GOODLUCK ACCESSORIES onto <b>Halol - Vadodara Rd</b>/<wbr/><b>Harni - Halol Rd</b><div style="font-size:0.9em">Pass by Boi Atm (on the left)</div>',
         'maneuver': 'turn-right', 'polyline': {
            'points': 'geihCubm_MCJgBo@CAi@OYKQEg@MQCIAIAG?K?A?K?KBKDIDYRi@b@ONa@^}@@q@p@Y\\EDcAfASPMJKFKDE@E@M@O?aBGu@C_AEqAIYAyCScGa@iCWaAK]ESGICGCACCACCCE'},
         'start_location': {'lat': 22.4982795, 'lng': 73.47259439999999}, 'travel_mode': 'DRIVING'},
        {'distance': {'text': '0.4 km', 'value': 449}, 'duration': {'text': '1 min', 'value': 83},
         'end_location': {'lat': 22.5111336, 'lng': 73.4707085},
         'html_instructions': 'Turn <b>left</b> at Satyam Auto Components Ltd onto <b>Halol - Godhra Rd</b>/<wbr/><b>Savli - Halol Rd</b><div style="font-size:0.9em">Pass by GOHIL HEMANGINIBEN MAHENDRASINH (on the left)</div><div style="font-size:0.9em">Destination will be on the right</div>',
         'maneuver': 'turn-left',
         'polyline': {'points': 'm}jhCi~l_Mu@ZUJA@{@\\g@RA@IDm@T[JMD]FYDQBYDcBTgALC@m@D_AHm@F]B_@D'},
         'start_location': {'lat': 22.5072745, 'lng': 73.471886}, 'travel_mode': 'DRIVING'}], 'traffic_speed_entry': [],
     'via_waypoint': []}], 'overview_polyline': {
    'points': 'm}hhCwym_MGb@SZKVAZ]ZSHO?[BONKjAo@l@Kf@e@|ACRBhCNnA?l@CVCJgBo@m@QeBc@g@CM?WHc@Xy@r@kDnDiAlAa@\\]NSBqBGaFU}Ku@kEc@q@MQGMOiCfAaBp@i@Pw@LwEl@_DX}@H'},
            'summary': 'Halol - Vadodara Rd/Harni - Halol Rd', 'warnings': [], 'waypoint_order': []}]


def decode_polyline_text(encoded_polyline: str):
    """
    Generate the latitude and longitude list from the encoded google maps polyline
    This will be used by FrontEnd to draw line in the map to show the route directions
    """
    decoded_lat_lng = []
    index = 0
    lat = 0
    lng = 0

    while index < len(encoded_polyline):
        # read each character of the encoded string
        b, shift, result = 0, 0, 0
        while True:
            # generate the latitude value
            """
            convert the char to ASCII value and adjust with polyline
            encoding scheme(subtract ASCII value with 63).

            extract the lat five digit from the bits and shift them
            then increase the shift by 5 digit.

            if bits is less than 32 bit decimal break the loop no more bits to process.
            """
            b = ord(encoded_polyline[index]) - 63
            index += 1
            result |= (b & 0x1F) << shift
            shift += 5
            if b < 0x20:
                break
        decoded_lat = ~(result >> 1) if (result & 1) != 0 else (result >> 1)
        lat += decoded_lat

        shift, result = 0, 0
        while True:
            # generate the longitude value
            b = ord(encoded_polyline[index]) - 63
            index += 1
            result |= (b & 0x1F) << shift
            shift += 5
            if b < 0x20:
                break
        decoded_lng = ~(result >> 1) if (result & 1) != 0 else (result >> 1)
        lng += decoded_lng

        decoded_lat_lng.append(
            (lat / 1e5,lng / 1e5)
        )

    return decoded_lat_lng

#
# def get_legs_from_the_directions(directions: str) -> list:
#     try:
#         directions_json = json.loads(directions)
#         return directions_json[0]["legs"]
#     except Exception as ex:
#         logger.warning(f"Unable to extract the directions json. {ex}")
#         return []
#
#
# async def format_directions(directions: str) -> MapDirectionsOut:
#     """
#     Format the directions response for the FE with total duration in seconds,
#     distance in meters based on legs.
#
#     Maps polyline is encoded as string in each step decode to latitude and longitude
#     and add them to route.
#     """
#     distance = 0
#     duration = 0
#     route = []
#
#     directions_legs = get_legs_from_the_directions(directions)
#     for leg in directions_legs:
#         distance += leg["distance"]["value"]  # type: ignore
#         duration += leg["duration"]["value"]  # type: ignore
#         for step in leg["steps"]:  # type: ignore
#             encoded_polyline = step["polyline"]["points"]
#             polyline_coords = await decode_polyline_text(
#                 rf"{encoded_polyline}"
#             )
#             route.extend(polyline_coords)
#     return distance, duration, route
