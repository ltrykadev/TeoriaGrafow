%matplotlib inline
import matplotlib.pyplot as plt 
import networkx as nx
import matplotlib.image as mpimg

csv_positions = {}
csv_drive_times = {}
size_table = []

G = nx.Graph()

import csv 
with open('Baza_2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        csv_positions[row[0]] =  (float(row[1]),float(row[2]))
        csv_drive_times[row[0], row[5]] = (row[3])
        csv_drive_times[row[5], row[0]] = (row[3])
        G.add_edge(row[0], row[5], color=row[4])
        size_table.append(20*int(row[6]))
        
colors = nx.get_edge_attributes(G,'color').values()
    
plt.figure(figsize=(50,50))
img = mpimg.imread('map.png')
hor_min = 14.123 
hor_max = 24.1507
ver_min = 49.0064
ver_max = 54.8391
plt.imshow(img, extent=(hor_min, hor_max, ver_min, ver_max))

nx.draw(G, csv_positions, edge_color=colors, node_shape='o', node_color='orange', node_size=size_table, width=5, font_color="black", font_size=25, font_weight="bold", with_labels=True)
nx.draw_networkx_edge_labels(G, csv_positions, edge_labels=csv_drive_times, font_weight=3, font_size=20)

shortest_distance = nx.dijkstra_path(G, source='Praga', target='Lwow', weight='csv_drive_times')
print('Najkrótsza trasa z Pragi do Lwowa prowadzi przez: ')

dijkstra_table = []
for row in shortest_distance:
    dijkstra_table.append(row)

counter=0
for row in dijkstra_table:  
    if len(dijkstra_table) > (counter+1):
        print(dijkstra_table[counter],"-",(dijkstra_table[counter+1]),":",(csv_drive_times[(dijkstra_table[counter]),(dijkstra_table[counter+1])]) )
        counter += 1
