class RoomModel:
    def __init__(self, length, width, height, start_temp, target_temp):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Room dimensions must be positive values.")
        if start_temp >= target_temp:
            raise ValueError("Target temperature must be greater than the start temperature.")

        self.length = length
        self.width = width
        self.height = height
        self.start_temp = start_temp
        self.target_temp = target_temp

    def room_volume(self):
        return self.length * self.width * self.height

    def __str__(self):
        return f"Room Size: {self.room_volume()} cubic meters, Start Temp: {self.start_temp}°C, Target Temp: {self.target_temp}°C"
