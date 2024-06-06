import matplotlib.pyplot as plt
from PIL import Image
# import numpy as np

# https://geek-docs.com/matplotlib/matplotlib-axes/matplotlib-axes-axes-set_yscale-in-python.html
psmg_4 = [960.98224, 510.43222, 312.1531, 320.51044, 298.7595, 281.71048, 196.31079, 224.56737, 200.87212, 181.9603, 208.0066, 296.73465, 169.02211, 153.18588, 160.63062, 148.90968, 137.12697, 151.62144, 256.78796, 171.72966, 156.81166, 117.19932, 120.96142, 193.82681, 174.87311, 121.3579, 215.15843, 114.596634, 100.18306, 126.550446, 156.14833, 97.46465, 112.40854, 104.81079, 96.233696, 91.4617, 110.032234, 178.36835, 99.0394, 90.68564, 120.68049, 92.08492, 84.46669, 92.48162, 85.45845, 84.34915, 176.79774, 81.02618, 92.59316, 83.18751, 93.2241, 78.20909, 87.586006, 80.46699, 94.50677, 75.94117, 81.07972, 91.93827, 78.69939, 77.900604, 81.09879, 73.58602, 73.41532, 78.85259, 75.66788, 139.44157, 92.29425, 71.90864, 86.83525, 73.94034, 123.356125, 74.391815, 70.27426, 71.15792, 69.90789, 73.844505, 68.96784, 89.24897, 74.217094, 73.55321, 84.22541, 72.09782, 66.71987, 66.82124, 68.08157, 71.08213, 65.228546, 71.32647, 76.86011, 67.48892, 70.55656, 63.311672, 68.181046, 69.43577, 63.876377, 71.53578, 65.478516, 63.03749, 64.63412, 66.09009, 61.732872, 67.08884, 65.00907, 71.729485, 65.479645, 62.866085, 65.431335, 60.686428, 63.125916, 63.447952, 61.848827, 60.692165, 62.799564, 65.406456, 60.073204, 63.463577, 62.154514, 60.626286, 61.285233, 65.35595, 62.358738, 59.860416, 59.76794, 64.85409, 59.821793, 60.112614, 61.22202, 61.947056, 59.482277, 60.48892, 58.54413, 58.654606, 61.69311, 58.599266, 59.843483, 57.970387, 60.246822, 58.71234, 58.358273, 58.449112, 58.088566, 62.873356, 57.26686, 57.750027, 57.306797, 57.680515, 57.420692, 58.46472, 56.908207, 58.044125,
          57.474014, 57.11472, 57.372143, 56.874393, 56.78216, 57.04227, 56.859623, 56.770042, 57.73077, 57.30618, 57.409805, 56.616055, 56.31371, 56.82584, 57.55044, 56.126183, 59.188572, 56.15173, 57.302074, 56.87163, 56.085205, 57.153446, 56.139694, 56.92184, 56.480934, 55.83279, 56.485146, 55.883484, 55.818527, 55.722034, 56.001663, 55.734142, 56.318653, 56.378628, 55.804134, 56.562344, 55.52271, 55.503117, 55.55968, 55.85821, 55.706364, 55.9729, 55.296055, 55.1936, 55.584312, 56.465405, 55.800655, 55.84712, 54.92389, 55.144726, 55.229366, 55.346214, 55.041733, 55.743237, 55.1979, 55.31397, 55.133926, 54.727177, 54.783226, 54.798695, 55.199596, 54.642174, 54.85082, 54.736744, 55.133976, 54.435413, 55.18733, 54.97822, 55.026974, 54.835182, 54.513893, 54.557133, 54.601, 54.556103, 54.509254, 54.835087, 54.600723, 54.41177, 54.66715, 54.5757, 54.247215, 54.57323, 55.195858, 54.41831, 54.28475, 54.21437, 54.216015, 55.44429, 54.19249, 54.257595, 54.325546, 54.551754, 54.382004, 54.272923, 54.024014, 55.35046, 54.10306, 54.78564, 54.21493, 54.01941, 54.164955, 54.27331, 53.91357, 54.120834, 54.08097, 54.237904, 54.137634, 54.567165, 54.043053, 53.79905, 54.102306, 54.314198, 54.248634, 53.968346, 54.193882, 54.01566, 53.73441, 53.761864, 53.845715, 53.72849, 53.783207, 54.92911, 53.884464, 53.870995, 53.63562, 54.112827, 53.65076, 53.871548, 53.856007, 53.649952, 53.91958, 53.537743, 53.94669, 53.679466, 53.694187, 53.934433, 53.418034, 53.776318, 53.53503, 53.56634, 53.668198, 53.511307, 53.517605, 53.584545, 53.443615, 53.621334, 53.53373, 53.202835, 53.555836, 53.41161]
