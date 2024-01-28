from flask import Flask, request, jsonify
from service_one_2000watts.model import RoomModel
from service_one_2000watts.controller import HeatingController

app = Flask(__name__)
controller = HeatingController()

def create_routes(app, controller):
    @app.route('/service_one/control', methods=['POST'])
    def control_heating_one():
        command = request.json.get('command')
        if command == 'start':
            data = request.json.get('data')
            room = RoomModel(data['length'], data['width'], data['height'], data['start_temp'], data['target_temp'])
            controller.start_heating(room)
            return jsonify({'message': 'Heating started'})
        elif command == 'stop':
            controller.stop_heating()
            return jsonify({'message': 'Heating stopped'})
        else:
            return jsonify({'error': 'Invalid command'}), 400

    @app.route('/service_one/status', methods=['GET'])
    def get_status_one():
        current_state = controller.current_state()
        current_temp = controller.current_temperature()
        time_remaining = controller.time_remaining()
        energy_consumed = controller.get_energy_consumed()
        total_energy_required = controller.total_energy_to_target()

        return jsonify({
            'status': current_state,
            'current_temperature': current_temp,
            'time_remaining_to_target': time_remaining,
            'total_energy_consumed': energy_consumed,
            'total_energy_to_target': total_energy_required
        })



# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
