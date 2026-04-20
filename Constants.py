#constants


G = 6.674e-11
mass_earth = 5.972e24
earth_radius = 3963.19 * 1609.34
dt = 0.1

time = np.arange(0, sim_time + dt, dt)

solid_mass = initial_mass - fuel_mass

thrust_force = fuel_burn_rate * exhaust_velocity

max_wind_speed = 20.0
drag_coeff = 0.5
cross_section_area = 10.0

position = np.array([0.0, 0.0, earth_radius])
velocity = np.array([0.0, 0.0, 0.0])
thrust_direction = np.array([0.0, 0.0, 1.0])


exit_atmosphere = False
apogee_height_set = False
apogee_height = np.array([0.0, 0.0, 0.0])

wind_vector = np.zeros(3)


position_list = []
velocity_list = []