psmg_8 = [707.4851, 419.4051, 361.343, 283.7448, 369.0651, 235.6552, 247.1366, 301.9665, 208.3385, 176.5006, 183.2859, 324.4048, 224.7116, 170.7385, 180.5024, 143.5091, 353.3202, 137.1712, 149.4744, 167.5378, 133.8956, 118.7695, 121.782, 163.1141, 173.8663, 131.5201, 140.8013, 108.4008, 101.282, 129.1683, 139.6315, 112.2158, 95.9712, 118.0056, 91.6389, 114.7134, 113.4947, 85.4138, 107.358, 110.7371, 88.8174, 88.1391, 91.4607, 87.5226, 106.0866, 79.1499, 78.1297, 78.4874, 80.4912, 87.9379, 89.6897, 77.3571, 102.9608, 79.7995, 104.6616, 83.4689, 77.3718, 78.8396, 112.18, 85.5147, 73.9454, 77.17, 93.1472, 102.6395, 69.6383, 69.1134, 88.0236, 76.2871, 71.0079, 93.9378, 73.5657, 73.3268, 72.4724, 72.6524, 71.2833, 76.8695, 68.7207, 88.5314, 66.2517, 64.364, 66.29, 67.6023, 67.9692, 67.0593, 65.2793, 63.654, 63.0129, 66.0074, 84.8615, 62.6959, 62.7504, 60.9996, 63.6672, 60.9974, 62.6501, 68.0434, 67.8282, 62.6924, 80.2098, 60.7248, 63.2234, 61.4936, 62.0753, 59.3526, 74.2981, 61.2772, 59.1664, 63.3335, 59.7374, 61.7966, 62.9947, 62.5104, 61.1203, 60.9211, 64.7799, 61.0702, 66.0718, 60.5641, 60.2127, 61.7632, 60.9976, 65.0301, 60.8966, 59.5221, 59.4944, 59.8587, 64.0653, 59.8719, 61.5206, 59.669, 59.0729, 59.1196, 59.328, 64.3659, 60.103, 64.2982, 58.3121, 58.4195, 57.8104, 61.1099, 58.4784, 64.5398, 58.9143, 66.2474, 58.368, 58.1824, 60.5225,
          59.4825, 57.3691, 57.2957, 58.1, 62.2687, 57.6061, 57.9251, 57.2548, 56.9936, 58.42, 57.3855, 57.6996, 57.4246, 57.0941, 57.0481, 56.3158, 56.3526, 56.9388, 56.8689, 59.591, 56.5101, 56.3857, 57.4194, 56.5509, 56.2051, 57.4578, 56.811, 56.0748, 56.913, 55.9898, 56.8269, 55.7367, 56.062, 56.2895, 56.138, 55.5355, 55.7996, 55.9617, 55.5461, 55.7885, 55.3073, 55.3625, 55.7796, 55.7974, 56.1132, 55.1578, 55.5459, 55.9487, 55.363, 55.3414, 55.1915, 55.1436, 55.1194, 55.2079, 54.9734, 54.9402, 54.9895, 55.1749, 54.9888, 55.4008, 55.4352, 55.1831, 54.8446, 54.9879, 55.0022, 54.7595, 54.7295, 55.0046, 54.8801, 54.9669, 56.4045, 54.8462, 54.8906, 54.5883, 54.5596, 55.7439, 54.9102, 54.6861, 55.4333, 54.537, 54.7252, 54.4248, 54.407, 54.5763, 54.4213, 54.2551, 54.2465, 54.1407, 54.5414, 54.2088, 55.2925, 54.3611, 54.2221, 54.4836, 54.257, 53.9655, 54.2208, 54.0068, 55.1859, 54.2395, 53.8612, 54.4596, 54.2227, 54.4291, 54.0341, 53.8329, 53.8886, 53.9977, 54.2673, 53.7634, 54.6008, 53.9536, 54.5873, 53.9493, 54.4061, 53.9681, 53.8497, 54.0915, 54.1204, 53.6885, 53.8877, 53.8041, 53.6976, 54.0938, 53.8714, 53.66, 54.0757, 53.7914, 53.9437, 53.8258, 53.6823, 54.9096, 53.6824, 53.7541, 54.5578, 55.1022, 53.788, 53.7438, 53.9081, 53.4904, 54.0038, 53.5221, 53.5606, 53.5154, 53.464, 53.789, 53.4183, 53.5608, 53.6614, 53.3654, 53.4711, 53.457, 54.078]
