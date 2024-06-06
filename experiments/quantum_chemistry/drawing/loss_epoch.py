import matplotlib.pyplot as plt
from PIL import Image
# import numpy as np

# https://geek-docs.com/matplotlib/matplotlib-axes/matplotlib-axes-axes-set_yscale-in-python.html
pmgd = [710.8477, 430.7972, 466.1062, 303.1116, 299.4464, 346.5337, 273.6119, 215.1704, 167.1174, 169.2498, 169.6256, 157.0826, 141.0671, 136.4553, 152.0934, 192.0273, 177.3306, 133.2638, 157.2829, 117.7762, 112.6729, 154.142, 104.3175, 114.3952, 119.3844, 161.9875, 121.6254, 104.9463, 139.3323, 102.2666, 117.1793, 149.0103, 94.3068, 143.2997, 89.9227, 122.6575, 84.5737, 86.579, 112.7238, 77.4205, 114.7162, 78.1786, 84.1332, 115.3457, 86.1154, 106.4727, 78.4809, 79.8217, 80.0013, 134.3831, 70.0305, 71.2565, 118.3551, 73.2768, 82.294, 72.204, 71.0965, 76.0624, 74.259, 67.9858, 67.1669, 73.6242, 69.4345, 94.9312, 66.6981, 69.3038, 73.908, 64.4168, 66.6132, 71.0303, 62.4034, 63.0219, 70.3841, 69.4224, 67.2759, 60.14, 66.7527, 60.0316, 66.0122, 66.6888, 69.2056, 67.0424, 60.135, 60.6671, 61.3098, 62.5158, 67.9098, 61.4418, 56.2544, 77.4538, 55.9867, 56.9963, 62.1785, 56.2969, 59.5846, 55.6738, 54.3805, 56.9771, 55.2802, 58.3329, 54.9887, 56.7687, 63.5487, 58.8758, 55.8804, 52.8872, 55.8001, 58.528, 60.9089, 68.5095, 65.5429, 64.1228, 63.0392, 70.8029, 59.8183, 63.0432, 76.3871, 60.2757, 58.3091, 59.4587, 66.2078, 67.2668, 76.9619, 61.3826, 58.5407, 56.4041, 56.9933, 58.5747, 55.8656, 58.967, 56.0147, 59.1067, 59.8002, 59.2017, 61.1244, 55.6629, 58.6352, 58.0357, 56.0671, 57.0038, 54.7388, 57.9543, 60.9194, 55.3733, 57.1428, 55.7057, 56.255,
        57.2865, 57.6675, 55.1953, 54.4969, 55.0846, 54.148, 55.9979, 54.5003, 53.6218, 54.8111, 54.8602, 53.484, 55.3671, 53.3555, 53.607, 55.3193, 53.9723, 54.7685, 53.4754, 53.4467, 52.8095, 52.8521, 55.0353, 54.6985, 53.7939, 54.299, 52.6883, 53.2975, 53.351, 52.3195, 54.8946, 52.8049, 52.7919, 52.5337, 54.3519, 53.8387, 54.8483, 52.237, 54.7006, 52.1017, 53.1162, 52.2504, 58.2849, 54.2276, 52.2967, 53.0033, 52.4828, 52.0017, 52.9899, 51.854, 51.7876, 51.9965, 51.7783, 53.4537, 51.8768, 51.5738, 52.4559, 51.3506, 51.9987, 53.2415, 51.3501, 52.129, 51.6248, 51.4136, 51.4098, 51.4455, 50.9905, 51.3629, 51.1607, 51.2169, 51.5904, 50.985, 50.9277, 51.5193, 50.7848, 50.7662, 50.65, 50.9752, 50.7923, 50.8804, 50.8087, 50.8492, 51.7947, 50.7425, 50.8425, 50.8603, 51.3037, 50.6276, 50.6621, 50.673, 51.15, 50.7248, 50.6402, 50.6161, 50.9267, 50.3899, 50.7635, 50.7552, 50.791, 50.5292, 50.7236, 50.4871, 50.9146, 50.6269, 51.0301, 50.3559, 50.4926, 50.9781, 50.255, 50.372, 50.2864, 50.5574, 50.6807, 50.3539, 50.5049, 50.3873, 50.3257, 51.0479, 50.2559, 50.3146, 50.2193, 52.2926, 50.3263, 50.2731, 50.1229, 50.6282, 50.094, 50.0751, 50.0989, 50.4019, 50.6126, 50.2, 50.1564, 50.4806, 50.0675, 50.0634, 50.0779, 50.5919, 49.9939, 49.9379, 50.2418, 50.0058, 50.0591, 49.8263, 49.8961, 50.0071, 49.9396, 50.9387, 49.8417, 50.1063, 49.9177, 49.8821, 50.1268]
