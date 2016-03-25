from synchrophasor.pmu import Pmu


pmu = Pmu(port=1410, ip="127.0.0.1")

pmu.set_configuration()  # This will load default PMU configuration specified in IEEE C37.118.2 - Annex D (Table D.2)
pmu.set_header()  # This will load default header message "Hello I'm tinyPMU!"

pmu.run()  # PMU starts listening for incoming connections

while True:
    if pmu.clients:  # Check if there is any connected PDCs
        pmu.send(pmu.ieee_data_sample)  # Sending sample data frame specified in IEEE C37.118.2 - Annex D (Table D.1)

pmu.join()
