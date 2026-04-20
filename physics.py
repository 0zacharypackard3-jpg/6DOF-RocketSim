#Physics Engine

# I want the physics engine to have three main porposes, dynamically calculate air density, gravity and drag. The   "Negative Forces", for my second I want it to  calculate  the "Positive Forces" I.e  thrust velocity acceleration and Angle of Attack or the directionn using quaternions.
import numpy as np

G = 6.674e-11
mass_earth = 5.972e24
earth_radius = 3963.19 * 1609.3 # 6_371_000 meters
dt = 0.1

max_wind_speed = 20.0
drag_coeff = 0.5
cross_section_area = 10.0

position = np.array([0.0, 0.0, earth_radius])
velocity = np.array([0.0, 0.0, 0.0])

thrust_direction = np.array([0.0, 0.0, 1.0])

exit_atmosphere = False
apogee_height_set = False
apogee_height = np.array([0.0, 0.0, 0.0])


wind_vector = np.random.uniform(-max_wind_speed, max_wind_speed, size =3 )
position = position
relative_position_magnitude = np.linalg.norm(position)


relative_velocity = velocity - wind_vector
relative_velocity_magnitude = np.linalg.norm(relative_velocity)

def air_density_altitude(z):
    if z < 11000:
        T = 288.15 - 0.0065 * z
        P = 101325 * (T/288.15)**(9.80665/(0.0065*287))
    elif z < 25000:
        T = 216.65
        P = 22632 * np.exp(-9.80665*(z-11000)/(287*T))
    else:
        T = 216.65
        P = 2488 * np.exp(-9.80665*(z-25000)/(287*T))
    rho = P / (287 * T)1
    return rho

def dynamic_Gravity(position):
    relative_direction_to_center = position
    distance_from_core = np.linalg.norm(relative_direction_to_center)
    if distance_from_core == 0 :
        return np.zeros(3)
    g = -(G * mass_earth / distance_from_core**3 ) 
    return g

def dynamic_Drag():
    if relative_velocity > 0:
        drag_force = 1/2 * ( rho * drag_coeff * cross_section_area * relative_velocity * relative_position_magnitude)
    else:0
        drag_force = np.zeros(3)