mgda = [859.4317, 974.4016, 409.1741, 266.2228, 280.4739, 332.7542, 325.6121, 291.9973, 282.281, 695.6249, 293.8248, 235.8765, 169.9236, 156.8249, 257.4877, 821.8826, 187.7596, 280.3948, 146.5439, 198.3772, 127.1028, 131.7622, 341.6948, 125.1979, 202.4536, 115.4904, 222.3199, 219.1311, 130.938, 231.5661, 126.8756, 108.0263, 238.1145, 114.9348, 91.6806, 132.9174, 105.612, 151.8671, 146.0422, 278.424, 113.3355, 109.9607, 112.3247, 119.5141, 98.2781, 126.9369, 94.2282, 87.4586, 227.7147, 121.8894, 82.3276, 168.0829, 87.1008, 79.3726, 80.322, 90.0397, 76.743, 74.8765, 81.3914, 132.0212, 98.4077, 77.1322, 79.4707, 73.9731, 72.6659, 73.5902, 79.4192, 93.4014, 73.8013, 68.4518, 101.4772, 71.1053, 72.7952, 117.7752, 80.3975, 68.9564, 71.2403, 200.2217, 99.7812, 65.6492, 65.1608, 71.3728, 161.0973, 73.4269, 66.6424, 140.612, 154.6156, 75.063, 70.641, 96.9762, 141.5089, 65.7071, 68.8895, 68.8963, 63.7993, 89.9155, 143.1051, 63.6602, 62.3055, 80.9703, 65.3023, 62.364, 75.8041, 62.9602, 60.5818, 60.6702, 75.4077, 60.6965, 64.5456, 64.1233, 61.6814, 62.6844, 60.696, 81.6664, 60.5903, 62.7237, 63.7514,
        67.7782, 62.8136, 71.6682, 59.2456, 60.5062, 59.9855, 59.9441, 62.4073, 58.1654, 58.5474, 59.1421, 67.2626, 57.9362, 63.3583, 68.6499, 74.1843, 59.4271, 59.5534, 59.2045, 57.5766, 61.4926, 60.1968, 59.2392, 58.8143, 56.6072, 56.5916, 56.9476, 59.5678, 58.9445, 57.6256, 56.6363, 56.5358, 57.0398, 57.6613, 56.7834, 62.5627, 56.3619, 56.1097, 71.6258, 56.3778, 56.5448, 56.0764, 57.2951, 57.6561, 60.2529, 56.5764, 56.6878, 55.1896, 64.7941, 55.7, 56.4921, 55.4804, 55.4729, 55.8432, 55.6109, 70.026, 54.8291, 55.8934, 55.4487, 62.6927, 55.4065, 55.571, 54.6865, 56.0798, 55.4105, 55.1322, 55.0584, 55.693, 54.8708, 54.7953, 55.8645, 55.6308, 61.1814, 54.7732, 56.536, 65.7792, 56.0096, 54.4072, 55.4626, 54.5988, 56.6048, 59.8245, 54.6801, 56.9623, 54.0812, 54.0033, 54.7821, 54.3518, 54.8453, 54.4891, 55.5915, 55.6824, 54.365, 54.171, 55.7043, 53.8458, 54.6973, 55.6455, 54.3736, 56.1394, 58.7792, 54.0764, 54.4433, 54.6412, 53.4636, 54.4985, 53.7094, 54.929, 53.5589, 54.3744, 53.5659, 60.7602, 53.2703, 55.0363, 53.1075, 63.6604, 53.524, 53.7501, 65.8967, 53.5621, 53.8725, 53.1152, 53.9013, 53.2032, 58.3868, 58.5118, 58.2561, 59.2913, 58.3375, 58.1358, 58.5653, 57.6948, 58.94, 57.3319, 58.9766, 58.4191, 57.1481, 56.7082, 58.0979, 57.7531, 57.6702, 57.6389, 55.9742, 56.52, 56.0005, 57.4819, 56.9983, 56.3842, 55.6057, 55.9834, 55.9868, 56.7645, 56.4788, 56.7695, 55.8546, 55.1055, 55.9866, 56.0381, 55.3475, 55.729, 55.1727, 55.166, 54.9708, 53.9934, 53.9106, 53.6901, 54.8804, 54.1769, 54.5576, 55.3472, 53.9704, 54.2152, 54.9054, 53.7638, 53.3671, 53.6626, 53.3566, 54.7685, 54.4882, 54.0767, 54.5463, 54.3529, 53.0451]