psmg_16 = [791.54663, 379.39874, 332.35785, 340.76245, 289.92462, 223.9413, 258.12036, 197.39769, 200.63097, 279.80066, 181.21536, 217.66237, 202.66815, 148.5112, 181.89972, 141.08788, 135.64824, 199.60551, 138.87929, 119.34677, 244.80273, 129.45111, 184.26451, 235.79716, 154.39398, 122.493744, 113.50642, 120.098, 113.71241, 105.24301, 100.77588, 113.40305, 107.953804, 128.5288, 100.55346, 101.884834, 101.25061, 103.51832, 141.92848, 112.92288, 93.02448, 92.04264, 93.7429, 121.8592, 87.94177, 106.94832, 99.19642, 93.547554, 92.61718, 81.884026, 84.43816, 84.7021, 81.79498, 80.31937, 93.46695, 78.89218, 118.772, 77.55632, 218.96657, 77.70326, 76.225945, 75.9267, 75.63397, 81.331245, 85.18642, 82.53179, 77.527, 78.51936, 79.24999, 76.99298, 75.538055, 79.062706, 71.7164, 74.96457, 76.02707, 71.606224, 71.83189, 71.33726, 72.82938, 69.99317, 70.24832, 76.368355, 68.43758, 85.85556, 73.69504, 70.36256, 68.070724, 70.05432, 69.05969, 70.10411, 87.298676, 66.0263, 79.471504, 77.65607, 66.42067, 73.46535, 69.603546, 65.30878, 68.17191, 82.73429, 65.44149, 72.97303, 67.19776, 64.03838, 64.819145, 67.82183, 63.629566, 65.32755, 63.571335, 62.92092, 64.69843, 63.214188, 63.423084, 63.96622, 63.34473, 62.449986, 62.80275, 62.5286, 62.197254, 62.670425, 61.902206, 62.347633, 61.4343, 61.34871, 65.98006, 64.19687, 64.559944, 60.725014, 64.65539, 63.7397, 60.97613, 61.091393, 61.36029, 60.135082, 60.638706, 62.445507, 60.894176, 60.463444, 62.158707, 60.43417, 60.30469, 59.944702, 60.579163, 59.75918, 59.227627, 59.277515, 59.345325, 59.59907, 59.77887, 60.916832,
           62.849308, 60.835632, 61.76161, 59.253075, 58.883102, 58.975964, 59.710575, 59.911636, 58.87388, 58.703365, 58.849503, 59.465866, 59.672165, 58.66235, 59.75901, 59.044003, 59.77802, 58.386757, 59.07191, 59.3442, 58.64116, 58.265297, 58.392906, 58.535168, 58.380337, 58.408276, 58.956905, 58.666805, 58.70422, 58.192204, 58.26229, 58.21288, 57.92783, 57.71183, 57.928383, 58.727184, 58.31043, 57.75399, 57.83644, 57.882328, 57.58698, 57.87395, 57.39795, 57.560986, 57.466347, 57.340427, 57.22674, 57.89301, 57.774654, 57.33479, 57.549557, 58.03142, 56.927917, 57.203075, 57.08793, 57.592567, 57.16201, 57.426846, 56.970432, 56.977737, 57.317772, 56.807423, 57.51095, 56.627895, 56.854347, 57.16437, 56.731216, 56.833908, 56.505543, 56.963932, 57.15798, 56.60802, 56.6317, 56.917343, 56.77836, 56.612553, 57.01029, 56.428234, 56.45074, 56.931015, 56.585827, 56.55835, 56.5939, 56.723545, 56.46143, 56.232273, 56.275814, 57.88579, 56.386276, 56.741093, 56.751583, 56.211685, 56.265137, 56.13046, 56.22632, 56.616837, 56.57875, 56.39922, 56.015182, 56.56846, 56.305626, 56.15735, 55.93664, 56.239742, 56.13445, 55.987156, 55.999386, 56.564014, 56.10027, 56.07172, 55.82262, 56.04571, 56.35583, 56.032887, 56.662888, 56.05459, 55.69076, 55.89094, 56.90753, 56.122547, 56.037292, 56.00806, 55.835716, 55.800354, 55.8651, 56.4281, 55.62588, 56.09004, 55.69791, 55.666237, 55.819286, 55.620632, 56.78125, 55.830296, 55.664425, 55.468483, 55.48965, 55.887596, 55.83413, 55.766674, 56.31687, 55.93274, 55.856224, 55.52875, 55.55405, 55.346275, 55.495434, 55.682705, 55.512917, 55.471397]
