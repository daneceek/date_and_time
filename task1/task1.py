import datetime 
def calculate_age(date):
    rok, mesic, den = datetime.date.today().timetuple()[:3]
    final_rok = rok - date.year
    mesic = mesic - date.month
    den = date.day - den
    if mesic < 0:
        final_rok -= 1
    if mesic == 0:
        if den < 0:
            final_rok -= 1
    return final_rok