linear = [511.66904, 815.31354, 423.4885, 294.84717, 243.02565, 249.04805, 308.82953, 244.0521, 204.46323, 311.0166, 273.32153, 222.0297, 207.88869, 202.90132, 166.26405, 179.61829, 190.47563, 149.04407, 184.40294, 155.46994, 191.56244, 178.04295, 134.92198, 158.27455, 122.15576, 156.10333, 127.09807, 145.48915, 124.13663, 120.23909, 159.40077, 125.2127, 113.02254, 111.93436, 124.562164, 162.19684, 127.451164, 131.56627, 131.77016, 114.05784, 106.30705, 112.35237, 105.82378, 111.97449, 106.98525, 98.89302, 109.90776, 95.598885, 96.49293, 100.92725, 97.95586, 101.353294, 136.95038, 94.00938, 129.2731, 91.98999, 99.86075, 103.84145, 112.37917, 115.8116, 97.978905, 108.302765, 91.36516, 87.6842, 88.689766, 97.925285, 95.78311, 89.139946, 98.69743, 91.17852, 89.671776, 89.50788, 100.67405, 82.74992, 90.802155, 80.676384, 89.32476, 87.70241, 81.82996, 79.95962, 101.86048, 83.21054, 87.14891, 77.356674, 79.46375, 83.641106, 84.869705, 78.10906, 82.3671, 76.83145, 76.4471, 78.11846, 78.46744, 76.16745, 76.79499, 78.61808, 77.56493, 80.80532, 74.99628, 74.806946, 79.79813, 75.39096, 79.665886, 74.444954, 76.36065, 75.51553, 76.5214, 73.37398, 73.65814, 75.34108, 74.83128, 78.664536, 74.50121, 74.31524, 72.87635, 72.73668, 73.0343, 73.208084, 72.10554, 79.58448, 78.61899, 76.50024, 74.37177, 72.005486, 75.513054, 74.62475, 72.2191, 74.98992, 73.254486, 71.61142, 71.604095, 72.10951, 71.78883, 71.41064, 71.36428, 72.264275, 71.17098, 70.87505, 71.23834, 71.44595, 71.02176, 71.75068, 71.54733, 70.32989, 72.7166, 77.802376, 71.41531,
          71.95122, 69.36335, 72.732025, 69.49346, 70.47796, 71.08066, 69.7474, 70.54929, 69.88443, 70.25292, 71.17988, 75.82964, 69.871, 69.16135, 69.51533, 73.09778, 69.04377, 69.43958, 71.241356, 70.56809, 70.8962, 70.51882, 69.2251, 73.120834, 68.84127, 68.807785, 70.55248, 69.439156, 68.78649, 69.11066, 68.14489, 69.146324, 68.92532, 70.99702, 68.10044, 69.443535, 67.89277, 68.306885, 69.24287, 68.24763, 67.99021, 69.150566, 68.036224, 70.26282, 67.916306, 68.49612, 67.652435, 69.17108, 67.68759, 67.95587, 68.89821, 68.239716, 67.80909, 68.00031, 66.858, 71.18354, 68.61089, 68.61651, 67.8899, 68.5012, 67.610054, 67.012146, 67.376915, 66.742546, 66.93518, 67.590004, 66.68332, 67.86722, 66.92569, 68.26311, 66.72822, 67.11439, 67.41223, 66.589264, 67.74755, 67.49944, 67.166016, 67.22434, 66.62386, 66.36415, 67.65517, 67.3683, 66.75853, 66.238655, 66.745964, 67.3016, 67.28076, 66.57283, 67.0978, 66.66558, 68.359436, 66.38095, 67.17094, 66.695526, 66.18177, 66.558495, 66.08869, 66.75146, 67.73206, 65.88728, 66.76596, 66.21252, 67.362236, 66.09305, 66.118256, 66.29195, 66.628494, 65.84732, 66.51032, 66.00523, 66.33801, 65.91678, 66.53329, 65.97396, 67.23854, 66.11667, 66.079056, 66.142975, 66.26956, 66.43996, 66.51373, 66.05606, 66.34104, 66.78687, 67.05714, 66.17064, 66.20745, 66.07538, 66.54879, 66.3168, 65.81326, 66.22586, 65.758415, 66.65251, 66.256, 65.981155, 65.99707, 65.57952, 66.41248, 66.04462, 65.84468, 65.78125, 65.5405, 65.52277, 65.94524, 67.13714, 65.71238, 65.61258, 65.6771, 65.638725, 65.72705, 65.58283, 65.48798]
imtl = [820.9613, 1376.4386, 524.2871, 1261.4852, 1064.5842, 1245.2502, 1256.5666, 434.1518, 466.3804, 473.507, 510.673, 441.2811, 2542.2296, 806.7068, 336.4591, 401.6023, 2073.8703, 536.7035, 1266.5147, 541.9922, 424.1435, 318.9562, 332.2074, 752.8984, 224.298, 297.7818, 254.3492, 660.9703, 382.6637, 547.2187, 690.9259, 599.7166, 213.839, 328.7518, 324.7466, 199.2973, 356.573, 217.5587, 467.6569, 386.2376, 205.0883, 151.6086, 180.708, 168.1195, 280.4141, 1160.0229, 555.9164, 153.6755, 520.2603, 141.1968, 251.4702, 314.5079, 140.6943, 346.4594, 184.858, 175.7952, 173.0883, 141.8248, 752.7163, 129.1873, 114.3933, 140.5499, 409.4916, 194.5157, 132.0168, 156.0876, 116.246, 107.0004, 172.9559, 104.4408, 211.0601, 101.7606, 798.6064, 106.1843, 97.2137, 337.3861, 314.2063, 624.3945, 401.9741, 138.2225, 225.3862, 151.6147, 207.5566, 99.7997, 439.2787, 92.3912, 85.2208, 207.5254, 98.3174, 169.1811, 89.3154, 85.3009, 164.5603, 81.51, 932.3592, 97.2795, 83.1251, 82.1133, 83.4866, 75.6629, 328.4792, 79.2313, 75.3475, 73.6051, 93.6131, 75.4571, 152.7976, 70.1216, 69.304, 246.3649, 78.4005, 93.7066, 69.7419, 67.5571, 101.0308, 97.9341, 68.5477, 351.268, 508.2686, 85.5179, 121.5762, 71.9876, 92.8373, 67.1151, 82.7061, 237.5758, 69.2732, 68.5117, 68.3414, 65.1373, 69.0738, 103.1232, 611.4933, 534.4511, 425.0979, 308.8289, 296.9375, 295.7115, 77.2431, 67.9567, 64.7524, 63.1881, 62.27, 101.9684, 62.014,
        63.3244, 60.4138, 63.8212, 199.9829, 64.3799, 60.0545, 63.2588, 59.7066, 59.5088, 193.248, 135.8793, 91.0963, 63.3838, 60.3069, 59.7088, 59.6623, 59.6758, 60.0034, 59.2085, 59.2608, 66.4235, 76.5792, 59.5336, 64.9542, 59.7961, 59.0091, 78.6511, 58.4222, 58.6453, 58.194, 62.0547, 59.8966, 116.0882, 233.5074, 202.5883, 98.5157, 69.1607, 60.4008, 58.5079, 57.5805, 57.3372, 60.4984, 57.3393, 57.019, 57.2226, 57.3223, 56.7646, 56.7273, 67.1633, 57.9395, 56.932, 56.9816, 98.3492, 61.5753, 56.6165, 55.9799, 56.0359, 68.1685, 55.8067, 56.097, 57.3455, 55.2788, 56.033, 152.0154, 86.2154, 55.9787, 155.1824, 56.6412, 56.9416, 208.6749, 55.8963, 71.4454, 55.6793, 69.7962, 229.5506, 55.1692, 55.0929, 55.6014, 55.697, 57.2487, 55.6428, 72.8469, 60.5666, 57.4304, 55.1571, 54.7963, 56.8127, 54.9319, 54.8187, 55.0567, 58.9137, 54.8483, 54.6969, 58.3555, 55.1722, 54.5083, 57.0291, 54.4282, 54.1788, 85.6884, 79.5835, 68.2433, 64.4308, 59.3496, 57.3315, 56.1996, 57.3925, 55.6417, 55.0341, 54.6976, 54.6346, 54.5507, 54.2154, 54.3843, 54.168, 127.4547, 54.0825, 56.5154, 53.8524, 113.0481, 145.0567, 140.3501, 198.2162, 236.0572, 91.3304, 56.5216, 57.5086, 54.3419, 53.9767, 84.2521, 53.8075, 53.468, 112.6236, 53.9078, 53.3667, 70.536, 84.7472, 53.8131, 54.6839, 115.7051, 58.667, 54.1979, 265.2778, 58.0227, 53.5121, 54.8766, 53.332, 53.5479, 53.1871, 53.0623, 54.7519, 52.9875, 52.466, 86.367, 145.2124]
