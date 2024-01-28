from service_one_2000watts.model import RoomModel
import time

class HeatingController:
    def __init__(self, power_rating=2000):
        self.power_rating = power_rating
        self.is_heating = False
        self.start_time = None
        self.heating_duration = None
        self.current_room_model = None
        self.total_energy_consumed = 0  # in kilowatt-hours (kWh)

    def start_heating(self, room_model):
        self.current_room_model = room_model
        self.heating_duration = self.calculate_heating_time(room_model)
        self.start_time = time.time()
        self.is_heating = True

    def stop_heating(self):
        self.is_heating = False
        self._update_energy_consumed()
        self.start_time = None
        self.heating_duration = None

    def calculate_heating_time(self, room_model):
        heating_time = (room_model.target_temp - room_model.start_temp) * room_model.room_volume() / self.power_rating
        return max(heating_time, 0)

    def _update_energy_consumed(self):
        if self.start_time:
            elapsed_time = time.time() - self.start_time
            self.total_energy_consumed += (self.power_rating / 1000) * (elapsed_time / 3600)  # Convert to kWh

    def current_state(self):
        return "on" if self.is_heating else "off"

    def current_temperature(self):
        if not self.is_heating or not self.current_room_model:
            return None
        elapsed_time = time.time() - self.start_time
        temperature_increase = (elapsed_time / 3600) * (self.power_rating / self.current_room_model.room_volume())
        return min(self.current_room_model.start_temp + temperature_increase, self.current_room_model.target_temp)

    def time_remaining(self):
        if not self.is_heating or not self.heating_duration:
            return None
        elapsed_time = time.time() - self.start_time
        remaining_time = max(self.heating_duration - (elapsed_time / 3600), 0)
        return remaining_time

    def total_energy_to_target(self):
        return (self.heating_duration * (self.power_rating / 1000))  # Convert to kWh

    def get_energy_consumed(self):
        self._update_energy_consumed()
        return self.total_energy_consumed