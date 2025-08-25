 # import data

import physics_constants

 # calculation of position, velocity and kinetic energy

t = 2
position = physics_constants.building_height + physics_constants.initial_velocity * (t - 0.5) * physics_constants.standard_gravity * (t ** 2)
velocity = physics_constants.initial_velocity - physics_constants.standard_gravity * t
kinetic_energy = 0.5 * physics_constants.ball_mass * (physics_constants.initial_velocity ** 2)

 # print output
 
print(physics_constants.standard_gravity)
print(physics_constants.ball_mass)
print(physics_constants.building_height)
print(physics_constants.initial_velocity)
print(position)
print(kinetic_energy)
if velocity > 0:
    print("Moving down")
else:
     print("Moving up")