pcgrad = [962.0925, 409.60138, 358.6485, 271.82547, 556.34863, 246.63478, 410.69308, 235.15321, 221.95827, 282.63263, 197.73457, 193.5934, 220.4542, 249.92157, 155.52048, 199.37881, 239.76439, 163.76317, 191.61224, 176.65077, 158.72902, 199.65228, 181.11847, 123.37979, 136.70062, 128.1118, 129.4096, 136.48282, 151.74318, 116.47349, 120.23076, 133.11916, 120.95287, 101.11175, 105.35906, 109.83375, 103.81758, 109.90029, 115.77502, 100.70242, 102.469215, 98.72849, 129.43314, 111.40502, 100.960815, 148.59381, 97.22656, 143.00426, 89.833855, 88.427864, 110.14157, 93.69396, 101.8521, 87.683525, 95.596504, 87.73287, 88.8238, 85.088585, 147.699, 89.61704, 86.18236, 90.836044, 105.6042, 84.00153, 95.465935, 91.44543, 85.143295, 93.46956, 79.985634, 100.17056, 81.81697, 80.772606, 85.88793, 79.045944, 104.415825, 81.88324, 77.8656, 83.77665, 77.22143, 79.10504, 78.72007, 93.494415, 95.81533, 89.78189, 85.80064, 77.353935, 75.49087, 74.16572, 76.24341, 91.60267, 81.0394, 74.56486, 83.33839, 72.15296, 73.37557, 79.503204, 72.76033, 76.39543, 76.43133, 78.69805, 70.95521, 69.94412, 80.25722, 73.01988, 73.803314, 69.88986, 71.51104, 69.421906, 73.573425, 70.693565, 67.804756, 69.701096, 68.37651, 67.47315, 67.91573, 67.951935, 78.72323, 69.16318, 71.12929, 74.75522, 68.38501, 67.90133, 71.71923, 69.52604, 69.27296, 71.32861, 70.70996, 66.7941, 70.34077, 66.110115, 66.3892, 67.03544, 65.61117, 67.639915, 74.4256, 65.88878, 70.0604, 65.58532, 66.75168, 68.33827, 66.41225, 65.029594, 65.13871, 65.97122, 67.14796, 64.69024, 67.632195, 65.979164,
          64.45483, 66.768974, 66.336334, 64.60029, 64.414185, 64.230415, 65.415596, 65.72108, 64.19635, 64.15573, 64.13794, 66.14435, 64.467026, 64.89954, 63.708237, 65.55881, 66.26559, 63.65015, 63.63396, 64.16267, 65.935936, 67.21643, 63.554222, 63.50757, 63.559376, 63.88031, 63.510963, 63.582386, 63.382023, 63.135006, 62.907497, 63.394413, 63.8163, 63.189774, 63.357212, 64.05226, 63.839233, 62.878403, 62.959896, 62.933434, 63.202892, 63.094296, 62.924282, 62.92456, 64.06082, 63.20085, 62.613476, 62.542797, 62.975258, 62.993263, 62.883312, 63.400974, 62.596035, 62.934055, 63.205654, 62.615673, 62.850403, 62.711685, 63.053085, 62.56936, 62.253345, 62.6548, 62.1645, 62.804237, 63.526356, 62.252953, 64.40327, 62.565712, 62.370304, 63.127987, 62.332413, 62.799747, 62.60706, 62.411243, 63.726974, 62.332615, 62.170517, 63.50555, 62.667725, 62.42255, 62.07098, 63.456905, 62.37311, 62.03899, 62.25084, 62.862453, 62.616837, 62.401234, 61.708035, 62.119034, 63.087814, 62.119534, 61.880787, 62.271603, 61.910656, 61.76689, 61.67242, 62.827232, 61.865067, 61.85222, 62.112648, 63.059372, 62.742783, 62.29935, 61.47854, 62.15143, 61.95221, 62.0537, 61.74029, 61.660458, 61.855007, 62.081726, 61.660145, 62.201656, 61.711365, 61.603165, 61.51952, 62.346985, 61.78388, 61.656593, 63.265663, 61.622593, 62.056274, 61.375973, 61.54679, 61.820778, 61.54369, 62.27284, 64.721565, 61.71121, 62.08341, 61.584354, 61.467373, 61.208313, 61.341076, 62.903725, 61.103687, 61.438683, 61.50254, 62.224003, 64.51271, 64.290085, 61.0936, 61.7893, 61.2493, 60.5574, 60.2061, 60.2003, 59.6487, 59.2137, 59.1208, 58.6864]

