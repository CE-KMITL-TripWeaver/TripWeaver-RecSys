import random as rd

'''
based on persona 'https://www.canva.com/design/DAF3tu3oqLc/TJPmfsXlYo01Z8EGpdHqfA/edit?utm_content=DAF3tu3oqLc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton'

page 9: love diving
page 13: love art
page 14: love shopping    
page *: a family man, have kid

'''

def create_user_persona_nature() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_temple_historical() -> list[dict]:
    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_adventure() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(3, 4), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_art() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_beach() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_family_friendly() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt

def create_user_persona_citylife() -> list[dict]:

    res_preference_prompt = [
        {"name": "Nature & Outdoors", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy spending time in nature, such as mountains, beaches, national parks, waterfalls, forests, or riversides?"},

        {"name": "Cultural & Historical", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy exploring cultural and historical attractions like temples, museums, landmarks, or monuments?"},

        {"name": "Urban & City Life", "score": rd.randint(4, 5), 
        "question": "On a scale of 0-5, how much do you enjoy urban experiences like shopping, walking streets, cityscapes, markets, or nightlife?"},

        {"name": "Relaxation & Meditation", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy relaxing activities like meditation, cozy snuggles, or peaceful foggy settings?"},

        {"name": "Adventure & Activities", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy adventure activities like hiking, cycling, camping, or diving?"},

        {"name": "Wildlife & Family-Friendly", "score": rd.randint(0, 2), 
        "question": "On a scale of 0-5, how much do you enjoy visiting family-friendly places like zoos or waterparks with activities suitable for kids?"},

        {"name": "Arts & Architecture", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy exploring art and architecture during your travels?"},

        {"name": "Small Villages & Rural Life", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting small villages and experiencing rural life?"},

        {"name": "Islands & Beaches", "score": rd.randint(0, 3), 
        "question": "On a scale of 0-5, how much do you enjoy visiting islands and spending time on beaches?"},
    ]

    return res_preference_prompt