psmg_32 = [682.39606, 591.45355, 293.6842, 271.54718, 251.33482, 275.7794, 204.28937, 473.1654, 174.40921, 217.83902, 162.94086, 154.29517, 162.8855, 164.98117, 144.43626, 145.77832, 153.53304, 155.7059, 129.67574, 145.05644, 135.06447, 118.33723, 123.9815, 154.85838, 110.388275, 115.30642, 155.00356, 105.5654, 104.46812, 116.142044, 97.97348, 134.61224, 104.764534, 98.81826, 102.44096, 136.95775, 98.170555, 95.450165, 109.03272, 151.73384, 95.65162, 91.347404, 98.66102, 86.74899, 123.54326, 126.200874, 136.79893, 144.19989, 230.2423, 98.73876, 160.33565, 105.10656, 108.58025, 98.50078, 111.73957, 85.53308, 92.39965, 100.936615, 93.27448, 84.12493, 92.9215, 99.494194, 89.64783, 90.209435, 80.657646, 85.1099, 86.72605, 80.17359, 86.48215, 84.46088, 87.671906, 85.22408, 76.89929, 83.7269, 104.053635, 82.98789, 96.64773, 81.011894, 75.827805, 79.330536, 108.06625, 75.42843, 78.06653, 76.19682, 89.04179, 82.45466, 91.87257, 92.50164, 70.90889, 82.88429, 71.76405, 73.18499, 89.32933, 74.0735, 80.456566, 68.77795, 69.956055, 68.78544, 67.71051, 69.451004, 69.73159, 74.48893, 83.70394, 66.52636, 74.7669, 67.11053, 65.84935, 65.66871, 66.9986, 69.0493, 66.25761, 65.18523, 66.14044, 65.0055, 64.582504, 65.45291, 65.608116, 65.52778, 69.53132, 64.682335, 66.63734, 63.674305, 64.3917, 64.29864, 63.543236, 68.003365, 64.14749, 73.26963, 64.46998, 65.21276, 63.362953, 64.34772, 63.241882, 64.14527, 65.38921, 63.788784, 68.0581, 64.978065, 62.84951, 70.60033, 62.10967, 64.29031, 62.209, 65.71644, 62.349655, 65.74064, 62.839317, 62.040028, 61.257286, 61.768387, 68.85253, 62.899857,
           61.436806, 62.509117, 62.659912, 61.29403, 62.386623, 61.317154, 62.353214, 61.950756, 61.14612, 61.745533, 66.205925, 62.719177, 61.807644, 61.519688, 61.38824, 60.991177, 60.912315, 64.62458, 66.56939, 61.79343, 62.91317, 60.881996, 60.594753, 61.982, 60.75499, 61.52098, 60.718807, 60.528538, 62.557236, 60.202587, 60.963097, 64.55041, 59.93728, 61.50748, 60.291927, 60.197464, 60.35968, 59.903736, 63.19205, 61.128506, 59.96381, 59.983948, 59.780636, 59.643112, 59.649452, 59.509464, 59.575085, 59.737206, 60.016346, 59.60665, 59.653847, 59.522213, 59.59486, 59.722973, 59.43401, 60.003117, 59.497364, 59.36151, 59.589745, 59.296413, 59.403038, 59.355507, 60.189964, 60.78021, 59.65703, 59.315258, 59.24075, 59.56111, 59.4838, 60.258873, 59.321594, 59.409557, 59.380386, 59.42744, 59.039505, 59.536545, 59.024014, 59.202835, 59.07578, 59.419273, 59.014267, 58.953323, 59.051952, 58.91671, 59.20869, 59.52816, 62.010914, 59.033558, 58.955418, 59.62905, 59.005222, 58.913162, 59.045692, 58.935463, 58.91084, 58.716225, 58.768307, 59.060337, 58.661537, 58.91895, 59.08575, 58.854427, 60.320374, 58.727524, 58.601086, 58.68367, 58.62615, 58.81155, 58.679813, 59.016354, 58.974792, 59.182312, 59.693844, 58.59775, 59.061535, 58.38866, 58.507423, 58.473446, 59.994278, 58.510643, 58.852596, 58.960815, 58.931484, 59.308704, 58.641403, 58.268826, 58.287426, 59.355972, 58.351517, 58.20625, 58.323105, 59.083652, 58.387936, 58.465122, 60.681545, 58.981567, 58.18436, 59.563328, 58.831142, 58.304283, 58.260048, 58.27108, 58.123646, 58.071327, 59.30512, 58.144665, 58.998425, 57.918617]

