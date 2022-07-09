%matplotlib inline
import matplotlib.pyplot as plt 
import networkx as nx

csv_positions = {}
csv_drive_times = {}

G = nx.Graph()

import csv 
with open('baza.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        csv_positions[row[0]] =  (float(row[1]),float(row[2]))
        csv_drive_times['Warszawa', row[0]] = (row[3])
        G.add_edge('Warszawa', row[0], color=row[4])
        
colors = nx.get_edge_attributes(G,'color').values()
plt.figure(figsize=(25,25))

nx.draw(G, csv_positions, edge_color=colors, node_shape='p', node_color='lightblue', node_size=25000, width=3, font_size=25, with_labels=True)
nx.draw_networkx_edge_labels(G, csv_positions, edge_labels=csv_drive_times, font_weight=3, font_size=20)

shortest_distance = nx.dijkstra_path(G, source='Rzeszow', target='Szczecin', weight='csv_drive_times')
print('Najkrótsza trasa z Rzeszowa do Szczecina prowadzi przez: ')
for city in shortest_distance:
    print(city, '- Warszawa :', csv_drive_times['Warszawa', city], 'minut')
