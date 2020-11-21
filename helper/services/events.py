from helper.dao.events import EventsDao

Events = {
    "LANDSCAPE": "Landscape Photography.",
    "WILDLIFE": "wildlife Photographer",
    "AERIAL": "Aerial Photography",
    "SPORT": "Sports/Action Photography",
    "PORTRAIT": "portrait Photography",
    "ARCHITECTURAL": "Architectural Photography",
    "WEDDING": "Wedding Photography",
    "EVENT": "Event Photography",
    "FASHION": "Fashion Photography",
    "MACRO": "Macro Photography",
    "BABY": "Baby Photography",
    "FAMILY": "Family Photography",
    "ABSTRACT": "Abstract Photography",
    "BEAUTY": "Beauty Photography",
    "BIRD": "Bird Photography",
    "BODYSCAPE": "Bodyscape Photography",
    "CANDID": "Candid Photography",
    "CONCEPTUAL": "Conceptual Photography",
    "FIREWORK": "Firework Photography",
    "FOOD": "Food Photography",
    "HI-SPEED": "Hi Speed Photography",
    "INFRARED": "Infrared Photography",
    "LOMO": "Lomo Photography",
    "LONG-EXPOSURE": "Long Exposure Photography",
    "MICRO": "Micro Photography",
    "MOBILE": "Mobile Photography",
    "MODELING": "Modeling Photography",
    "NATURE": "Nature Photography",
    "NIGHT": "Night Photography",
    "PAST-AND-PRESENT": "Past And Present Photography",
    "RAIN": "Rain Photography",
    "REAL-ESTATE": " Real Estate Photography",
    "STREET": "Street Photography",
    "TIME-LAPSE": "Time Lapse Photography",
    "TRAVEL": "Travel Photography",
    "UNDERWATER": "Underwater Photography",
    "VEHICLE": "Vehicle Photography",
    "VINTAGE": "Vintage Photography"
}
class EventService:

    def add_events(self, *args, **options):
        for key, val in Events.items():
            events_dao_obj =  EventsDao()
            events_dao_obj.add_events(name=val, code=key)
            # event_category, created = EventCategory.objects.get_or_create(code=key, title=val)
