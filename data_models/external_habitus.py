from collections import defaultdict


class HabitusFullDict:
    def __init__(self, skin_thickness=None, skin_color=None, skin_birthmarks=None, skin_burnt=None, makeup=None,
                 right_ear=None, left_ear=None, forehead=None, expression_lines=None, piercings=None, right_eyelid=None,
                 left_eyelid=None, right_eye=None, left_eye=None, nose=None, mouth=None, teeth=None, tongue=None,
                 jaw=None, facial_hair=None, hair=None, neck=None, body=None, right_arm=None, left_arm=None,
                 right_leg=None, left_leg=None, right_foot=None, left_foot=None):
        self.my_dict = {'skin_thickness': skin_thickness, 'skin_color': skin_color,
                        'skin_birthmarks': skin_birthmarks, 'skin_burnt': skin_burnt, 'makeup': makeup,
                        'right_ear': right_ear, 'left_ear': left_ear, 'forehead': forehead,
                        'expression_lines': expression_lines, 'piercings': piercings, 'right_eyelid': right_eyelid,
                        'left_eyelid': left_eyelid, 'right_eye': right_eye, 'left_eye': left_eye, 'nose': nose,
                        'mouth': mouth, 'teeth' : teeth, 'tongue': tongue, 'jaw': jaw, 'facial_hair': facial_hair,
                        'hair': hair, 'neck': neck, 'body': body, 'right_arm':  right_arm, 'left_arm': left_arm,
                        'right_leg': right_leg, 'left_leg': left_leg, 'right_foot': right_foot,
                        'left_foot': left_foot}

    def update_data(self, skin_thickness=None, skin_color=None, skin_birthmarks=None, skin_burnt=None, makeup=None,
                    right_ear=None, left_ear=None, forehead=None, expression_lines=None, piercings=None, right_eyelid=None,
                    left_eyelid=None, right_eye=None, left_eye=None, nose=None, mouth=None, teeth=None, tongue=None,
                    jaw=None, facial_hair=None, hair=None, neck=None, body=None, right_arm=None, left_arm=None,
                    right_leg=None, left_leg=None, right_foot=None, left_foot=None):
        self.my_dict = {'skin_thickness': skin_thickness, 'skin_color': skin_color,
                        'skin_birthmarks': skin_birthmarks, 'skin_burnt': skin_burnt, 'makeup': makeup,
                        'right_ear': right_ear, 'left_ear': left_ear, 'forehead': forehead,
                        'expression_lines': expression_lines, 'piercings': piercings, 'right_eyelid': right_eyelid,
                        'left_eyelid': left_eyelid, 'right_eye': right_eye, 'left_eye': left_eye, 'nose': nose,
                        'mouth': mouth, 'teeth' : teeth, 'tongue': tongue, 'jaw': jaw, 'facial_hair': facial_hair,
                        'hair': hair, 'neck': neck, 'body': body, 'right_arm':  right_arm, 'left_arm': left_arm,
                        'right_leg': right_leg, 'left_leg': left_leg, 'right_foot': right_foot,
                        'left_foot': left_foot}


class ExternalHabitusObj(defaultdict):
    def __init__(self, skin=None, birthmarks=None, head=None, forehead=None, eyelids=None, r_eye=None, l_eye=None,
                 nose=None, r_ear=None, l_ear=None, mouth=None, teeth=None, tongue=None, jaw=None, facial_hair=None,
                 hair=None, neck=None, body=None, r_arm=None, l_arm=None, r_foot=None, l_foot=None, r_hand=None,
                 l_hand=None, r_leg=None, l_leg=None):
        super().__init__()
        self['skin'] = skin if skin is not None else Skin()
        self['birthmarks'] = birthmarks if birthmarks is not None else Birthmarks()
        self['head'] = head if head is not None else Head()
        self['forehead'] = forehead if forehead is not None else Forehead()
        self['eyelids'] = eyelids if eyelids is not None else Eyelids()
        self['r_eye'] = r_eye if r_eye is not None else Eye()
        self['l_eye'] = l_eye if l_eye is not None else Eye(False)
        self['nose'] = nose if nose is not None else Nose()
        self['r_ear'] = r_ear if r_ear is not None else Ear()
        self['l_ear'] = l_ear if l_ear is not None else Ear(False)
        self['mouth'] = mouth if mouth is not None else Mouth()
        self['teeth'] = teeth if teeth is not None else Teeth()
        self['tongue'] = tongue if tongue is not None else Tongue()
        self['jaw'] = jaw if jaw is not None else Jaw()
        self['facial_hair'] = facial_hair if facial_hair is not None else FacialHair()
        self['hair'] = hair if hair is not None else Hair()
        self['neck'] = neck if neck is not None else Neck()
        self['body'] = body if body is not None else Body()
        self['r_arm'] = r_arm if r_arm is not None else Arm()
        self['l_arm'] = l_arm if l_arm is not None else Arm(False)
        self['r_foot'] = r_foot if r_foot is not None else Foot()
        self['l_foot'] = l_foot if l_foot is not None else Foot(False)
        self['r_hand'] = r_hand if r_hand is not None else Hand()
        self['l_hand'] = l_hand if l_hand is not None else Hand(False)
        self['r_leg'] = r_leg if r_leg is not None else Leg()
        self['l_leg'] = l_leg if l_leg is not None else Leg(False)


