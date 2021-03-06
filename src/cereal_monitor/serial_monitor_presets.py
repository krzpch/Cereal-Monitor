import json

class MonitorPresets():
    saved_presets_path = '.\\saved_presets.json'
    data = {}

    def __init__(self):
        try:
            with open(self.saved_presets_path, 'r') as infile:
                self.data = json.load(infile)
        except FileNotFoundError:
            self.data['presets'] = []

    def save_preset(self, name, port, baudrate, parity, stopbits, bytesize, sfc, rtscts, dsrdtr):
        newdata = {
            'name': name,
            'port': port,
            'baudrate': baudrate,
            'parity': parity,
            'stopbits': stopbits,
            'bytesize': bytesize,
            'sfc': sfc,
            'rtscts': rtscts,
            'dsrdtr': dsrdtr
        }

        self.data['presets'].append(newdata)

        with open(self.saved_presets_path, 'w') as outfile:
            json.dump(self.data, outfile, indent=4)

    def load_preset(self, name):
        for preset in self.data['presets']:
            if name == preset['name']:
                return preset['port'], preset['baudrate'], preset['parity'], preset['stopbits'], preset['bytesize'], preset['sfc'], preset['rtscts'], preset['dsrdtr']
        
    def delete_preset(self, name):
        i = 0
        for preset in self.data['presets']:
            if name == preset['name']:
                self.data['presets'].pop(i)
                with open(self.saved_presets_path, 'w') as outfile:
                    json.dump(self.data, outfile, indent=4)
            i = i + 1
