import utils.file_reader as file_reader

input_file_path = "input/input.txt"

class SubmarineParameters:
    def __init__(self, gamma_rate, epsilon_rate, oxygen_gen_rating, co2_scrubber_rating):
        self.gamma_rate = gamma_rate
        self.epsilon_rate = epsilon_rate
        self.oxygen_gen_rating = oxygen_gen_rating
        self.co2_scrubber_rating = co2_scrubber_rating
    
    @staticmethod
    def from_binary(gamma_rate_binary, epsilon_rate_binary, oxygen_gen_rating_binary, co2_scrubber_rating_binary):
        gamma_rate = int(gamma_rate_binary, 2)
        epsilon_rate = int(epsilon_rate_binary, 2)
        oxygen_gen_rating = int(oxygen_gen_rating_binary, 2)
        co2_scrubber_rating = int(co2_scrubber_rating_binary, 2)
        return SubmarineParameters(gamma_rate, epsilon_rate, co2_scrubber_rating, oxygen_gen_rating)
        
    def get_power_consumption(self):
        return self.gamma_rate * self.epsilon_rate

    def get_life_support_rating(self):
        return self.oxygen_gen_rating * self.co2_scrubber_rating

def decode_life_support_rating(input_list, rating_name):
    list_under_scope = input_list
    for i in range(len(input_list[0])):
        zero_count = 0
        one_count = 0
        zero_list = []
        one_list = []
        if (len(list_under_scope) == 1):
            break
        for j in range(len(list_under_scope)):
            if list_under_scope[j][i] == '0':
                zero_count += 1
                zero_list.append(list_under_scope[j])
            elif list_under_scope[j][i] == '1':
                one_count += 1
                one_list.append(list_under_scope[j])
        if rating_name == "oxygen_gen_rating":
            if zero_count > one_count:
                list_under_scope = zero_list
            else:
                list_under_scope = one_list
        elif rating_name == "co2_scrubber_rating":
            if zero_count > one_count:
                list_under_scope = one_list
            else:
                list_under_scope = zero_list
        else:
            raise Exception("Unexpected rating_name: " + rating_name)
        
    if (len(list_under_scope) > 1):
        raise Exception("Could not find " + rating_name) 
    
    return list_under_scope[0]


if __name__ == '__main__':
    input_lines = file_reader.read_string_file(input_file_path)
    input_count = len(input_lines)

    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(input_lines[0]) - 1):
        zero_count = 0
        one_count = 0
        for j in range(input_count):
            if input_lines[j][i] == '0':
                zero_count += 1
            elif input_lines[j][i] == '1':
                one_count += 1
            else:
                raise Exception("Unexpected input: " + input_lines[j])
        if zero_count > one_count:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    oxygen_gen_rating = decode_life_support_rating(input_lines, "oxygen_gen_rating")
    co2_scrubber_rating = decode_life_support_rating(input_lines, "co2_scrubber_rating")

    submarineParameters = SubmarineParameters.from_binary(gamma_rate, epsilon_rate, oxygen_gen_rating, co2_scrubber_rating)

    print("Silver  -->  power_consumption:", submarineParameters.get_power_consumption())
    print("Gold  -->  life_support_rating:", submarineParameters.get_life_support_rating())