cagrad = [973.5182, 447.74963, 521.0119, 291.24756, 424.14212, 275.24213, 247.44366, 356.7957, 239.14528, 307.4925, 445.58908, 185.26222, 227.31688, 161.61264, 334.4075, 144.00746, 171.20563, 168.00758, 131.55019, 152.61282, 151.30113, 257.81577, 193.37242, 118.76455, 126.72949, 155.71771, 228.68784, 158.3775, 134.80396, 109.441826, 151.25299, 135.8163, 103.99385, 234.48859, 115.214165, 137.85248, 120.30582, 160.48834, 106.170044, 166.17572, 119.93445, 116.263435, 133.97026, 95.938484, 140.0973, 172.41719, 92.64874, 119.317604, 122.51694, 94.16004, 92.69385, 87.47948, 104.61694, 103.06589, 85.36493, 112.70354, 83.203995, 112.03616, 92.73721, 81.529045, 90.20645, 86.24343, 92.75905, 96.28462, 81.924194, 77.98256, 92.406364, 81.93803, 77.0652, 81.09565, 93.96624, 77.595184, 78.9945, 81.104324, 76.64254, 75.95736, 74.76148, 96.11862, 75.05869, 75.81297, 74.885185, 75.8413, 74.84581, 75.866585, 74.92056, 79.42764, 77.12989, 75.81473, 75.617424, 90.11031, 77.013214, 72.58382, 75.36325, 70.902145, 78.12521, 71.04265, 76.34472, 72.93506, 74.17743, 73.44253, 81.162056, 70.19493, 92.95994, 73.89399, 70.86003, 83.79208, 69.62839, 72.05883, 69.95739, 67.958015, 76.17252, 69.40387, 67.70472, 69.35483, 73.50468, 67.78591, 72.0382, 68.76496, 69.14785, 69.40954, 66.454575, 82.72765, 71.54495, 80.28777, 69.0318, 70.84261, 65.9206, 67.306465, 75.15464, 66.542046, 70.11052, 66.39738, 67.024185, 65.85128, 68.41062, 66.58726, 69.59883, 66.36005, 74.02456, 65.87655, 65.46563, 65.49223, 65.58849, 64.94355, 69.810234, 67.926605, 65.84734, 67.128365, 64.28319, 64.79703,
          64.7467, 64.760445, 66.2596, 65.23736, 63.887814, 65.39083, 63.926876, 65.09589, 64.47, 63.776512, 64.05039, 64.0337, 64.85725, 70.88675, 63.776, 63.90204, 62.88052, 63.541565, 62.983585, 64.73084, 63.029087, 64.54944, 63.070763, 63.215733, 63.01521, 63.447044, 64.1233, 63.199207, 62.756813, 64.56076, 63.979233, 62.672226, 63.916325, 66.061516, 62.79076, 65.14335, 64.16358, 63.321762, 64.62235, 62.29504, 62.441235, 62.87427, 62.201134, 62.095314, 61.903065, 62.00083, 62.23508, 62.79116, 62.11232, 63.02129, 61.52808, 61.880478, 61.81974, 61.55048, 61.69757, 62.310204, 62.832993, 62.620274, 61.502293, 63.010193, 61.468456, 63.276047, 63.44318, 62.0756, 61.455627, 61.925327, 62.325256, 61.887657, 61.328285, 61.11592, 61.8876, 61.743465, 61.79368, 62.70237, 61.28668, 61.88285, 61.487278, 61.769913, 61.74834, 61.734215, 62.567, 61.003807, 61.615982, 60.76376, 60.921032, 61.109188, 61.80897, 62.38954, 61.849464, 62.588135, 62.793934, 61.613033, 60.934006, 60.954784, 62.860035, 60.905678, 61.385952, 66.56224, 62.56696, 60.658848, 60.716408, 61.109432, 60.667057, 60.92361, 60.89138, 64.078636, 60.62418, 60.68142, 60.826393, 62.479496, 60.615074, 61.095226, 60.538086, 60.67549, 60.211414, 60.28766, 61.11122, 61.387024, 60.67107, 60.81868, 62.69301, 60.377148, 60.523575, 61.022324, 60.506176, 60.810352, 61.554012, 60.80629, 61.001198, 60.0636, 60.68351, 60.61529, 60.468384, 60.650013, 61.216427, 60.40476, 60.42019, 60.02435, 59.896935, 60.201572, 59.843822, 60.90281, 59.83536, 62.2328, 59.905888, 59.93944, 61.031456, 59.9442, 60.391087, 60.36936]
