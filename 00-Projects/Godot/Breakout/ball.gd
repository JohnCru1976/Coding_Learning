extends CharacterBody2D

var direction		# Is a normalized 2D vector
var speed = 450		# Initial speed
var offset = 5
# Screen parameters
var screen_width = 480
var screen_height = 720

# Called when the node enters the scene tree for the first time.
func _ready():
	start_ball()
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass

func _physics_process(delta):
	# Move the object on the actual direction
	var collision = move_and_collide(direction.normalized() * speed * delta)
	if collision:
		var type_collision = collision.get_collider().get_class()
		# Player collision
		if type_collision == "RigidBody2D":
			direction = direction.bounce(collision.get_normal())
		# Brick collision
		if type_collision == "StaticBody2D":
			direction = direction.bounce(collision.get_normal())
	if position.y <= 0 + offset:
		direction.y = - direction.y
	if position.y >= screen_height + 50:
		direction.y = - direction.y
	# Screen lef-rigth limits
	if position.x <= 0 + offset or position.x >= screen_width - offset:
		direction.x = - direction.x

# The ball collisions with stick
func stick_collision(num_player, zone_touch, stick_direction):
	if num_player == 1:
		$AudioPlayer1.play()
	if num_player == 2:
		$AudioPlayer2.play()
		# Responding for collisions
	# Always the x-axis are going to be the opposite
	direction.x = - direction.x
	# Up stick zone
	if zone_touch == 0:
		# Change direction 0.3 if ball goes up-down and invert direction
		direction.y = change_direcction_y(direction.y, 0.3, true, false, true)
		if stick_direction == -1:	# Stick goes up
			# Ball goes up
			if direction.y < 0:
				speed += 60
			# Ball goes down
			if direction.y > 0:
				speed += 120
		elif stick_direction == 1: # Stick goes down
			# Ball goes up
			if direction.y < 0:
				direction.y = change_direcction_y(direction.y, -0.5, true, true, false)
				speed -= 20
			# Ball goes down
			if direction.y > 0:
				speed += 80
		elif stick_direction == 0: # Stick quiet
			speed += 60
	# Middle stick zone
	elif zone_touch == 2:
		if stick_direction == -1: # Stick goes up
			direction.y = change_direcction_y(direction.y, -0.5, true, true, false)
			# Ball goes up
			if direction.y < 0:
				speed += 50
			# Ball goes down
			if direction.y > 0:
				speed -= 20
		elif stick_direction == 1: # Stick goes down
			direction.y = change_direcction_y(direction.y, -0.5, true, true, false)
			# Ball goes up
			if direction.y < 0:
				speed -= 20
			# Ball goes down
			if direction.y > 0:
				speed += 50
		elif stick_direction == 0: # Stick quiet
			speed += 20
	# Down stick zone
	elif zone_touch == 4:
		# Change direction 0.3 if ball goes down-up and invert direction
		direction.y = change_direcction_y(direction.y, 0.3, false, true, true)
		if stick_direction == -1:  # Stick goes up
			# Ball goes up
			if direction.y < 0:
				speed += 80
			# Ball goes down
			if direction.y > 0:
				direction.y = change_direcction_y(direction.y, -0.5, true, true, false)
				speed -= 20
		elif stick_direction == 1: # Stick goes down
			# Ball goes up
			if direction.y < 0:
				speed += 120
			# Ball goes down
			if direction.y > 0:
				speed += 60
		elif stick_direction == 0: # Stick quiet
			speed += 60
			
func start_ball():
	# Inicializa la posición
	position = Vector2(screen_width / 2, screen_height / 2 + 35)
	# Inicializa la dirección - Sale hacia abajo con un angulo aleatorio
	direction = Vector2( random_number(-0.5, 0.5), 1)
	
func random_number(num_min, num_max):
	# Generate a random number between min_value (inclusive) and max_value (exclusive)
	var random_number = randf() * (num_max - num_min) + num_min
	print(random_number)
	return random_number

func accelerate(level):
	var acceleration
	if level <= 0 or level > 5:
		# No acceleration, returns 0
		acceleration = 0
	else:
		acceleration = level * 10
	return acceleration

func change_direcction_y(direction_y, variation, up_down, down_up, invert):
	'''Params'''
	var final_direction = direction_y
	
	# The ball is going up
	if direction_y < 0 and down_up == true:
		if abs(direction_y) + variation < 2.5:
			final_direction -= variation
		else:
			final_direction = - 2.5
		if invert:
			return - final_direction
	
	# The ball is going down
	if direction_y > 0 and up_down == true:
		if abs(direction_y) + variation < 2.5:
			final_direction += variation
		else:
			final_direction = 2.5
		if invert:
			return - final_direction
			
	return final_direction


