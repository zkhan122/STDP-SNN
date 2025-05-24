import matplotlib.pyplot as plt
import nest.voltage_trace

nest.set_verbosity("M_WARNING")

nest.ResetKernel()

neuron = nest.Create("iaf_psc_alpha")
print(neuron)


voltmeter = nest.Create("voltmeter")

nest.SetStatus(neuron, "I_e", 376.0) # 376 is background current

nest.SetStatus(voltmeter, params={})
nest.Connect(voltmeter, neuron)


nest.Simulate(200.0) # simulation time is 200 ms

nest.voltage_trace.from_device(voltmeter)
plt.show()