famo = [522.3509, 356.0002, 561.8272, 546.3925, 273.3013, 227.0054, 215.7909, 187.1131, 188.57, 253.7609, 184.4556, 183.399, 155.219, 364.2585, 386.2147, 132.1171, 187.5564, 138.1942, 141.1636, 154.2787, 134.6481, 115.8742, 118.0139, 149.1204, 138.5193, 129.7085, 204.1344, 198.5476, 106.6334, 108.5983, 102.9774, 102.4868, 103.3023, 104.2153, 98.5509, 94.4151, 89.9714, 91.1431, 111.8279, 93.5297, 90.152, 96.0474, 112.8599, 86.264, 86.9633, 103.1179, 94.1226, 83.3509, 80.4137, 83.5507, 83.8018, 79.687, 103.8657, 83.1076, 91.9359, 88.8314, 85.7104, 88.9867, 83.1097, 113.672, 85.0471, 77.3305, 81.8368, 77.2342, 85.2755, 81.4506, 76.1381, 70.0289, 73.6442, 79.1086, 70.5354, 84.5091, 74.8878, 71.656, 83.6855, 69.9255, 71.6439, 68.3677, 74.4552, 77.7134, 69.2938, 67.6976, 66.7364, 68.0303, 77.0849, 67.3016, 65.3358, 65.7577, 68.3928, 68.0847, 63.8461, 68.8686, 71.1949, 63.465, 66.4201, 63.672, 66.0992, 63.2944, 64.3437, 63.3759, 69.9379, 62.2855, 68.3474, 62.0575, 66.4665, 63.9725, 62.1894, 64.6315, 61.4975, 56.6776, 56.6052, 56.6079, 58.9953, 57.6734, 56.9193, 59.511, 56.4932, 58.3012, 56.2973, 57.255, 54.9992, 56.5475, 58.6486, 56.0155, 55.0102, 54.7139, 55.4317, 58.6956, 55.0002, 54.1862, 56.7849, 55.1583, 54.9655, 60.8514, 56.7547, 57.695, 58.8923, 54.1613, 56.0536, 53.845, 59.9566, 54.2767, 53.8692, 53.9344, 54.8255, 53.6236, 53.8824,
        52.9441, 54.9906, 52.9521, 52.7418, 53.5783, 52.8662, 53.3043, 52.7144, 53.5528, 52.7593, 52.4611, 52.1992, 52.1555, 51.9367, 52.5596, 52.1897, 51.9496, 52.4879, 54.4786, 51.907, 51.7783, 53.8284, 51.7567, 51.8856, 51.6124, 51.4098, 51.2286, 52.222, 51.7261, 52.9339, 51.689, 50.9733, 51.661, 52.166, 50.8689, 51.0701, 50.9625, 50.9233, 51.2808, 51.2371, 50.7775, 50.8011, 50.6765, 51.2655, 51.1155, 50.5876, 50.24, 50.7778, 50.1643, 50.5145, 50.4868, 50.2027, 50.1117, 50.1856, 50.2776, 50.7983, 51.0186, 49.8588, 50.1813, 49.8115, 50.2227, 50.0351, 50.3547, 49.8168, 49.8654, 52.2142, 49.9614, 50.163, 50.4821, 50.008, 49.8876, 49.9711, 50.2381, 49.791, 49.8394, 52.8672, 49.4955, 49.7596, 49.7388, 49.6876, 49.749, 49.665, 50.0025, 49.5879, 49.4972, 51.4062, 49.5418, 49.4177, 49.1281, 49.5859, 49.4315, 52.0203, 49.6849, 49.3684, 50.2503, 49.55, 50.2649, 49.1177, 49.5039, 49.6626, 49.7538, 51.2168, 49.5894, 50.7665, 48.9986, 50.3682, 49.2075, 48.991, 49.5164, 48.9941, 49.123, 48.9268, 49.1988, 49.4755, 48.8299, 49.1769, 49.2839, 48.6493, 48.6705, 48.6402, 48.6996, 49.0129, 48.648, 48.4331, 48.9179, 48.7921, 50.3784, 48.5837, 48.5027, 48.3189, 48.8205, 48.5205, 48.5959, 50.9367, 48.5694, 50.3162, 48.2884, 48.3257, 48.2949, 48.2127, 49.3002, 48.0846, 48.3814, 48.3016, 48.2524, 48.0754, 48.2516, 48.2581, 48.0745, 48.7265, 48.4444, 48.8976, 48.1249]
