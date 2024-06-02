from parameters import Parameters

class Intensity:
    def __init__(self):
        self.parameters = Parameters(file_name='parameters.json')
        self.idx_intensity = 0
        self.lambda_intensity_ratio = self.parameters.lambda_intensity_ratio[self.idx_intensity]
        self.service_time = self.parameters.lambda_intensity_time[self.idx_intensity] * self.parameters.hour2milisek



    def change_lambda_intensity(self):
        self.idx_intensity = (self.idx_intensity + 1) % len(self.parameters.lambda_intensity_ratio)
        self.lambda_intensity_ratio = self.parameters.lambda_intensity_ratio[self.idx_intensity]
        self.service_time = self.parameters.lambda_intensity_time[self.idx_intensity] * self.parameters.hour2milisek
