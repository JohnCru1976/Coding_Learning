extends Area2D

var direction		# Is a normalized 2D vector
var speed = 550		# Initial speed
var offset = 12
var ball_scale = 0.25
# Screen parameters
var screen_width
var screen_height

# Called when the node enters the scene tree for the first time.
func _ready():
	start_ball()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	print(direction)
	# Move the object on the actual direction
	position = position + direction.normalized() * speed * delta
	# Screen top-bottom limits
	if position.y <= 0 or position.y >= screen_height - 17 :
		direction.y = - direction.y
	if position.y <= 0:
		position.y = 3
	if position.y >= screen_height - 17:
		position.y = screen_height - 20
	# Screen lef-rigth limits
	if position.x <= 0: # Left
		get_parent().sum_point(2)
		self.queue_free()
	if position.x >= screen_width: # Right
		get_parent().sum_point(1)
		self.queue_free()

# The ball collisions with stick
func stick_collision(num_player, zone_touch, stick_direction):
	print("Soy la bola")
	print("\tHe tocado al jugador " + str(num_player) + " en la zona " +
		 str(zone_touch) + " con stick en dirección " + str(stick_direction))
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
	# Scale
	scale = Vector2(ball_scale, ball_scale)
	# Geeting the window dimensions
	screen_width = get_viewport().size.x
	screen_height = get_viewport().size.y
	# Inicializa la posición
	position = Vector2(screen_width / 2 - offset, screen_height / 2 - offset)
	# Inicializa la dirección
	direction = Vector2(random_direction(), random_number(-0.2, 0.2))
	

# Returns 1: Rigth or -1: Left
func random_direction():
	var direction_random = [1,-1]
	var random = randi()
	return direction_random[random % direction_random.size()]

func random_number(num_min, num_max):
	# Generate a random number between min_value (inclusive) and max_value (exclusive)
	var random_number = randf() * (num_max - num_min) + num_min
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

#func end_collision_connection():
#	var player1 = get_node("../Player1")
#	if player1:
#		connect("end_collision", player1["_on_ball_end_collision"], CONNECT_DEFERRED)
#	var player2 = get_node("../Player2")
#	if player2:
#		connect("end_collision", player2["_on_ball_end_collision"], CONNECT_DEFERRED)