nashmtl = [940.793, 606.83795, 500.3275, 1389.6294, 300.89612, 1488.5115, 293.2498, 254.76329, 356.5028, 226.96063, 228.95323, 338.4285, 212.73384, 189.13686, 142.74666, 268.2533, 167.70328, 190.40973, 128.44628, 176.74416, 279.1642, 122.90522, 137.52786, 142.87405, 124.94551, 122.5075, 240.20444, 143.80267, 113.07105, 187.14777, 100.57848, 239.17706, 133.53958, 100.638916, 107.58542, 197.9231, 89.64191, 104.73804, 161.8727, 85.31855, 105.45551, 91.31635, 96.68628, 79.738556, 96.02963, 78.8839, 76.76872, 78.88834, 139.16792, 78.4861, 84.18412, 82.77058, 76.14503, 76.5043, 135.08821, 88.239204, 85.440445, 69.10925, 71.24664, 69.65172, 73.45011, 73.00837, 69.79893, 72.05262, 69.03522, 77.67121, 115.728226, 63.100845, 65.11969400000001, 74.10617, 61.993343, 62.33124, 61.03525, 67.85947999999999, 76.36286, 62.718113, 68.14427599999999, 59.722084, 72.04755, 66.542652, 58.550488, 58.965256, 60.48538, 59.599926, 70.8437, 59.731796, 57.840942, 56.51216, 59.673996, 66.732956, 58.497585, 57.30675, 57.904892, 56.727524, 85.28365, 56.824955, 57.95302, 56.08337, 57.744946, 56.29165, 57.359947, 56.448734, 54.896095, 55.50979, 55.675735, 55.756935, 58.428833, 89.69112, 53.916195, 53.967796, 54.29425, 55.35998, 54.99595, 53.660313, 54.830875, 77.77975, 55.21252, 56.89181, 54.735256, 58.64655, 56.964417, 53.00122, 53.555984, 55.007973, 65.9417, 54.34222, 55.432102, 52.10934, 55.39877, 52.430874, 52.422585, 52.97183, 51.97866, 55.363613, 51.556553, 52.262547, 52.248684,
           51.312634, 52.29169, 51.36656, 51.58221, 52.130787, 51.69645, 51.53694, 52.616337, 51.88784, 51.377247, 50.977005, 51.443798, 54.047623, 51.367188, 51.037884, 51.557713, 51.003326, 74.64222, 50.91013, 51.422474, 54.76486, 50.264935, 52.66248, 50.640133, 50.58553, 52.281925, 50.4223, 50.392452, 51.162426, 49.951797, 50.16207, 49.92723, 50.67821, 49.697388, 50.059696, 50.30048, 50.15373, 50.042027, 62.468014, 49.468525, 51.989468, 63.92654, 49.764065, 56.27624, 49.343307, 49.533463, 50.08106, 50.399723, 49.741867, 49.046104, 50.467216, 49.753323, 49.683018, 49.04029, 48.994408, 51.360085, 48.903244, 50.15188, 50.596504, 49.064735, 49.96194, 49.394608, 48.96483, 50.010555, 48.64455, 50.79166, 49.04726, 49.02768, 48.610565, 48.617344, 48.44849, 48.71933, 49.016964, 48.160114, 48.85832, 48.73944, 48.638584, 49.18849, 50.781662, 48.20621, 48.671265, 48.763554, 47.995052, 48.536716, 47.999237, 48.214676, 48.83345, 47.89968, 49.42898, 48.20783, 48.48239, 47.96963, 50.818825, 48.188335, 48.174908, 48.236027, 47.819366, 47.639206, 47.824387, 47.743313, 48.275112, 47.655064, 47.95189, 47.679947, 48.668552, 48.139725, 47.680313, 47.85892, 48.586437, 48.053425, 47.648262, 47.857376, 48.9182, 47.528046, 48.41298, 47.65071, 47.974293, 47.59178, 48.13899, 47.551765, 47.69126, 48.18996, 47.806934, 47.51875, 47.601334, 48.780987, 48.473766, 48.4082, 47.42961, 47.671856, 47.758877, 47.39882, 47.4751, 47.31159, 47.574924, 47.84441, 47.283157, 47.35632, 48.549454, 47.29764, 50.4535, 50.5946, 51.0837, 49.8452, 50.2734, 50.382, 49.0976, 50.1983, 49.3194, 48.9606, 50.5426, 50.4613, 50.0063, 48.9745, 48.5588, 49.5741, 49.0281, 48.3887, 49.0834, 48.1618, 49.8786, 48.4147, 49.1472]
