from datetime import datetime
import json


class FileHandler:
    def store_data(self, data):
        currentDay = datetime.now().day
        currentMonth = datetime.now().month
        currentYear = datetime.now().year

        filename = f"{currentDay}_{currentMonth}_{currentYear}"

        with open(f"{filename}.json", "w") as f:
            f.write(json.dumps(data))
        
        return True