# Create a list of communication rounds (assuming 1 round per loss value)
rounds = list(range(0, len(psmg_4)))

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))

plt.plot(rounds, psmg_4, color='cyan', linestyle='-.', label='PSMGD (R=4)')
plt.plot(rounds, psmg_8, color='blue', linestyle='-.', label='PSMGD (R=8)')
plt.plot(rounds, psmg_16, color='green', linestyle='-', label='PSMGD (R=16)')
plt.plot(rounds, psmg_32, color='purple', linestyle=':', label='PSMGD (R=32)')
# Setting logarithmic scale for y-axis
ax.set_yscale("log")

# Setting labels and title
# ax.set_xlabel('Training epochs', fontsize=15)
# ax.set_ylabel('Test Loss', fontsize=15)

# Configuring ticks and legends
ax.set_xticks([0, 50, 100, 150, 200, 250, 300])
ax.legend(loc='upper right', fontsize=12)

# Setting limits (adjust these if necessary)
# ax.set_ylim(bottom=1)  # Adjust as needed based on your data
plt.xlim(-1, len(psmg_4))

# Tight layout for better spacing
plt.tight_layout()

# Save plot to file
output_file = '/home/mx6835/Academic/MM1204/FAMO/experiments/quantum_chemistry/drawing/results/AB_loss.png'
plt.savefig(output_file, dpi=300)

# Optional: Convert to PDF as in original script
image = Image.open(output_file)
image = image.convert('RGB')
pdf_file = output_file.replace('.png', '.pdf')
image.save(pdf_file, 'PDF', resolution=100.0)
image.close()
# # Set the y-axis scales
# # plt.yticks([0.5, 1.0, 1.5, 2])
# plt.xticks([0, 50, 100, 150, 200, 250, 300])
# # Adjust x-axis tick label font size
# plt.tick_params(axis='x', labelsize=15)
# # Adjust y-axis tick label font size
# plt.tick_params(axis='y', labelsize=15)
# # Add a legend
# plt.legend(loc='upper right', fontsize=12)

# # Set the y-axis limits
# plt.ylim(bottom=0, top=500)
# plt.xlim(-1, len(psmg_4))
# # Display the plot
# plt.tight_layout()
# output_file = '/home/mx6835/Academic/MM1204/FAMO/experiments/quantum_chemistry/drawing/results/QM9_loss.png'
# plt.savefig(output_file, dpi=300)
# image = Image.open(output_file)
# image = image.convert('RGB')
# pdf_file = output_file.replace('.png', '.pdf')
# image.save(pdf_file, 'PDF', resolution=100.0)
# image.close()
