!pip install pgmpy
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import networkx as nx
import matplotlib.pyplot as plt

model = BayesianNetwork([('Rain', 'TrafficJam'), ('Accident', 'TrafficJam')])
cpd_rain = TabularCPD(variable='Rain', variable_card=2, values=[[0.7], [0.3]])
cpd_accident = TabularCPD(variable='Accident', variable_card=2, values=[[0.2], [0.8]])
cpd_traffic_jam = TabularCPD(variable='TrafficJam', variable_card=2,values=[[0.9, 0.8, 0.7, 0.1],[0.1, 0.2, 0.3, 0.9]],
evidence=['Rain', 'Accident'],
evidence_card=[2, 2])
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic_jam)
inference = VariableElimination(model)
probability_traffic_jam = inference.query(variables=['TrafficJam'], evidence={'Rain': 0, 'Accident': 1})
print(probability_traffic_jam)

pos = nx.circular_layout(model)  # You can change this to other layouts
labels = {node: node for node in model.nodes()}
nx.draw(model, pos=pos, labels=labels, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
plt.show()
