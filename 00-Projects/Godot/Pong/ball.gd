extends Area2D

var direction		# Is a normalized 2D vector
var speed = 400		# Initial speed
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
	# Move the object on the actual direction
	position = position + direction.normalized() * speed * delta
	# Screen top-bottom limits
	if position.y <= 0 or position.y >= screen_height - 17 :
		direction.y = - direction.y

func stick_collision(num_player, zone_touch, stick_direction):
	print("Soy la bola")
	print("\tHe tocado al jugador " + str(num_player) + " en la zona " +
		 str(zone_touch) + " con stick en dirección " + str(stick_direction))
	# Responding for collisions
	# Always the x-axis are going to be the opposite
	direction.x = - direction.x
	print("\tRebote")
	# Up stick zone
	if zone_touch == 0:
		if stick_direction == -1:	# Stick goes up
			
			pass
		elif stick_direction == 1: # Stick goes down
			
			pass
		elif stick_direction == 0: # Stick quiet
			
			pass
	# Middle-Up stick zone
	elif zone_touch == 1:
		if stick_direction == -1: # Stick goes up
			
			pass
		elif stick_direction == 1: # Stick goes down
			
			pass
		elif stick_direction == 0: # Stick quiet
			
			pass
	# Middle stick zone
	elif zone_touch == 2:
		if stick_direction == -1: # Stick goes up
			
			pass
		elif stick_direction == 1: # Stick goes down
			
			pass
		elif stick_direction == 0: # Stick quiet
			
			pass
	# Middle-Down stick zone
	elif zone_touch == 3:
		if stick_direction == -1: # Stick goes up
			
			pass 
		elif stick_direction == 1: # Stick goes down
			
			pass
		elif stick_direction == 0: # Stick quiet
			
			pass
	# Down stick zone
	elif zone_touch == 4:
		if stick_direction == -1:  # Stick goes up
			
			pass
		elif stick_direction == 1: # Stick goes down
			
			pass
		elif stick_direction == 0: # Stick quiet
			
			pass
	

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
	
	# TEST #
	#direction = Vector2(random_direction(), 0)

# Returns 1: Rigth or -1: Left
func random_direction():
	var direction_random = [1,-1]
	var random = randi()
	return direction_random[random % direction_random.size()]

func random_number(num_min, num_max):
	# Generate a random number between min_value (inclusive) and max_value (exclusive)
	var random_number = randf() * (num_max - num_min) + num_min
	return random_number

#func end_collision_connection():
#	var player1 = get_node("../Player1")
#	if player1:
#		connect("end_collision", player1["_on_ball_end_collision"], CONNECT_DEFERRED)
#	var player2 = get_node("../Player2")
#	if player2:
#		connect("end_collision", player2["_on_ball_end_collision"], CONNECT_DEFERRED)