fairgrad = [650.187, 622.5695, 452.7355, 935.4231, 447.7089, 314.3828, 216.0473, 559.8478, 405.3761, 302.8816, 281.874, 364.3471, 238.6643, 206.9067, 229.6894, 187.4122, 166.7206, 322.1135, 253.1573, 300.1349, 492.9757, 120.2971, 123.0255, 226.8608, 175.6229, 127.1455, 157.0126, 118.3964, 122.9566, 90.266, 143.0927, 281.7804, 102.0492, 124.0489, 181.0483, 127.8059, 98.2248, 98.225, 81.0764, 103.1141, 123.1485, 221.7303, 101.9354, 90.0442, 112.7769, 84.4017, 86.618, 86.3508, 109.7251, 152.1024, 93.3469, 119.9932, 79.3552, 109.6073, 76.746, 154.3999, 75.8311, 74.161, 100.002, 89.975, 78.4835, 71.726, 117.3733, 78.4058, 84.82, 88.3026, 74.2171, 75.1371, 144.8678, 113.8635, 81.3133, 128.1733, 90.559, 67.4685, 76.7606, 65.4231, 84.2638, 68.5536, 77.1361, 88.7806, 68.9071, 82.8958, 65.0437, 64.2229, 77.1487, 70.4161, 69.8281, 78.3127, 68.6371, 66.7323, 61.5439, 76.3231, 64.5508, 64.3965, 85.5821, 59.6127, 65.7811, 65.2747, 61.4722, 67.5676, 60.5704, 59.1159, 61.9568, 58.2996, 90.0945, 59.6524, 64.3257, 57.6968, 58.8523, 57.9477, 56.9587, 57.336, 57.6197, 57.1843, 58.7039, 66.4948, 56.4075, 58.6662, 57.6239, 63.5653, 57.9269, 59.4891, 55.4112, 62.5737, 55.6469, 55.4445, 55.6811, 55.7027, 56.9206, 66.2911, 56.8516, 54.787, 59.2449, 59.5063, 54.6216, 55.718, 54.6624, 54.2969, 58.905, 55.2501, 54.1475, 56.411, 54.7543, 55.1702, 59.0389, 55.3925,
            53.6372, 56.5444, 53.7854, 59.0997, 53.4478, 53.8846, 57.3576, 53.1326, 60.8862, 53.8509, 53.3333, 53.4702, 56.8278, 53.6187, 53.2514, 53.3485, 52.8857, 54.6518, 53.6189, 52.8694, 53.277, 53.1476, 54.3444, 54.3224, 54.0218, 52.7538, 52.9081, 52.3919, 54.7084, 52.4918, 52.9206, 53.4952, 53.4637, 52.6242, 53.3494, 54.5925, 52.51, 52.6559, 53.5614, 53.4412, 52.7986, 52.3239, 52.3795, 52.5232, 53.2673, 53.3438, 55.3366, 53.4907, 52.1246, 53.0437, 52.6707, 52.804, 51.8007, 53.2463, 53.3114, 52.1771, 51.8674, 52.2483, 52.3253, 52.1317, 53.2264, 52.66, 52.318, 51.8776, 51.471, 51.9851, 51.772, 52.091, 51.6463, 51.8412, 52.4402, 51.3717, 51.8088, 51.3547, 53.9522, 51.5924, 51.291, 52.2318, 51.2651, 51.7953, 53.249, 51.113, 52.4212, 51.9626, 51.3702, 52.0985, 53.3116, 51.7584, 51.7539, 52.0991, 51.5271, 50.8765, 51.8172, 58.9187, 51.6533, 53.3966, 51.6726, 52.0987, 50.8252, 51.5926, 51.9043, 54.1339, 51.6094, 51.4206, 51.7459, 51.1145, 50.7201, 50.8929, 50.7949, 51.1303, 51.7, 51.0785, 51.2458, 50.725, 55.992, 50.5352, 50.915, 50.7803, 51.4357, 50.3435, 54.2936, 55.1901, 51.0567, 50.2004, 50.3362, 51.7035, 50.8324, 51.0263, 50.5853, 53.849, 50.9025, 50.609, 53.2791, 50.4189, 50.1229, 50.6367, 50.6616, 50.6607, 49.953, 51.2088, 50.3326, 56.2308, 50.2595, 50.3394, 50.6343, 49.8664, 49.7501, 54.6332, 50.2911, 50.0715, 52.9593, 50.0946, 51.6182, 49.6103]

# Create a list of communication rounds (assuming 1 round per loss value)
rounds = list(range(0, len(pmgd)))

# Create the plot
fig, ax = plt.subplots(figsize=(8, 4))

# Plot each array with different colors and line shapes
# plt.plot(rounds, loss_array1, color='blue', linestyle='-', label='Array 1')
# plt.plot(rounds, loss_array2, color='green', linestyle='--', label='Array 2')
# plt.plot(rounds, loss_array3, color='red', linestyle='-.', label='Array 3')
# plt.plot(rounds, loss_array4, color='orange', linestyle=':', label='Array 4')
# plt.plot(rounds, loss_array5, color='purple', linestyle='-', label='Array 5')

plt.plot(rounds, linear, color='orange', linestyle='--', label='LS')
plt.plot(rounds, mgda, color='cyan', linestyle='-.', label='MGDA')
plt.plot(rounds, pcgrad, color='purple', linestyle=':', label='PCGrad')
plt.plot(rounds, cagrad, color='red', linestyle='-.', label='CAGrad')
plt.plot(rounds, imtl, color='green', linestyle='-', label='IMTL-G')
plt.plot(rounds, famo, color='yellow', linestyle='-', label='FAMO')
plt.plot(rounds, nashmtl, color='lightgreen', linestyle='-', label='NashMTL')
plt.plot(rounds, fairgrad, color='lightpink',
         linestyle='--', label='FairGrad')
plt.plot(rounds, pmgd, color='blue', linestyle='-.', label='PSMGD')

# Setting logarithmic scale for y-axis
ax.set_yscale("log")

# Setting labels and title
# ax.set_xlabel('Training epochs', fontsize=15)
# ax.set_ylabel('Test Loss', fontsize=15)

# Configuring ticks and legends
ax.set_xticks([0, 50, 100, 150, 200, 250, 300])
ax.legend(loc='upper right', fontsize=12)
ax.tick_params(axis='x', labelsize=12)  # Adjust x-axis tick label font size
ax.tick_params(axis='y', labelsize=12)  # Adjust y-axis tick label font size
# Setting limits (adjust these if necessary)
# ax.set_ylim(bottom=1)  # Adjust as needed based on your data
plt.xlim(-1, len(pmgd))

# Tight layout for better spacing
plt.tight_layout()

# Save plot to file
output_file = '/home/mx6835/Academic/MM1204/FAMO/experiments/quantum_chemistry/drawing/results/QM9_loss.png'
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
# plt.xlim(-1, len(pmgd))
# # Display the plot
# plt.tight_layout()
# output_file = '/home/mx6835/Academic/MM1204/FAMO/experiments/quantum_chemistry/drawing/results/QM9_loss.png'
# plt.savefig(output_file, dpi=300)
# image = Image.open(output_file)
# image = image.convert('RGB')
# pdf_file = output_file.replace('.png', '.pdf')
# image.save(pdf_file, 'PDF', resolution=100.0)
# image.close()