class ExternalHabitusFullDict(defaultdict):
    def __init__(self, external_habitus_obj=None):
        super().__init__()
        if external_habitus_obj is not None:
            self.extractor(external_habitus_obj.keys())

    def extractor(self, obj):
        print(obj)
        for key in list(obj):
            if key is not None:
                #   Unpack composed parts (arm, hand, leg, foot)
                if type(obj) in [type(Arm()), type(Hand()), type(Leg()), type(Foot())]:
                    #   Unpack composed parts (hand)
                    if isinstance(obj, type(Hand())):
                        for element in obj.values():
                            if isinstance(element, type(Finger())):
                                for finger in element.keys():
                                    print(element[finger])
                    else:
                        print()


class Skin(defaultdict):
    def __init__(self, thickness=None, color=None, birthmarks=None, burnt=False):
        super().__init__()
        self['thickness'] = thickness
        self['color'] = color
        self['birthmarks'] = birthmarks
        self['burnt'] = burnt


class Birthmarks(defaultdict):
    def __init__(self, existence=None):
        super().__init__()
        self['existence'] = existence


class Head(defaultdict):
    def __init__(self, makeup=None, right_ear=None, left_ear=None):
        super().__init__()
        self['makeup'] = makeup
        self['right_ear'] = right_ear
        self['left_ear'] = left_ear


class Forehead(defaultdict):
    def __init__(self, size=None, expression_lines=None, piercings=False, jewelry=False):
        super().__init__()
        self['size'] = size
        self['expression_lines'] = expression_lines
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Eyelids(defaultdict):
    def __init__(self, deformities=None, piercings=False, jewelry=False):
        super().__init__()
        self['deformities'] = deformities
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Eye(defaultdict):
    def __init__(self, right=True, shape=None, size=None, color=None):
        super().__init__()
        self['right'] = right
        self['shape'] = shape
        self['size'] = size
        self['color'] = color


class Nose(defaultdict):
    def __init__(self, size=None, deformities=None, piercings=False, jewelry=False):
        super().__init__()
        self['size'] = size
        self['deformities'] = deformities
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Ear(defaultdict):
    def __init__(self, right=True, size=None, deformities=None, piercings=False, jewelry=False):
        super().__init__()
        self['right'] = right
        self['size'] = size
        self['deformities'] = deformities
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Mouth(defaultdict):
    def __init__(self, size=None, deformities=None, piercings=False, jewelry=False):
        super().__init__()
        self['size'] = size
        self['deformities'] = deformities
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Teeth(defaultdict):
    def __init__(self, size=None, color=None, orientation=None, missing=None):
        super().__init__()
        self['size'] = size
        self['color'] = color
        self['orientation'] = orientation
        self['missing'] = missing


class Tongue(defaultdict):
    def __init__(self, length=None, width=None, color=None, missing=None, deformities=None, burnt_marks=False,
                 piercings=False, jewelry=False):
        super().__init__()
        self['length'] = length
        self['width'] = width
        self['color'] = color
        self['missing'] = missing
        self['deformities'] = deformities
        self['burnt_marks'] = burnt_marks
        self['piercings'] = piercings
        self['jewelry'] = jewelry


class Jaw(defaultdict):
    def __init__(self, shape=None):
        super().__init__()
        self['shape'] = shape


class FacialHair(defaultdict):
    def __init__(self, eyebrows=None, eyelashes=None, moustache=None, beard=None, color=None):
        super().__init__()
        self['eyebrows'] = eyebrows
        self['eyelashes'] = eyelashes
        self['moustache'] = moustache
        self['beard'] = beard
        self['color'] = color


class Hair(defaultdict):
    def __init__(self, size=None, color=None, baldness=False):
        super().__init__()
        self['size'] = size
        self['color'] = color
        self['baldness'] = baldness


class Neck(defaultdict):
    def __init__(self, length=None, width=None, jewelry=False):
        super().__init__()
        self['length'] = length
        self['width'] = width
        self['jewelry'] = jewelry


class Body(defaultdict):
    def __init__(self, thorax=None, abdomen=None, pelvis=None):
        super().__init__()
        self['thorax'] = thorax
        self['abdomen'] = abdomen
        self['pelvis'] = pelvis


class Arm(defaultdict):
    def __init__(self, right=True, missing=False, length=None, width=None, strength=None, hair=None):
        super().__init__()
        self['right'] = right
        self['missing'] = missing
        self['length'] = length
        self['width'] = width
        self['strength'] = strength
        self['hair'] = hair


class Foot(defaultdict):
    def __init__(self, right=True, missing=False):
        super().__init__()
        self['right'] = right
        self['missing'] = missing


class Hand(defaultdict):
    def __init__(self, right=True, thumb=None, index=None, middle=None, ring=None, pinky=None, nail_length=None):
        super().__init__()
        self['right'] = right
        self['thumb'] = thumb if thumb is not None else Finger()
        self['index'] = index if index is not None else Finger()
        self['middle'] = middle if middle is not None else Finger()
        self['ring'] = ring if ring is not None else Finger()
        self['pinky'] = pinky if pinky is not None else Finger()
        self['nail_length'] = nail_length


class Finger(defaultdict):
    def __init__(self, present=True, severed=False, deformed=False):
        super().__init__()
        self['present'] = present
        self['severed'] = severed
        self['deformed'] = deformed


class Leg(defaultdict):
    def __init__(self, right=True, present=True, severed=False, deformed=False, longest=None):
        super().__init__()
        self['right'] = right
        self['present'] = present
        self['severed'] = severed
        self['deformed'] = deformed
        self['longest'] = longest
